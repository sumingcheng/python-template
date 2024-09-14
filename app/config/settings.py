import os


class Config:
    DATABASE_URL = os.getenv('DATABASE_URL', 'localhost:5432')
    DATABASE_USER = os.getenv('DATABASE_USER', 'admin')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'password')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'mydatabase')
    API_SECRET_KEY = os.getenv('API_SECRET_KEY', 'your_secret_key')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', 'your_access_token')

    required_vars = ['DATABASE_USER', 'DATABASE_PASSWORD', 'API_SECRET_KEY', 'ACCESS_TOKEN']
    for var in required_vars:
        if locals()[var] is None:
            raise ValueError(f"环境变量 {var} 未设置。")

    @classmethod
    def as_dict(cls):
        # 定义敏感的配置项名称
        sensitive_keys = {'DATABASE_PASSWORD', 'API_SECRET_KEY', 'ACCESS_TOKEN'}
        return {
            k: v for k, v in cls.__dict__.items()
            if not k.startswith('__') and not callable(v) and k not in sensitive_keys
        }
