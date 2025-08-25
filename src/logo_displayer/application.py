import logging
import asyncio
import time

from pydoover.docker import Application
from pydoover import ui

from .app_config import LogoDisplayerConfig
from .app_ui import LogoDisplayerUI

log = logging.getLogger()

class LogoDisplayerApplication(Application):
    config: LogoDisplayerConfig  # not necessary, but helps your IDE provide autocomplete!
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.started: float = time.time()
        self.ui: LogoDisplayerUI = None
    
    async def setup(self):
        self.ui = LogoDisplayerUI(self.config)
        self.ui_manager.add_children(*self.ui.fetch())
        self.ui_manager.set_variant(ui.ApplicationVariant.stacked)

    async def main_loop(self):
        pass