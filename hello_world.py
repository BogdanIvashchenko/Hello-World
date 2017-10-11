import time
import os

is_prod = os.environ.get('GLOBAL_VARIABLE_STRING', None)
print(is_prod)
#from boto.s3.connection import S3Connection
#s3 = S3Connection(os.environ['GLOBAL_VARIABLE_STRING'])

print(GLOBAL_VARIABLE_STRING)
time.sleep(60)
