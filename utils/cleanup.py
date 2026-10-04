# utils/cleanup.py
import os
import shutil
import asyncio
import time
from pathlib import Path
from utils.logger import logger
from config import config

async def cleanup_job_dir(job_dir: str) -> None:
    try:
        if os.path.exists(job_dir):
            await asyncio.to_thread(shutil.rmtree, job_dir, ignore_errors=True)
            logger.debug(f"Cleaned: {job_dir}")
    except Exception as e:
        logger.warning(f"Cleanup failed {job_dir}: {e}")

async def cleanup_old_dirs(max_age_hours: int = 2) -> None:
    work = Path(config.WORK_DIR)
    if not work.exists():
        return
    cutoff = time.time() - (max_age_hours * 3600)
    for item in work.iterdir():
        if item.is_dir():
            try
