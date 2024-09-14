from fastapi import FastAPI
from app.api.v1.api import api_router
from app.middleware.cors import setup_cors
from app.core.config import settings

app = FastAPI(title="用户管理系统")

# 设置 CORS 中间件
setup_cors(app)

# 注册路由
app.include_router(api_router, prefix=settings.API_V1_STR)
