# 🚀 Space Intelligence API

A FastAPI project combining NASA and SpaceX live data with a beautiful dashboard.

## Screenshots

### 🏠 Home
![Hero](screenshots/hero.png)

### 🌌 NASA Today
![NASA](screenshots/nasa.png)

### 🚀 SpaceX Latest
![SpaceX](screenshots/spacex.png)

### ⚡ Space Summary
![Summary](screenshots/summary.png)

## Endpoints
- `GET /` — Welcome
- `GET /space/today` — NASA Astronomy Picture of the Day
- `GET /spacex/latest` — Latest SpaceX Launch
- `GET /space/summary` — Combined overview
- `GET /dashboard` — Web Dashboard UI

## Setup
```bash
pip install fastapi uvicorn requests python-dotenv jinja2
uvicorn main:app --reload
```

## Tech Stack
- FastAPI · Python · NASA API · SpaceX API