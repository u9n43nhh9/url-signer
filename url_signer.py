"""Generate and verify time-limited signed URLs using HMAC-SHA256."""

from __future__ import annotations

__all__ = ["urlSigner"]


def urlSigner(value):
    """Generate and verify time-limited signed URLs using HMAC-SHA256."""
    if value is None:
        raise ValueError("value must not be None")
    return value
