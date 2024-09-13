# python-template
python-template

## tree

```
your_project/
├── app/
│   ├── __init__.py
│   ├── main.py                # 应用入口
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py        # 配置文件
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py            # 依赖项
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── users.py
│   │           └── items.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── security.py        # 安全相关模块
│   │   └── errors.py          # 全局异常处理
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── item_service.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py         # 数据库初始化
│   └── tests/
│       ├── __init__.py
│       ├── conftest.py        # 测试配置
│       ├── test_users.py
│       └── test_items.py
├── alembic/                   # 数据库迁移
│   ├── versions/
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── scripts/                   # 脚本文件
│   └── run.sh
├── .env                       # 环境变量文件
├── .gitignore                 # Git 忽略文件
├── requirements.txt           # 项目依赖
├── README.md                  # 项目说明
└── setup.py                   # 包配置（可选）

```

