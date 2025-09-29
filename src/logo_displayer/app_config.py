from pathlib import Path

from pydoover import config


class LogoDisplayerConfig(config.Schema):
    def __init__(self):
        self.logo_url = config.String(
            "Logo URL", 
            description="The URL of the logo to display",
            default="https://doover.com/wp-content/uploads/2025/02/Blue-Background-2.png"
        )
        
        self.max_logo_height = config.Number(
            "Max Logo Height", 
            description="The maximum height of the logo in pixels",
            default=150.0
        )

        self.position = config.Integer(
            "Position",
            default=80,  # fairly high
            minimum=0,
            maximum=999,
            description="The position of the logo in the UI. Smaller is higher, larger is lower. 100 is the default position of most apps.",
        )

def export():
    LogoDisplayerConfig().export(Path(__file__).parents[2] / "doover_config.json", "logo_displayer")

if __name__ == "__main__":
    export()
