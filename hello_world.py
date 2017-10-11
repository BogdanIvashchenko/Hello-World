import time
import os

GLOBAL_VARIABLE_STRING = os.environ.get('GLOBAL_VARIABLE_STRING', None)
print(GLOBAL_VARIABLE_STRING)
time.sleep(60)
