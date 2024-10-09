"""Custom client handling, including TestSourceStream base class."""

from __future__ import annotations

from singer_sdk.streams import Stream


class TestSourceStream(Stream):
    """Stream class for TestSource streams."""
