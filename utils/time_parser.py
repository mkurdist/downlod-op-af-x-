# utils/time_parser.py
import re
from typing import Optional

def parse_time(time_str: str) -> Optional[float]:
    s = time_str.strip().replace('،', ':').replace(',', '.')

    m = re.match(r'^(\d{1,2}):([0-5]\d):([0-5]\d(?:\.\d+)?)$', s)
    if m:
        return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))

    m = re.match(r'^(\d{1,3}):([0-5]\d(?:\.\d+)?)$', s)
    if m:
        return int(m.group(1)) * 60 + float(m.group(2))

    m = re.match(r'^(\d+(?:\.\d+)?)$', s)
    if m:
        return float(m.group(1))

    return None

def format_duration(seconds: float) -> str:
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"

def seconds_to_ffmpeg(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}"
