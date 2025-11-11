# 🚀 FastAPI Base Template

This project is a **base FastAPI application** that can be easily cloned and customized for any microservice or API project.  
It includes environment management, dynamic configuration, structured logging, and a clean modular folder layout.

> 🧩 Originally designed for the **User Management Service** integrated with **Keycloak**, this can be reused as a boilerplate for new FastAPI-based services.

---

## 🧠 Tech Stack

- **FastAPI** — modern async Python web framework  
- **PostgreSQL** — database  
- **SQLAlchemy (Async)** — ORM for models and queries  
- **Alembic** — database migrations  
- **Pydantic** — for schema validation  
- **Uvicorn** — ASGI server  
- **dotenv** — environment variable management  
- **Logging** — dynamic and structured

---

## 🧰 Prerequisites

- **Python 3.13+**
- **pip** (comes with Python)
- **Git**

---

## ⚙️ Project Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-base-template.git
cd fastapi-base-template
````

---

### 2️⃣ Create and Activate a Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

For **macOS/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create your environment file:

```bash
cp .env.example .env
```

Update `.env` values like database URL, allowed origins, and app name.

---

### 5️⃣ Run the FastAPI App

```bash
uvicorn src.main:app --reload --port 8000
```

App will be available at → [http://localhost:8000](http://localhost:8000)

---

### 6️⃣ (Optional) Run Alembic Migrations

If you’re using a database, initialize migrations:

```bash
alembic upgrade head
```

---

## 🧱 Project Structure

```
src/
├── api/
│   ├── routers/
│   └── v1/
├── app/
│   ├── config.py
│   └── middleware/
├── core/
│   ├── logger.py
│   └── common/
├── models/
├── services/
├── utils/
│   └── rsa_keys.py
└── main.py
```

---

## 🪵 Logging

Logging is dynamically configured via environment variables:

```env
LOG_LEVEL=INFO
LOGGER_NAME=FastAPI
```

Logs include timestamps, logger name, and severity level.

---

## 🧩 Environment Variables Overview

See `.env.example` for a full list. Example:

```env
APP_NAME=FastAPI Base Service
APP_VERSION=1.0.0
DEBUG=True
PORT=8000
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/userdb
ALLOWED_ORIGINS=http://localhost:3000
```

---

## 🏁 Startup Logs

When the app starts, you’ll see logs like:

```
INFO  Project 'DSG User Management Service' (v1.0.0) is running successfully 🚀
INFO  RSA keys loaded: ✅
```

---

## 📜 License

MIT License © 2025 — Data Safeguard Inc. or Your Organization Name

---

## 💡 Next Steps

* Add your API endpoints under `src/api/v1/`
* Implement services and database models
* Configure Keycloak integration if needed
* Dockerize your app for deployment

---
