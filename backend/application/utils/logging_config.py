import logging
import json
import os
from datetime import datetime, timezone

from application.utils import get_env


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "module": record.module,
        };
        if record.exc_info:
            log_obj["exception"] = self.formatException(record.exc_info);
        return json.dumps(log_obj);


def is_development(app):
    if app.debug:
        return True;
    env = (get_env("FLASK_ENV") or "").lower();
    return env == "development";


def setup_logging(app):
    logger = app.logger;
    logger.setLevel(logging.DEBUG);
    # Avoid duplicate handlers when reloading
    if logger.handlers:
        return;

    if is_development(app):
        handler = logging.StreamHandler();
        handler.setLevel(logging.DEBUG);
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        );
        handler.setFormatter(formatter);
        logger.addHandler(handler);
    else:
        log_dir = get_env("LOG_DIR") or "logs";
        os.makedirs(log_dir, exist_ok=True);
        log_file = os.path.join(log_dir, "app.log");
        handler = logging.FileHandler(log_file, encoding="utf-8");
        handler.setLevel(logging.INFO);
        handler.setFormatter(JsonFormatter());
        logger.addHandler(handler);

    # Capture Werkzeug request logs with the same handler
    werkzeug_logger = logging.getLogger("werkzeug");
    werkzeug_logger.handlers.clear();
    werkzeug_logger.addHandler(logger.handlers[0]);
