#!/bin/bash
# /setup.sh

# 设置环境名称
ENV_NAME="template"

# 检查是否安装了 Conda
if ! command -v conda &> /dev/null
then
    echo "Conda 未安装，请先安装 Anaconda 或 Miniconda。"
    exit
fi

# 创建 Conda 环境
echo "正在创建 Conda 环境：$ENV_NAME"
conda env create -f environment.yml

# 激活环境
echo "激活 Conda 环境：$ENV_NAME"
source activate $ENV_NAME

# 安装依赖（已通过 environment.yml 安装，无需再次安装）
# 如果需要单独安装，可取消以下注释
# echo "安装依赖"
# conda install --yes --file requirements.txt

# 运行数据库迁移
echo "运行数据库迁移"
#alembic upgrade head

# 启动应用
echo "启动应用"
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
