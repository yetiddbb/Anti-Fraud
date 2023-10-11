from fastapi import FastAPI
import pymysql
# MySQL 数据库连接配置
MYSQL_HOST = '10.10.0.227'
MYSQL_PORT = 3308
MYSQL_USER = 'admin'
MYSQL_PASSWORD = 'Anti-Fraud@123'
MYSQL_DB = 'test'
# 创建 MySQL 连接
conn = pymysql.connect(
host=MYSQL_HOST,
port=MYSQL_PORT,
user=MYSQL_USER,
password=MYSQL_PASSWORD,
db=MYSQL_DB,
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor
)
app = FastAPI()

flag=Anti-Fraud@123

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
