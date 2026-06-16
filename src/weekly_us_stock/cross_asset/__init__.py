"""Cross-asset evaluation spine (#7 skeleton). Importing the package registers
the built-in asset plugins (currently: equity)."""
from weekly_us_stock.cross_asset import equity as _equity  # noqa: F401  (registers on import)
