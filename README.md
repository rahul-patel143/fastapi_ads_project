# FastAPI Cron Job Application 🚀

This project is a FastAPI-based application that includes a **cron job** using APScheduler. The cron job runs automatically at specified intervals, and the latest logs can be retrieved via an API.
Note: I have include .env, ads_db.sql and logs file too for reference.

## 📌 Features
- FastAPI-based RESTful API
- APScheduler for scheduled cron jobs
- API to retrieve ad-metrics with datetime range, region, platform
- API to retrieve the last 10 logs
- Dockerized application for easy deployment

## 🏗️ Project Structure
```
/fastapi_cron_project
│── /app
│   │── main.py             # FastAPI application with cron job
│   │── cron_job.py         # Cron job logic (auto-starts with app)
│   │── dependencies.py     # Database dependencies (if required)
│   │── models.py           # SQLAlchemy models
│   │── schemas.py          # Pydantic request/response models
│   │── requirements.txt    # Python dependencies
│── Dockerfile              # Docker configuration
│── README.md               # Project documentation
│── .gitignore              # Ignore unnecessary files
│── ads_db.sql              # postgres database backup file
```

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/rahul-patel143/fastapi_ads_project.git
cd fastapi_ads_project
```

### 2️⃣ Create and Activate a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI App
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 5️⃣ Test the API
```sh
curl http://127.0.0.1:8000  # Check Health of app
curl http://127.0.0.1:8000/logs  # Fetch latest 10 logs
```

---

## 🐳 Docker Setup

### 1️⃣ Build the Docker Image
```sh
docker build -t fastapi-cron-app .
```

### 2️⃣ Run the Docker Container
```sh
docker run -d -p 8000:8000 --name fastapi-cron fastapi-cron-app
```

### 3️⃣ Check Running Containers
```sh
docker ps
```

### 4️⃣ View Logs in Docker
```sh
docker logs fastapi-cron
```

### 5️⃣ Stop & Remove the Container
```sh
docker stop fastapi-cron
docker rm fastapi-cron
```

---

## 📡 API Endpoints

| Method | Endpoint      | Description                            |
|--------|--------------|-----------------------------------------|
| GET    |`/ad-metrics` | Fetch the ad-metrics data using filters |
| GET    | `/logs`      | Fetch the latest 10 cron logs           |
| GET    | `/health`    | Check if the server is running          |

---

## 📂 Environment Variables (Optional)
If needed, create a `.env` file and configure environment variables.

---

## 📝 Author
Developed by **Rahul Patel** 🚀

