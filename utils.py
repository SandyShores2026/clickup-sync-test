"""Sample utility functions for string processing."""

import re
from collections import Counter


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_-]+", "-", text).strip("-")


def truncate(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate text to max_length, appending suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)].rstrip() + suffix


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word in text."""
    words = text.lower().split()
    return dict(Counter(words))
