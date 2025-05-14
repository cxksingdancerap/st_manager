class_info=[]

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
    global class_info
    name,age,score=input("请分别输入学生的姓名，年龄和分数，用空格分开:").split()
    for s1 in class_info:
        if name==s1.name:
            print("学生重名了！")
            return
    s=student(name,age,score)
    class_info.append(s)
    # for s1 in class_info:
    #     print(s1)


def show_info():
    for s1 in class_info:
        print(s1)


def del_info():
    global class_info
    name=input("请输入要删除学生的信息:")
    for s1 in class_info:
        if name==s1.name:
            class_info.remove(s1)
            print("删除学生信息成功")
            return
    print("要删除学生的信息不存在")


def modify_student():
    global class_info
    name=input("请输入您想要修改学生的姓名:")
    for s1 in class_info:
        if s1.name==name:
            name1, age1, score1 = input("请分别输入学生的姓名，年龄和分数，用空格分开:").split()
            s1.name,s1.age,s1.score=name1,age1,score1
            print("修改学生信息成功！")
            return
    print("学生信息不存在！")


def search_student():
    global class_info
    name=input("请输入要查询的学生姓名:")
    for s1 in class_info:
        if s1.name==name:
            print(s1)
            return
    print("您输入的学生信息不存在")
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
            break
if __name__=="__main__":
    main()