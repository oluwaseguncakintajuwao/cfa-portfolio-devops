"""
Central configuration for the project.

DevOps principle:
- Read settings from environment variables (12-factor app style)
- Provide sensible defaults for local development
"""

from __future__ import annotations

import os
from dataclasses import dataclass

try:
    # Optional: makes local development easier if you later add a .env file
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # In CI/Docker, env vars are typically injected; .env may not exist
    pass


@dataclass(frozen=True)
class Settings:
    # Assets (CFA relevance: equity/bond/diversifier proxies)
    tickers: str = os.getenv("TICKERS", "SPY,AGG,GLD")

    # Date range for analysis (ISO format)
    start_date: str = os.getenv("START_DATE", "2016-01-01")
    end_date: str | None = os.getenv("END_DATE") or None  # None => today

    # Database connection (Postgres in Docker; can be swapped later)
    db_url: str = os.getenv(
        "DB_URL",
        "postgresql+psycopg2://postgres:postgres@localhost:5432/cfa"
    )

    # Optional: where to write logs/reports later
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

    def ticker_list(self) -> list[str]:
        """Return tickers as a clean list."""
        return [t.strip().upper() for t in self.tickers.split(",") if t.strip()]
