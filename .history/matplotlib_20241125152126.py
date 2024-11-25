import sys
print(sys.executable)  # Check Python interpreter path

try:
    import matplotlib.pyplot as plt
    print("Matplotlib version:", plt.__version__)
except ImportError as e:
    print("Import error:", e)