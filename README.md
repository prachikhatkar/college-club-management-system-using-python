 College Club Management System

A simple terminal-based Python project for managing college clubs, members, events, and event registrations.

 Features
- Add, view, and search clubs
- Add and view club members
- Add and view events
- Register members for events
- Prevent duplicate records
- Basic input validation
- Local `.txt` file storage
- Command-line interface

Run
```bash
python main.py
```

Structure
```text
college_club_management_system/
├── data/
│   ├── clubs.txt
│   ├── members.txt
│   ├── events.txt
│   └── registrations.txt
├── main.py
├── clubs.py
├── members.py
├── events.py
├── registrations.py
├── database.py
├── validators.py
├── README.md
├── statement.md
├── TESTING.md
├── requirements.txt
└── .gitignore
```

 Storage
`clubs.txt`: club_id|club_name|category|coordinator  
`members.txt`: member_id|member_name|club_id  
`events.txt`: event_id|event_name|club_id|date  
`registrations.txt`: member_id|event_id

 Limitations
No GUI, web server, cloud database, authentication, or external packages.

Future Enhancements
- Club-admin login
- Event attendance
- Announcements and reminders
- SQLite/MySQL support
- GUI using Tkinter
- CSV/PDF reports
