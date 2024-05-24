import psycopg2
from config import load_config
from flask import Flask # Here we are importing the Flask class. This class is used to create the app.
import pandas as pd
import json
app = Flask(__name__) # Here we are creating an instance of the Flask app.

# 取得config內的資訊
config = load_config()
Database = config['GCP']['database']
Host = config['GCP']['host']
User = config['GCP']['user']
Password = config['GCP']['password']
Port = config['GCP']['port']
# 連線
conn = psycopg2.connect(database=Database,
                        host=Host,
                        user=User,
                        password=Password,
                        port=Port)

def sign_in(r,cID,passw):
    p = False
    # 创建一个游标对象
    cur = conn.cursor()

    # 定义查询的 SQL 语句
    select_query = """
    SELECT user_id, username, password_hash, role, email
    FROM users
    WHERE user_id = %s AND role = %s AND password_hash = %s;
    """

    # 执行查询
    cur.execute(select_query, (cID, r, passw))

    # 获取查询结果
    result = cur.fetchone()

    # 检查是否有匹配的记录
    if result:
        print("Login successful")
        data = {
            "message" : "Login Successful"
        }
        print("回傳值：",data)
        return json.dumps(data)
    else:
        print("Login failed")
        data = {
           "message" : "Login failed"
        }
        print("回傳值：",data)
        return json.dumps(data)

    # 关闭游标和连接
    cur.close()
    conn.close()
    # for index, row in member_df.iterrows():
    #     if row['customer_ID'] == cID and row['pwd'] == passw and :
    #         print('登入成功')
    #         p=True
    #     elif row['customer_ID'] == cID and row['pwd'] != passw:
    #         print('帳號或密碼錯誤')
    #         p=True
    # if p == False:
    #     print('沒有在資料庫找到您的資料喔')

with open('signin.json', 'r') as f:
    sign_in_data = json.load(f)
r = sign_in_data['role']
cID = sign_in_data['email']
passw = sign_in_data['password_hash']
print(r,cID,passw)
sign_in(r,cID,passw)
# data = {'customer_ID': ['312706006','311706006'],
#         'pwd': ['Accc1234','Vcde1575']}
# member_df = pd.DataFrame(data)
# member_df =member_df.sort_values(by=['customer_ID'],ascending=True)
# print("資料庫內資料:\n",member_df)
# def sign_up():
#     with open('signin.json', 'r') as f:
#         sign_in_data = json.load(f)
#     cID = sign_in_data['customer_ID']
#     passw = sign_in_data['pwd']
#     member_df.loc[len(member_df.index)] = [cID,passw]
#     print(member_df)
#     print("註冊成功")