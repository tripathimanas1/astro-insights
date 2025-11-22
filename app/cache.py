from typing import Dict, Tuple
from datetime import date


CacheKey = Tuple[str, str, str, str]

_cache: Dict[CacheKey, str] = {}


def get_from_cache(name: str, zodiac: str, date_for: date, language: str) -> str | None:
    key: CacheKey = (name.lower().strip(), zodiac, date_for.isoformat(), language)
    return _cache.get(key)


def store_in_cache(name: str, zodiac: str, date_for: date, language: str, insight: str) -> None:
    key: CacheKey = (name.lower().strip(), zodiac, date_for.isoformat(), language)
    _cache[key] = insight
