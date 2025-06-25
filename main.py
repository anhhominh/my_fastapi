from contextlib import asynccontextmanager
from fastapi import FastAPI
from pymongo import MongoClient
from configs.databases import connect_mongodb
from routers import users
import logging

# Configure the logger (often done at the start of the application)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # Set the minimum level to log
# Create a console handler and add it to the logger
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

#--- Khởi tạo db_client
db_client: MongoClient = None

# --- Lifespan Event Handler ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup Logic (Logic khi ứng dụng khởi động) ---
    global db_client
    try:
        db_client = connect_mongodb()
    except Exception as e:
        logger.error(f"Có lỗi: {e}")
    yield

    # --- Shutdown Logic (Logic khi ứng dụng tắt) ---
    if db_client:
        db_client.close()
        print("Đã đóng kết nối MongoDB.")
    else:
        print("Không có kết nối MongoDB nào để đóng.")

# Khởi tạo ứng dụng FastAPI với lifespan
app = FastAPI(lifespan=lifespan)

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Healthy!"}