from database import EVENTS_FILE,CLUBS_FILE,read_lines,append_line
def add_event():
 i=input("Enter event ID: ").strip(); n=input("Enter event name: ").strip(); c=input("Enter club ID: ").strip(); d=input("Enter event date (YYYY-MM-DD): ").strip()
 if not i or not n or not c or not d: print("Event details cannot be empty."); return
 if any(x.split("|")[0]==i for x in read_lines(EVENTS_FILE)): print("Event already exists."); return
 if not any(x.split("|")[0]==c for x in read_lines(CLUBS_FILE)): print("Club ID not found."); return
 if len(d.split("-"))!=3 or not all(x.isdigit() for x in d.split("-")): print("Invalid date format."); return
 append_line(EVENTS_FILE,f"{i}|{n}|{c}|{d}"); print("Event added successfully.")
def view_events():
 a=read_lines(EVENTS_FILE)
 if not a: print("No events found."); return
 print("\n----- Club Events -----")
 for x in a:
  i,n,c,d=x.split("|"); print(f"Event ID: {i} | {n} | Club ID: {c} | Date: {d}")
