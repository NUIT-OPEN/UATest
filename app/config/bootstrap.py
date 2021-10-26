from saika import BaseConfig


class BootstrapConfig(BaseConfig):
    local_res = True

    def merge(self) -> dict:
        return dict(
            BOOTSTRAP_SERVE_LOCAL=self.local_res
        )
