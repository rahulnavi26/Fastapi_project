from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# MongoDB Atlas URL
MONGODB_URL = os.getenv("MONGODB_URL")

if not MONGODB_URL:
    raise ValueError("MONGODB_URL not found in .env file")

print("MongoDB URL Loaded Successfully")

# MongoDB Connection
client = MongoClient(MONGODB_URL)

try:
    client.admin.command("ping")
    print("✅ MongoDB Atlas Connected Successfully!")
except Exception as e:
    print("❌ MongoDB Connection Failed")
    print(e)

# Database
db = client["simpledb"]
collection = db["users"]

# FastAPI App
app = FastAPI()

# Static Folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates Folder
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    users = list(collection.find({}, {"_id": 0}))

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "users": users
        }
    )


@app.post("/add")
def add_user(
    name: str = Form(...),
    email: str = Form(...)
):
    collection.insert_one(
        {
            "name": name,
            "email": email
        }
    )

    return RedirectResponse(
        url="/",
        status_code=303
    )
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# MongoDB Atlas URL
MONGODB_URL = os.getenv("MONGODB_URL")

if not MONGODB_URL:
    raise ValueError("MONGODB_URL not found in .env file")

print("MongoDB URL Loaded Successfully")

# MongoDB Connection
client = MongoClient(MONGODB_URL)

try:
    client.admin.command("ping")
    print("✅ MongoDB Atlas Connected Successfully!")
except Exception as e:
    print("❌ MongoDB Connection Failed")
    print(e)

# Database
db = client["simpledb"]
collection = db["users"]

# FastAPI App
app = FastAPI()

# Static Folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates Folder
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    users = list(collection.find({}, {"_id": 0}))

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "users": users
        }
    )


@app.post("/add")
def add_user(
    name: str = Form(...),
    email: str = Form(...)
):
    collection.insert_one(
        {
            "name": name,
            "email": email
        }
    )

    return RedirectResponse(
        url="/",
        status_code=303
    )
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# MongoDB Atlas URL
MONGODB_URL = os.getenv("MONGODB_URL")

if not MONGODB_URL:
    raise ValueError("MONGODB_URL not found in .env file")

print("MongoDB URL Loaded Successfully")

# MongoDB Connection
client = MongoClient(MONGODB_URL)

try:
    client.admin.command("ping")
    print("✅ MongoDB Atlas Connected Successfully!")
except Exception as e:
    print("❌ MongoDB Connection Failed")
    print(e)

# Database
db = client["simpledb"]
collection = db["users"]

# FastAPI App
app = FastAPI()

# Static Folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates Folder
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    users = list(collection.find({}, {"_id": 0}))

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "users": users
        }
    )


@app.post("/add")
def add_user(
    name: str = Form(...),
    email: str = Form(...)
):
    collection.insert_one(
        {
            "name": name,
            "email": email
        }
    )

    return RedirectResponse(
        url="/",
        status_code=303
    )