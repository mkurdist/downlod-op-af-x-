# utils/logger.py
import logging
import logging.handlers
import os
import re
from config import config

_SENSITIVE_PATTERNS = [
    (re.compile(r'bot\d+:[A-Za-z0-9_-]{35,}'), 'BOT:***'),
    (re.compile(r'Authorization:\s*\S+'), 'Authorization:***'),
    (re.compile(r'token=[A-Za-z0-9_-]+'), 'token=***'),
]

class SensitiveFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        try:
            msg = record.getMessage()
            for pattern, repl in _SENSITIVE_PATTERNS:
                msg = pattern.sub(repl, msg)
            record.msg = msg
            record.args = ()
        except Exception:
            pass
        return True

def setup_logger(name: str = "xbot") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.DEBUG)

    fmt = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)
    ch.addFilter(SensitiveFilter())

    os.makedirs(config.LOG_DIR, exist_ok=True)
    fh = logging.handlers.RotatingFileHandler(
        os.path.join(config.LOG_DIR, "bot.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding='utf-8'
    )
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)
    fh.addFilter(SensitiveFilter())

    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

logger = setup_logger()
