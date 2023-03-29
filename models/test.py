import importlib.util
from ..leye import add

#module_path = '../test.py'
#abs_path = importlib.util.find_spec(module_path).origin
#leye = importlib.util.module_from_spec(importlib.util.spec_from_file_location('leye', abs_path))
#importlib.util.exec_module(leye)

b = add(1, 2, 3, 4, 5)
print(b)
