# Hybrid MVC & Clean Code Project
A complete Django aplicaation for ooking an appointment, users can login by token, they don't need to sibmit info for logging in.
Note that:
Some parts specially doctors part is incomplete, but updating

UI: Bootstrap
Back-end: Django
## Overview
This project combines **MVC architecture** with **Clean Code principles** to build a maintainable, scalable, and clear web application. It features multiple apps, including `myapp`, `chatapp` (with partial WebSocket), and `otpauth`.

---

## Architecture

### MVC
- **Model:** Database models and ORM
- **View:** Templates and frontend UI
- **Controller:** Request handling, business logic

### Clean Code
- Single Responsibility Principle per module
- Clear, meaningful naming conventions
- Minimal duplication
- Small, focused functions/methods

---

## Features
- User authentication with OTP
- Basic chat functionality (WebSocket partial)
- Modular app design for easy expansion

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/alih982/Django-application-with-JWT-Authentication
cd test1

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
or for python3:
pip3 install -r requirements.txt

Run migrations:

python3 manage.py makemigrations
python3 manage.py migrate

Run the application:

python3 manage.py runserver
