from fastapi import FastAPI

from app.middleware.cors import setup_cors

app = FastAPI()
setup_cors(app)

# 注册路由
# app.include_router(router)
