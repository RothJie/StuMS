import pymysql

userName = ""

def open():
    db = pymysql.connect(host="localhost", port=3306, user="root", passwd="abc123", db="tb_student")
    return db

def execute(sql,values):
    """执行增加、删除、修改，values必须用元组括起来（value，）"""
    db = open()
    cursor = db.cursor()
    try:
        cursor.execute(sql, values)
        db.commit()
        return 1
    except Exception as e:
        print(e)
        db.rollback()
        return 0
    finally:
        cursor.close()
        db.close()

def query(sql,*keys):
    db = open()
    cursor = db.cursor()
    cursor.execute(sql, keys)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

if __name__ == '__main__':
    print(execute("INSERT INTO tb_user VALUES(%s,%s)",('z',"z")))
    print(query("select * from tb_user;",))