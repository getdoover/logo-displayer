from pydoover import ui


class LogoDisplayerUI:
    def __init__(self, config):
        self.config = config
        self.logo = ui.RemoteComponent(
            "logo",
            "Logo",
            position=1000,
            component_url="https://getdoover.github.io/image-loader/ImageLoader.js",
            image_url=self.config.logo_url.value,
            max_height=self.config.max_logo_height.value,
        )

    def fetch(self):
        return [self.logo]

