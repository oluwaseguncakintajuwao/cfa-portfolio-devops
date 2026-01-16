"""
Database utilities.

Responsibilities:
- Create a SQLAlchemy engine
- Provide safe helpers for executing SQL
- Keep DB logic out of business logic
"""

from __future__ import annotations

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine


def get_engine(db_url: str) -> Engine:
    """
    Create a SQLAlchemy engine.

    DevOps notes:
    - pool_pre_ping avoids stale connections
    - future=True opts into SQLAlchemy 2.x behavior
    """
    return create_engine(
        db_url,
        pool_pre_ping=True,
        future=True,
    )


def run_sql(engine: Engine, sql: str) -> None:
    """
    Execute raw SQL (DDL or DML).

    Used for:
    - Creating tables
    - Creating views
    - One-off setup tasks
    """
    with engine.begin() as conn:
        conn.execute(text(sql))
