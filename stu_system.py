#定义一个列表存储所有学生的信息
stu = []
#增加学生信息
def add_stu():
    stu_ID = input("输入学生ID：")
    stu_name = input("输入学生姓名：")
    stu_age = input("输入学生年龄：")
    stu_class = input("输入学生班级：")
    #表示每个学生的信息用字典来存储
    stu_inf = {"ID":stu_ID,"name":stu_name,"age":stu_age,"class":stu_class}
    stu.append(stu_inf)
def main():
    while(True):
        # user_input = input(">")
        # print(user_input)
        #增加学生信息
        if(user_input == "1"):
            add_stu()
            print("hello world")
        elif(user_input == "0"):
            exit()

if __name__ == "__main__":
    main()