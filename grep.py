import sys

if len(sys.argv) < 2:
    print('Usage: grep "string" [file]')
    sys.exit(1)

pattern = sys.argv[1]

if len(sys.argv) >= 3:                      # קבלת נתיב לקובץ
    try:
        f = open(sys.argv[2], encoding="utf-8", errors="replace")
    except OSError as e:
        print("grep:", e)
        sys.exit(1)
else:                                       # קריאה מ-stdin (pipe)
    f = sys.stdin

for num, line in enumerate(f, start=1):
    if pattern in line:
        print(f"{num}: {line.rstrip()}")