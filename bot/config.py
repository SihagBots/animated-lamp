import os


def _get_env_int(name, default=None, *, required=False):
    raw = os.environ.get(name)
    if raw in (None, ""):
        if required:
            raise ValueError(f"Missing required environment variable: {name}")
        return default
    return int(raw)


def _get_env_int_list(name, default=None, *, required=False):
    raw = os.environ.get(name, "")
    values = [value for value in raw.split() if value]
    if not values:
        if required:
            raise ValueError(f"Missing required environment variable: {name}")
        return default or []
    return [int(value) for value in values]


def _get_env_str(name, default=None, *, required=False):
    raw = os.environ.get(name, default)
    if required and (raw is None or raw == ""):
        raise ValueError(f"Missing required environment variable: {name}")
    return raw


class Config:

    API_ID = _get_env_int("API_ID", required=True)
    API_HASH = _get_env_str("API_HASH", required=True)
    BOT_TOKEN = _get_env_str("BOT_TOKEN", required=True)
    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")
    LOG_CHANNEL = _get_env_int("LOG_CHANNEL", required=True)
    DATABASE_URL = _get_env_str("DATABASE_URL", required=True)
    AUTH_USERS = _get_env_int_list("AUTH_USERS", required=True)
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = _get_env_int("TRACK_CHANNEL", default=0)
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 5))
    HOST = os.environ.get("HOST", "")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
