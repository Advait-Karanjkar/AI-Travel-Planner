# ==============================================================
# app.py — Flask Application Entry Point
#
# AI Travel Planner powered by IBM watsonx.ai + Granite models.
# Run: python app.py   or   flask run
# ==============================================================

import logging
from flask import Flask
from config import ActiveConfig
from routes.main import main_bp
from routes.api import api_bp

# ── Logging configuration ─────────────────────────────────────
logging.basicConfig(
    level=logging.DEBUG if ActiveConfig.DEBUG else logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def create_app() -> Flask:
    """Application factory — creates and configures the Flask app."""

    app = Flask(__name__, template_folder="templates", static_folder="static")

    # Load settings from config object
    app.config.from_object(ActiveConfig)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    logger.info("✈️  %s v%s started", ActiveConfig.APP_NAME, ActiveConfig.APP_VERSION)
    logger.info("🤖  Model: %s", ActiveConfig.WATSONX_MODEL_ID)
    logger.info("🌐  watsonx URL: %s", ActiveConfig.WATSONX_URL)

    return app


# ── Entry point ───────────────────────────────────────────────
app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=ActiveConfig.PORT,
        debug=ActiveConfig.DEBUG,
    )
