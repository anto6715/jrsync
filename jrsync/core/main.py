from datetime import datetime
from pathlib import Path

import jrsync.conf as settings
from jrsync.core import pyrsync
from jrsync.model import Jsync


def execute(config: Path, date_to_sync: datetime, **kwargs) -> None:
    """
    Entry point for executing jrsync commands
    Args:
        config: Path to configuration file
        date_to_sync: Date to synchronize

    """
    data = settings.read_config(config)

    # use configuration to builds jsync objects
    jsync_objs = [Jsync(date_to_sync=date_to_sync, **d) for d in data]

    # call rsync for each jsync object
    for js in jsync_objs:
        pyrsync.rsync(js.source_dir, js.dest_dir, **kwargs)
