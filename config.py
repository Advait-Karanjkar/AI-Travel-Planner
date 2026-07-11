# ==============================================================
# config.py — Application Configuration
# Reads from .env and exposes typed settings to the Flask app.
# ==============================================================

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    """Base configuration shared by all environments."""

    # ── Flask ──────────────────────────────────────────────────
    SECRET_KEY: str = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")
    DEBUG: bool = os.getenv("FLASK_DEBUG", "False").lower() == "true"

    # ── IBM watsonx.ai ────────────────────────────────────────
    IBM_API_KEY: str = os.getenv("IBM_API_KEY", "")
    WATSONX_PROJECT_ID: str = os.getenv("WATSONX_PROJECT_ID", "")
    WATSONX_URL: str = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
    WATSONX_MODEL_ID: str = os.getenv("WATSONX_MODEL_ID", "ibm/granite-3-8b-instruct")

    # ── Model Generation Parameters ──────────────────────────
    MAX_NEW_TOKENS: int = 2048        # Maximum tokens in the response
    MIN_NEW_TOKENS: int = 50          # Minimum tokens in the response
    TEMPERATURE: float = 0.7          # Creativity (0.0 = deterministic, 1.0 = creative)
    TOP_P: float = 0.9                # Nucleus sampling probability
    TOP_K: int = 50                   # Top-K sampling
    REPETITION_PENALTY: float = 1.1   # Penalise repeated phrases

    # ── Application ───────────────────────────────────────────
    APP_NAME: str = "AI Travel Planner"
    APP_VERSION: str = "1.0.0"
    PORT: int = int(os.getenv("PORT", 5000))


class DevelopmentConfig(Config):
    """Development-specific settings."""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production-specific settings."""
    DEBUG = False
    TESTING = False
    # In production override SECRET_KEY via environment variable


# Active config selected by FLASK_ENV
config_map = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}

ActiveConfig = config_map.get(os.getenv("FLASK_ENV", "development"), DevelopmentConfig)
