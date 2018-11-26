import os
import subprocess

cmd = " git --version"

result = os.system(cmd)
print("Result:" , result)

result = subprocess.run([cmd],shell=True)
print("Result:" , result)

result = subprocess.check_output(cmd)
print("Result:" , result)
