import os
import sys
from pathlib import Path
import platform

print("Python version:", sys.version.split()[0])
print("Platform:", platform.platform())
print("Current working directory:", Path.cwd())
print("Python executable:", sys.executable)
print("Project root exists:", Path(".").exists())
print("VENV variable set:", "VIRTUAL_ENV" in os.environ)
print("PYTHONPATH:", os.environ.get("PYTHONPATH", "<not set>"))
print("Smoke test passed.")
