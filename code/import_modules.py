import importlib
from pathlib import Path

def get_modules(path: str = "./actions/"):
    path: Path = Path(path)
    classes = []
    for module in path.glob("*.py"):
        mode = importlib.import_module(f"{path.parts[-1]}.{module.stem}")
        for cl in dir(mode):
            cl = getattr(mode, cl)
            if type(cl) is type and hasattr(cl, "forward"):
                classes.append(cl)
    return classes
