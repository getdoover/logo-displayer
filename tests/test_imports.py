"""
Basic tests for an application.

This ensures all modules are importable and that the config is valid.
"""

def test_import_app():
    from logo_displayer.application import LogoDisplayerApplication
    assert LogoDisplayerApplication

def test_config():
    from logo_displayer.app_config import LogoDisplayerConfig

    config = LogoDisplayerConfig()
    assert isinstance(config.to_dict(), dict)

def test_ui():
    from logo_displayer.app_ui import LogoDisplayerUI
    assert LogoDisplayerUI
