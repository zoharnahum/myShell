import sys
import subprocess


subprocess.run(["cmd", "/c", "dir"] + sys.argv[1:])
