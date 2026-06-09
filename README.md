# Intern Task Tracker

A task manager REST API built with **Django** and **Django REST Framework (DRF)**. This application allows authenticated users to perform complete CRUD operations on their tasks, featuring task validation, status/priority filtering, overdue task checks, search, and containerization support using Docker.

---

## 🛠️ Tech Stack
* **Framework**: Django
* **API Toolkit**: Django REST Framework (DRF)
* **Database**: SQLite (local)
* **Containerization**: Docker

---

## 🚀 Local Setup Instructions

Follow these steps to run the application on your local machine:

### 1. Set Up Virtual Environment
Initialize and activate a Python virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate it (Mac/Linux)
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Database Migrations
Create the local SQLite database and structure:
```bash
python manage.py migrate
```

### 4. Create a Superuser
Create an admin account to log in and manage tasks:
```bash
python manage.py createsuperuser
```

### 5. Run the Server
Launch the development server:
```bash
python manage.py runserver 127.0.0.1:8010
```
Your API will now be available at `http://127.0.0.1:8010/`.

---

## 🔒 Authentication

All API endpoints (except login pages) require authentication. 
* **Browsable API**: Access the login page at `http://127.0.0.1:8010/api-auth/login/` in your browser.
* **API Clients (Postman/Curl)**: Use **Basic Authentication** by providing your superuser `username` and `password` in the request authorization headers.

---

## 📡 API Endpoints

The root tasks API endpoint is `/api/tasks/`. Below are the available CRUD operations:

| Action | HTTP Method | URL Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **Create Task** | `POST` | `/api/tasks/` | Creates a new task. |
| **List Tasks** | `GET` | `/api/tasks/` | Retrieves all tasks owned by the logged-in user. |
| **Get Task Details** | `GET` | `/api/tasks/<id>/` | Retrieves details of a specific task. |
| **Update Task** | `PUT` / `PATCH` | `/api/tasks/<id>/` | Modifies fields of an existing task. |
| **Delete Task** | `DELETE` | `/api/tasks/<id>/` | Removes a task. |

### 📝 Sample POST Payload
```json
{
    "title": "Finish Project Documentation",
    "description": "Create README, Postman collections, and demo video.",
    "status": "In Progress",
    "priority": "High",
    "due_date": "2026-06-15"
}
```

---

## 🔍 Filtering and Searching

You can query and filter the tasks using standard query parameters:

* **Filter by Status**:
  `GET /api/tasks/?status=Pending`
* **Filter by Priority**:
  `GET /api/tasks/?priority=High`
* **Combined Filter**:
  `GET /api/tasks/?status=In Progress&priority=Medium`
* **Filter Overdue Tasks** (due date is in the past and status is not Completed):
  `GET /api/tasks/?overdue=true`
* **Search by Title**:
  `GET /api/tasks/?search=Document`

---

## 🐳 Docker Deployment

### 1. Build the Docker Image
```bash
docker build -t task-tracker-api .
```

### 2. Run the Container
```bash
docker run -p 8010:8010 task-tracker-api
```
Once run, the application maps port `8010` and runs migrations automatically inside the container.
