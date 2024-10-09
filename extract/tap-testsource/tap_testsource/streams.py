"""Stream type classes for tap-testsource."""

from __future__ import annotations

import sys
import typing as t
from typing import Iterable
from datetime import date
from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_testsource.client import TestSourceStream

if sys.version_info >= (3, 9):
    pass
else:
    pass


class TestStream(TestSourceStream):
    """Define custom stream."""

    name = "meltano-test-tap-2"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    is_sorted = True
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property(
            "id",
            th.StringType,
            description="The user's system ID",
        ),
        th.Property(
            "birthday",
            th.DateType,
            description="The user's birthday",
        ),
    ).to_dict()

    def get_records(
            self,
            context # noqa: ARG002
    ) -> Iterable[dict]:
        """Get dummy records."""
        records = [
            {"name": "foo", "id": "1", "birthday": "10000-01-01"},
            {"name": "boz", "id": "123", "birthday": "2020-01-01"},
            {"name": "bar", "id": "2", "birthday": "2020-01-01"},
            {"name": "bar", "id": "4", "birthday": "2020-01-01"},
        ]
        yield from (record for record in records)
