import sys
import os

module_path = os.path.abspath(os.path.join(os.pardir))
if module_path not in sys.path:
    print(module_path)
    sys.path.append(module_path)