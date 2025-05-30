from ngapp import AppAccessConfig, AppConfig
from . import __version__, DemoApp

_DESCRIPTION = "App descrition shown in preview"

config = AppConfig(
    name="Demo App",
    version = __version__,
    python_class=DemoApp,
    frontend_pip_dependencies=[],
    frontend_dependencies=[],
    description=_DESCRIPTION,
    compute_environments=[],
    access=AppAccessConfig()
)
    
