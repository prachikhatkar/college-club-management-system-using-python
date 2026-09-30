from database import MEMBERS_FILE,CLUBS_FILE,read_lines,append_line
def add_member():
 i=input("Enter member ID: ").strip(); n=input("Enter member name: ").strip(); c=input("Enter club ID: ").strip()
 if not i or not n: print("Member details cannot be empty."); return
 if any(x.split("|")[0]==i for x in read_lines(MEMBERS_FILE)): print("Member already exists."); return
 if not any(x.split("|")[0]==c for x in read_lines(CLUBS_FILE)): print("Club ID not found."); return
 append_line(MEMBERS_FILE,f"{i}|{n}|{c}"); print("Member added successfully.")
def view_members():
 a=read_lines(MEMBERS_FILE)
 if not a: print("No members found."); return
 print("\n----- Club Members -----")
 for x in a:
  i,n,c=x.split("|"); print(f"Member ID: {i} | Name: {n} | Club ID: {c}")
