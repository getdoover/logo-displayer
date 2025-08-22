from pydoover.docker import run_app

from .application import LogoDisplayerApplication
from .app_config import LogoDisplayerConfig

def main():
    """
    Run the application.
    """
    run_app(LogoDisplayerApplication(config=LogoDisplayerConfig()))
