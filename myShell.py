import os
import subprocess
import getpass

# התיקייה שבה נמצאים קבצי התוכנית
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# פקודות שממומשות בקובץ bat + קובץ py נפרדים
EXTERNAL = {"ls", "hexdump", "grep"}

# טבלת התפריט:
MENU = [
    ("hello",   "הדפסת hello ואת שם המשתמש שהריץ אותו"),
    ("ls",      "הצגת תוכן התיקייה הנוכחית (אפשר גם: ls <שם תיקייה>)"),
    ("hexdump", "הדפסת קובץ בצורה הקסדצימלית (hexdump <קובץ>)"),
    ("grep",    "חיפוש מחרוזת בקובץ או ב-pipe (grep \"מחרוזת\" <קובץ>)"),
    ("cd",      "מעבר לתיקייה אחרת (cd <תיקייה>, גם .. וגם \\)"),
    ("help",    "הצגת התפריט הזה"),
    ("exit",    "יציאה"),
]


def show_menu():
    '''
    מדפיסה את תפריט הפקודות למשתמש
    :return:
    '''
    print("=" * 62)
    print("                      MYSHELL - תפריט פקודות")
    print("=" * 62)
    print(f"{'פקודה':<10}| תיאור")
    print("-" * 62)
    # מעבר על כל הפקודות בטבלה והדפסת שורה לכל אחת
    for name, desc in MENU:
        print(f"{name:<10}| {desc}")
    print("=" * 62)


def do_hello():
    """מדפיסה את שם המשתמש המחובר למערכת"""
    print(getpass.getuser())


def do_cd(arg):
    """cd: מעבר לתיקייה אחרת. תומכת בנתיבים, ב-\\ וב-.."""
    # הסרת רווחים וגרשיים (למקרה של נתיב עם רווחים בתוך "")
    arg = arg.strip().strip('"')
    # בלי פרמטר: מדפיסים את התיקייה הנוכחית
    if not arg:
        print(os.getcwd())
        return
    try:
        os.chdir(arg)
    except OSError as e:
        print("cd:", e)


def run_external(name, line):
    """מפעילה את קובץ ה-bat של הפקודה, והוא מפעיל את קובץ ה-py שלה"""
    env = os.environ.copy()
    env["PATH"] = BASE_DIR + os.pathsep + env.get("PATH", "")
    rest = line[len(name):]
    subprocess.run(f"{name}.bat{rest}", shell=True, env=env)


def main():
    show_menu()
    while True:
        try:
            line = input(os.getcwd() + ">").strip()
        except Exception as e:
            print()
            break
        # שורה ריקה: ממשיכים לפקודה הבאה
        if not line:
            continue

        # שם הפקודה הוא המילה הראשונה בשורה
        name = line.split()[0].lower()
        if name == "exit":
            break                           # יציאה מהתוכנית
        elif name == "hello":
            do_hello()                      # ממומשת בתוכנית הראשית
        elif name == "help":
            show_menu()                     # הצגת התפריט שוב
        elif name == "cd":
            do_cd(line[2:])
        elif name in EXTERNAL:
            run_external(name, line)        # ls / hexdump / grep דרך bat + py
        else:
            print(f"'{name}' is not a supported command. type 'help' to see the menu")


if __name__ == "__main__":
    main()