import sys
import subprocess

# שקול ל-dir, כולל תמיכה בפרמטר של שם תיקייה
subprocess.run(["cmd", "/c", "dir"] + sys.argv[1:])