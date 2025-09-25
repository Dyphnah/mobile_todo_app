# Task Management Backend API

This is a RESTful backend for a task and project management system built with Django and Django REST Framework (DRF). It supports role-based access, project creation, task tracking, and comment management.


## Features

- Role-based access control (Owner, Project Manager, Staff, Client)
- Project creation restricted to managers and owners
- Task creation and status updates (pending, in progress, review, completed, blocked)
- Comments scoped under projects
- Filter tasks by project or view them under project endpoints
- Flexible API structure with both global and nested access


## Tech Stack

- Python 3.10+
- Django 5.2+
- Django REST Framework
- SQLite (default, can be swapped for PostgreSQL)
- Token-based authentication (optional)


## Installation

```bash
# Clone the repo
git clone git@github.com:Dyphnah/mobile_todo_app.git
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

## API Endpoints

```bash

#Projects

GET /projects/ — List all projects

POST /projects/ — Create a project (restricted)

GET /projects/<id>/tasks/ — View tasks under a project

POST /projects/<id>/add_task/ — Add task under a project

GET /projects/<id>/comments/ — View comments under a project

POST /projects/<id>/add_comment/ — Add comment under a project

# Tasks
GET /tasks/ — List all tasks

GET /tasks/?project=<id> — Filter tasks by project

POST /tasks/<id>/completed/ — Mark task as completed

POST /tasks/<id>/review/ — Mark task for review

POST /tasks/<id>/pending/ — Mark task as pending

POST /tasks/<id>/in_progress/ — Mark task as in progress

POST /tasks/<id>/backlog/ — Mark task as blocked


```

## Testing
Use Django’s built-in test framework or tools like Postman to test endpoints. Make sure to authenticate if using protected routes.

## License
Feel free to use and modify it for personal projects.

## Contributions
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## Contact
For questions or feedback, reach out via GitHub or email: nyandukodyphnah4@gmail.com



