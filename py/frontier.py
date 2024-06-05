#!/usr/bin/python
print('Content-type: text/html\n')
import sys
import subprocess
result = subprocess.run(['python', 'dream1.py'], capture_output=True, text=True)
print(result.stdout)