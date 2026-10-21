import sys
import os
import subprocess

if len(sys.argv) != 2:
    print("Usage: hexdump <file>")
    sys.exit(1)

path = sys.argv[1]
if not os.path.isfile(path):
    print("hexdump: file not found:", path)
    sys.exit(1)

# שקול ל-certutil -dump "filename.ext"
subprocess.run(["certutil", "-dump", path])