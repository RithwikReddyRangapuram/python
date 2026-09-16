"""Setup verification."""
import sys
print("Python:", sys.version.split()[0])
print("Running from:", sys.executable)
import numpy, pandas
print("numpy:", numpy.__version__, "| pandas:", pandas.__version__)
