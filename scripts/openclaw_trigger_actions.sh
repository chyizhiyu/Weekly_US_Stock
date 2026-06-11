#!/usr/bin/env bash
set -euo pipefail

# Manually trigger the Weekly US Stock GitHub Actions workflow by pushing a
# disposable tag, then wait for - and print - the Feishu summary that matches
# THIS exact trigger (tag or source SHA recorded in run_metadata.json).

REPO_DIR="${WEEKLY_US_STOCK_REPO_DIR:-$(pwd)}"
REMOTE="${WEEKLY_US_STOCK_GIT_REMOTE:-origin}"
RESULTS_BRANCH="${WEEKLY_US_STOCK_RESULTS_BRANCH:-weekly-us-stock-results}"
POLL_SECONDS="${WEEKLY_US_STOCK_POLL_SECONDS:-60}"
TIMEOUT_SECONDS="${WEEKLY_US_STOCK_TIMEOUT_SECONDS:-7200}"

if [ -n "${WEEKLY_US_STOCK_GIT_SSH_KEY:-}" ]; then
  export GIT_SSH_COMMAND="ssh -i ${WEEKLY_US_STOCK_GIT_SSH_KEY} -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
elif [ -f "$HOME/.ssh/weekly_us_stock_github_ed25519" ]; then
  export GIT_SSH_COMMAND="ssh -i $HOME/.ssh/weekly_us_stock_github_ed25519 -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
fi

cd "$REPO_DIR"

REMOTE_REF="${WEEKLY_US_STOCK_GIT_REMOTE_URL:-$REMOTE}"
if [ -z "${WEEKLY_US_STOCK_GIT_REMOTE_URL:-}" ]; then
  remote_url="$(git remote get-url "$REMOTE" 2>/dev/null || true)"
  if [ -n "${GIT_SSH_COMMAND:-}" ] && [[ "$remote_url" == https://github.com/* ]]; then
    repo_path="${remote_url#https://github.com/}"
    repo_path="${repo_path%.git}"
    REMOTE_REF="ssh://git@github.com/${repo_path}.git"
  fi
fi

git fetch "$REMOTE_REF" main
git checkout main
git pull --ff-only "$REMOTE_REF" main

SOURCE_SHA="$(git rev-parse HEAD)"
BASE_TAG="weekly-us-stock-$(TZ=Asia/Shanghai date +%Y%m%d-%H%M%S)"
TAG="${WEEKLY_US_STOCK_TAG:-$BASE_TAG}"
suffix=1
while git rev-parse -q --verify "refs/tags/$TAG" >/dev/null; do
  TAG="${BASE_TAG}-${suffix}"
  suffix=$((suffix + 1))
done

git tag "$TAG" "$SOURCE_SHA"
git push "$REMOTE_REF" "refs/tags/$TAG"

echo "Weekly US Stock tag pushed: $TAG" >&2
echo "Source commit: $SOURCE_SHA" >&2
echo "Waiting for $RESULTS_BRANCH/latest/feishu_summary.md ..." >&2

deadline=$((SECONDS + TIMEOUT_SECONDS))
while [ "$SECONDS" -lt "$deadline" ]; do
  git fetch "$REMOTE_REF" "$RESULTS_BRANCH:refs/remotes/origin/$RESULTS_BRANCH" >/dev/null 2>&1 || true

  metadata_file="$(mktemp)"
  if git show "origin/$RESULTS_BRANCH:latest/run_metadata.json" > "$metadata_file" 2>/dev/null; then
    if python3 - "$metadata_file" "$TAG" "$SOURCE_SHA" <<'PY'
import json
import sys
from pathlib import Path

metadata = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
expected_tag = sys.argv[2]
expected_sha = sys.argv[3]
if metadata.get("tag") == expected_tag or metadata.get("source_sha") == expected_sha:
    raise SystemExit(0)
raise SystemExit(1)
PY
    then
      echo >&2
      git show "origin/$RESULTS_BRANCH:latest/feishu_summary.md"
      rm -f "$metadata_file"
      exit 0
    fi
  fi
  rm -f "$metadata_file"

  echo "Result not ready for $TAG; sleeping ${POLL_SECONDS}s ..." >&2
  sleep "$POLL_SECONDS"
done

echo "ERROR: timed out waiting for the Weekly US Stock result for tag $TAG" >&2
exit 1
