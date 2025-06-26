from contextlib import asynccontextmanager
from fastapi import FastAPI
from configs.databases import connect_mongodb
from routers import examinations, users
from fastapi.middleware.cors import CORSMiddleware
from configs.databases import logger,db_client

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(examinations.router)

@app.get("/")
async def root():
    return {"message": "Healthy!"}