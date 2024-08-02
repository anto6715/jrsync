from datetime import datetime
from pathlib import Path

from jrsync.core import pyrsync
import jrsync.conf as settings
from jrsync.model import Jsync


def execute(config: Path, date_to_sync: datetime) -> None:
    data = settings.read_config(config)

    jsync_objs = [Jsync(date_to_sync=date_to_sync, **d) for d in data]

    for js in jsync_objs:
        pyrsync.rsync(js.source_dir, js.dest_dir)
