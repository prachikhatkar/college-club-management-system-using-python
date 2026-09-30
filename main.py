from clubs import add_club,view_clubs,search_club
from members import add_member,view_members
from events import add_event,view_events
from registrations import register_member,view_registrations

def menu():
 print("\n===== College Club Management System =====")
 print("1. Add Club\n2. View Clubs\n3. Search Club\n4. Add Member\n5. View Members\n6. Add Event\n7. View Events\n8. Register Member for Event\n9. View Registrations\n10. Exit")

def main():
 while True:
  menu(); c=input("Enter your choice: ").strip()
  if c=="1": add_club()
  elif c=="2": view_clubs()
  elif c=="3": search_club()
  elif c=="4": add_member()
  elif c=="5": view_members()
  elif c=="6": add_event()
  elif c=="7": view_events()
  elif c=="8": register_member()
  elif c=="9": view_registrations()
  elif c=="10": print("Thank you for using the College Club Management System."); break
  else: print("Invalid choice. Please enter 1 to 10.")

if __name__=="__main__": main()
