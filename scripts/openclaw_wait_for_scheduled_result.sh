#!/usr/bin/env bash
set -euo pipefail

# Wait for this week's scheduled Weekly US Stock result and print the Feishu
# summary to stdout (OpenClaw relays stdout to the Feishu chat verbatim).
#
# Freshness guarantees (so last week's report can never be re-sent):
# - latest/run_metadata.json must have as_of == the latest completed US
#   trading day per the NYSE calendar (DST and holiday aware), and
# - generated_at must fall inside the current schedule window (>= the most
#   recent Saturday 00:00 UTC).
# Validation runs through weekly_us_stock.tools.verify_result_metadata, which
# is standard-library-only: no pip install is needed on the OpenClaw host.
#
# Suggested OpenClaw cron (Saturday 08:05 Beijing):
#   cd /path/to/Weekly_US_Stock
#   git pull --ff-only origin main
#   WEEKLY_US_STOCK_TIMEOUT_SECONDS=7200 scripts/openclaw_wait_for_scheduled_result.sh

RESULTS_BRANCH="${WEEKLY_US_STOCK_RESULTS_BRANCH:-weekly-us-stock-results}"
POLL_SECONDS="${WEEKLY_US_STOCK_POLL_SECONDS:-60}"
TIMEOUT_SECONDS="${WEEKLY_US_STOCK_TIMEOUT_SECONDS:-7200}"
EXPECTED_AS_OF="${WEEKLY_US_STOCK_EXPECTED_AS_OF:-}"
REPO_DIR="${WEEKLY_US_STOCK_REPO_DIR:-$(pwd)}"

cd "$REPO_DIR"
export PYTHONPATH="${REPO_DIR}/src${PYTHONPATH:+:$PYTHONPATH}"

if [ -z "$EXPECTED_AS_OF" ]; then
  EXPECTED_AS_OF="$(python3 -m weekly_us_stock.tools.expected_as_of)"
fi

echo "Waiting for the scheduled Weekly US Stock result for $EXPECTED_AS_OF ..." >&2

deadline=$((SECONDS + TIMEOUT_SECONDS))
last_error=""
while [ "$SECONDS" -lt "$deadline" ]; do
  if ! git fetch --quiet origin "$RESULTS_BRANCH"; then
    last_error="git fetch of $RESULTS_BRANCH failed"
    echo "$last_error; retrying in ${POLL_SECONDS}s." >&2
    sleep "$POLL_SECONDS"
    continue
  fi

  metadata="$(git show "origin/$RESULTS_BRANCH:latest/run_metadata.json" 2>/dev/null || true)"
  if [ -z "$metadata" ]; then
    last_error="latest/run_metadata.json not found on $RESULTS_BRANCH"
  elif printf '%s' "$metadata" | python3 -m weekly_us_stock.tools.verify_result_metadata \
      --expected-as-of "$EXPECTED_AS_OF"; then
    git show "origin/$RESULTS_BRANCH:latest/feishu_summary.md"
    exit 0
  else
    last_error="published result failed freshness validation (see stderr above)"
  fi

  sleep "$POLL_SECONDS"
done

echo "ERROR: timed out after ${TIMEOUT_SECONDS}s waiting for the Weekly US Stock" \
     "result for $EXPECTED_AS_OF. Last problem: ${last_error:-unknown}." >&2
echo "Check the GitHub Actions 'Weekly US Stock Run' workflow for failures." >&2
exit 1
