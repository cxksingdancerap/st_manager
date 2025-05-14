from pymysql import Connection
conn=Connection(                  # 连接数据库
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)
# print(conn.get_server_info())
cursor=conn.cursor()    # 获取游标对象
conn.select_db("lgt")   # 选择数据库
# cursor.execute("create table st(name varchar(20),age varchar(20),score varchar(20))")                # 执行sql语句
class student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def __str__(self):
        return f"学生姓名: {self.name} 学生年龄: {self.age} 学生分数: {self.score}"


def print_menu():
    print("-------------------")
    print("1:添加学生")
    print("2:删除学生")
    print("3:修改学生")
    print("4:查询学生")
    print("5:显示所有学生")
    print("6:退出系统")
    print("-------------------")


def add_student():
    name,age,score=input("请分别输入学生的姓名，年龄和分数，用空格分开:").split()
    sql_check = "SELECT name FROM st WHERE name = %s"
    cursor.execute(sql_check, (name,))
    res=cursor.fetchall()
    if not res:
        s=student(name,age,score)
        sql = "INSERT INTO st (name, age, score) VALUES (%s, %s, %s)"
        cursor.execute(sql, (s.name, s.age, s.score))
        conn.commit()
    else:
        print("重名了")
def show_info():
    sql = "SELECT * FROM st"
    cursor.execute(sql)
    res=cursor.fetchall()
    for r in res:
        print(f"姓名:{r[0]},年龄:{r[1]},分数:{r[2]}")

def del_info():
    name=input("请输入要删除学生的姓名:")
    sql_check = "SELECT name FROM st WHERE name = %s"
    cursor.execute(sql_check, (name,))
    res=cursor.fetchall()
    if res:
        sql = "delete from st  where name=%s"
        cursor.execute(sql,(name,))
        conn.commit()
        print("删除成功！")
    else:
        print("要删除学生的信息不存在")


def modify_student():
    name = input("请输入要想要更改的学生的姓名:")
    sql_check = "SELECT name FROM st WHERE name = %s"
    cursor.execute(sql_check, (name,))
    res=cursor.fetchall()
    if res:
        moddify_name,age,score=input("请输入要修改的姓名，年龄和分数，用空格分隔:").split()
        sql="update st set name=%s, age=%s,score=%s where name=%s"
        cursor.execute(sql,(moddify_name,age,score,name))
        conn.commit()
        print("修改成功！")
    else:print("学生信息不存在！")


def search_student():
    name=input("请输入要查询的学生姓名:")
    sql_check = "SELECT name FROM st WHERE name = %s"
    cursor.execute(sql_check, (name,))
    res = cursor.fetchall()
    if res:
        sql="select * from st where name=%s"
        cursor.execute(sql,(name))
        res = cursor.fetchall()
        for r in res:
            print(f"姓名:{r[0]},年龄:{r[1]},分数:{r[2]}")
    else:print("您输入的学生信息不存在")
def main():
    while True:
        print_menu()
        choice=int(input("请输入您需要的功能："))
        if choice==1:
            add_student()
        elif choice==2:
            del_info()
        elif choice==3:
            modify_student()
        elif choice==4:
            search_student()
        elif choice==5:
            show_info()
        elif choice==6:
            print("退出系统")
            conn.close()
            break
if __name__=="__main__":
    main()