from database import CLUBS_FILE,read_lines,append_line
def add_club():
 i=input("Enter club ID: ").strip()
 if not i: print("Club ID cannot be empty."); return
 if any(x.split("|")[0]==i for x in read_lines(CLUBS_FILE)): print("Club already exists."); return
 n=input("Enter club name: ").strip(); c=input("Enter club category: ").strip(); co=input("Enter coordinator name: ").strip()
 if not n or not c or not co: print("Club details cannot be empty."); return
 append_line(CLUBS_FILE,f"{i}|{n}|{c}|{co}"); print("Club added successfully.")
def view_clubs():
 a=read_lines(CLUBS_FILE)
 if not a: print("No clubs found."); return
 print("\n----- College Clubs -----")
 for x in a:
  i,n,c,co=x.split("|"); print(f"ID: {i} | {n} | Category: {c} | Coordinator: {co}")
def search_club():
 k=input("Enter club ID or name to search: ").strip().lower()
 found=False
 for x in read_lines(CLUBS_FILE):
  i,n,c,co=x.split("|")
  if k and (k in i.lower() or k in n.lower()): print(f"ID: {i} | {n} | Category: {c} | Coordinator: {co}"); found=True
 if not found: print("No matching club found.")
