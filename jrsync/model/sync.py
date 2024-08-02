from datetime import datetime
from pathlib import Path
from typing import List

from pydantic import BaseModel, Field

import jrsync.conf as settings


class Jsync(BaseModel):
    date_to_sync: datetime
    source_dir: Path
    dest_dir: Path
    file_to_sync: List[str] | str = Field(settings.ALL_DIRECTORY)
    day: str = Field("*")
