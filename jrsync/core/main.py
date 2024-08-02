from datetime import datetime
from pathlib import Path

import jrsync.conf as settings
from jrsync.model import Jsync


def execute(config: Path, date_to_sync: datetime) -> None:
    data = settings.read_config(config)
    print(data)

    jsync_objs = [Jsync(date_to_sync=date_to_sync, **d) for d in data]

    for js in jsync_objs:
        print(js)
