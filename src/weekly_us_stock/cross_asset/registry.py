"""Asset-model registry: map an asset_class string to its plugin."""
from __future__ import annotations

from weekly_us_stock.cross_asset.base import AssetModel

_REGISTRY: dict[str, AssetModel] = {}


def register_asset_model(model: AssetModel) -> None:
    _REGISTRY[model.asset_class] = model


def get_asset_model(asset_class: str) -> AssetModel:
    if asset_class not in _REGISTRY:
        raise KeyError(f"no asset model registered for {asset_class!r}")
    return _REGISTRY[asset_class]


def registered_asset_classes() -> list[str]:
    return sorted(_REGISTRY)
