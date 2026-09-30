from database import REGISTRATIONS_FILE,MEMBERS_FILE,EVENTS_FILE,read_lines,append_line
def register_member():
 m=input("Enter member ID: ").strip(); e=input("Enter event ID: ").strip()
 if not any(x.split("|")[0]==m for x in read_lines(MEMBERS_FILE)): print("Member ID not found."); return
 if not any(x.split("|")[0]==e for x in read_lines(EVENTS_FILE)): print("Event ID not found."); return
 if any(x==f"{m}|{e}" for x in read_lines(REGISTRATIONS_FILE)): print("Member is already registered."); return
 append_line(REGISTRATIONS_FILE,f"{m}|{e}"); print("Member registered successfully.")
def view_registrations():
 a=read_lines(REGISTRATIONS_FILE)
 if not a: print("No registrations found."); return
 print("\n----- Event Registrations -----")
 for x in a:
  m,e=x.split("|"); print(f"Member ID: {m} | Event ID: {e}")
