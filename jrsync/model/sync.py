from datetime import datetime
from pathlib import Path
from typing import List

from pydantic import BaseModel, Field, field_validator
from pydantic_core.core_schema import ValidationInfo

import jrsync.conf as settings
from jrsync.utils import str_parser


class Jsync(BaseModel):
    date_to_sync: datetime
    source_dir: Path
    dest_dir: Path
    file_to_sync: List[str] | str = Field(settings.ALL_DIRECTORY)
    day: str = Field("*")

    @field_validator("source_dir", "dest_dir", mode="before")
    @classmethod
    def resolve_path(cls, v: str, info: ValidationInfo) -> Path:
        resolved_str_path = str_parser.resolve_str(v, info.data["date_to_sync"])
        return Path(resolved_str_path)
