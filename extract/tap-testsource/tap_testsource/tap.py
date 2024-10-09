"""TestSource tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_testsource import streams


class TapTestSource(Tap):
    """TestSource tap class."""

    name = "tap-testsource"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "test_val",
            th.StringType,
            required=True,
            description="dummy value, does nothing",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.TestSourceStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [streams.TestStream(tap=self)]


if __name__ == "__main__":
    TapTestSource.cli()
