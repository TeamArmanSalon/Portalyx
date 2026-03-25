# Portalyx – Student Portal System

## Overview

Portalyx is a web-based portal designed for educational institutions to manage academic processes and facilitate communication within the school environment. It provides a centralized system where students, faculty, administrators, and registrars can efficiently access and manage information relevant to their roles.

---

## Purpose

The purpose of Portalyx is to:

* Centralize academic information and services in one platform
* Provide secure and organized access for different user roles
* Simplify workflows such as enrollment, grading, and user management
* Improve efficiency and transparency in academic operations

---

## System Roles

### Student

* Access personal dashboard
* View profile and academic-related information
* Interact with enrolled subjects and records
* ...

### Faculty

* Manage classes and assigned subjects
* Handle student grading and academic evaluation
* Access teaching-related data
* ...

### Admin

* Manage users across the system
* Oversee system operations and configurations
* Access reports and administrative tools
* ...

### Registrar

* Handle student enrollment processes
* Manage academic records and documentation
* Generate institutional reports
* ...

---

## System Architecture

Portalyx follows a structured and modular architecture:

* **Frontend:**
  Built using HTML, CSS, and JavaScript for user interaction and interface design

* **Backend:**
  Developed using Python Flask, handling API requests, business logic, and system operations

* **Database:**
  Uses MariaDB/MySQL for data storage and management

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/TeamArmanSalon/Portalyx.git
cd Portalyx/backend
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv

#Activate:
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate # Window
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the backend folder:

```env
SECRET_KEY=your-secret-key
```

### 5. Run the Server

```bash
python portalyx_app.py
```

### 6. Access the API

Open your browser or Postman:

```
http://localhost:5555/
```

Example endpoints:

* `/api/auth`
* `/api/student`
* `/api/admin`
* `/api/faculty`
* `/api/registrar`

---

## Security

The system is designed with security in mind:

* Role-based access control
* Authentication mechanisms for user login
* Future implementation of token-based authentication (e.g., JWT)
* Protection of sensitive data through environment variables

---

## Conclusion

Portalyx aims to be a scalable and maintainable academic management system by applying clean architecture principles and separating responsibilities across different system components.
