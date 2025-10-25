import yaml

class ConfigLoader:
    def __init__(self, path="config/config.yaml"):
        with open(path, "r") as f:
            self.config = yaml.safe_load(f)

    def get(self, key, default=None):
        keys = key.split(".")
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value or default
