from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")
# env file load
load_dotenv()
NASA_API_KEY=os.getenv("NASA_API_KEY"
                       )
# my first instance creation
app = FastAPI(
    title="Space Intelligence API",
    description="Combines NASA and SpaceX data in one place",
    version="1.0.0"
)
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
# first end point
@app.get("/")
def home():
    return{
        "message":"Hi There! Welcome to Space Intelligence API 🚀",
        "endpoints": ["/space/today", "/spacex/latest", "/space/summary"]

    }

#nasa pic of the day
@app.get("/space/today")
def get_apod():
    url=f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return {
        "title": data["title"],
        "date": data["date"],
        "explanation": data["explanation"],
        "image_url": data["url"]
    }  
# spacex latest
@app.get("/spacex/latest")
def get_latest_launch():
    url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(url)
    data = response.json()
    return {
        "mission_name": data["name"],
        "date": data["date_utc"],
        "success": data["success"],
        "details": data["details"],
        "webcast": data["links"]["webcast"]
    }
# Combined summary of NASA + SpaceX
@app.get("/space/summary")
def get_summary():
    # Fetch NASA data
    nasa_url = "https://api.nasa.gov/planetary/apod?api_key=" + NASA_API_KEY
    nasa_response = requests.get(nasa_url)
    nasa_data = nasa_response.json()

    # Fetch SpaceX data
    spacex_url = "https://api.spacexdata.com/v4/launches/latest"
    spacex_response = requests.get(spacex_url)
    spacex_data = spacex_response.json()

    # Combine both into one response
    return {
        "nasa": {
            "title": nasa_data["title"],
            "date": nasa_data["date"],
            "image_url": nasa_data["url"]
        },
        "spacex": {
            "mission_name": spacex_data["name"],
            "date": spacex_data["date_utc"],
            "success": spacex_data["success"]
        }
    }
    