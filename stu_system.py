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

def del_stu():
    del_id = input("输入需要删除的学生id：")
    for stu_inf in stu:
        if(stu_inf["ID"] == del_id):
            stu.remove(stu_inf)
            print("学生信息已经删除！")
        else:
            print("没有找到目标学生")

def search_stu():
    tar_id = input("输入想要查询的学生id：")
    for stu_inf in stu:
        if(stu_inf["ID"] == tar_id):
            print("查询到的学生信息如下所示：")
            print(stu_inf["ID"])
            print(stu_inf["name"])
            print(stu_inf["age"])
            print(stu_inf["class"])
        else:
            print("没有找到目标学生")

def main():
    while(True):
        user_input = input(">")
        # print(user_input)
        #增加学生信息
        if(user_input == "1"):
            add_stu()
            print("学生信息增加成功！")
        #删除学生的信息
        elif(user_input == "2"):
            del_stu()
        #查询学生信息
        elif(user_input == "3"):
            search_stu()
        #退出入口
        elif(user_input == "0"):
            exit()
        
if __name__ == "__main__":
    main()