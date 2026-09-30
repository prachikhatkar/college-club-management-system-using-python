from pathlib import Path
DATA_DIR=Path(__file__).parent/"data"
CLUBS_FILE=DATA_DIR/"clubs.txt"; MEMBERS_FILE=DATA_DIR/"members.txt"; EVENTS_FILE=DATA_DIR/"events.txt"; REGISTRATIONS_FILE=DATA_DIR/"registrations.txt"
DATA_DIR.mkdir(exist_ok=True)
def read_lines(path):
 if not path.exists(): return []
 with open(path,"r",encoding="utf-8") as f: return [x.strip() for x in f if x.strip()]
def append_line(path,line):
 with open(path,"a",encoding="utf-8") as f: f.write(line+"\n")
