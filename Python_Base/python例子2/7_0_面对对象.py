# -*- coding: UTF-8 -*-
# coding=gbk
# 7.	在下述代码的基础上，生成两个子类的实例化对象，并打印输出这两个对象的所有属性。
# class UniversityMember:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getName(self):
#         return self.name

#     def getAge(self):
#         return self.age


# class Student(UniversityMember):
#     def __init__(self, name, age, sno, mark):
#         UniversityMember.__init__(self, name, age)
#         self.sno = sno
#         self.mark = mark

#     def getSno(self):
#         pass

#     def getMark(self):
#         pass


# def getSno(self):
#     return self.sno


# def getMark(self):
#     return self.mark


# class Teacher(UniversityMember):
#     def __init__(self, name, age, tno, salary):
#         UniversityMember.__init__(self, name, age)
#         self.tno = tno
#         self.salary = salary

#     def getTno(self):
#         return self.tno

#     def getSalary(self):
#         return self.salary


# student = Student(input("enter student's name:"), input("enter student's age:"), input("enter student sno:"), input("enter student's mark:"))  # 实例化一个学生对象
# teacher = Teacher(input("enter teacher's name:"), input("enter teacher's age:"), input("enter teacher's tno:"), input("enter teacher's salary:"))   # 实例化一个教师对象
# print("student: name:{},age:{},sno:{},mark:{}".format(student.getName(), student.getAge(), student.getSno(), student.getMark()))    #输出学生对象 
# print("teacher: name:{},age:{},tno:{},salary:{}".format(teacher.getName(), teacher.getAge(), teacher.getTno(), teacher.getSalary())) #输出教师对象


# -*- coding: UTF-8 -*-
# coding=gbk
# 7.在下述代码的基础上，生成两个子类的实例化对象，并打印输出这两个对象的所有属性。

class UniversityMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Student(UniversityMember):
    def __init__(self, name, age, sno, mark):
        # 学生类继承自UniversityMember类
        UniversityMember.__init__(self, name, age)
        self.sno = sno  # 学号
        self.mark = mark  # 成绩

    def getSno(self):
        pass

    def getMark(self):
        pass

def getSno(self):
    return self.sno

def getMark(self):
    return self.mark

class Teacher(UniversityMember):
    def __init__(self, name, age, tno, salary):
        # 教师类继承自UniversityMember类
        UniversityMember.__init__(self, name, age)
        self.tno = tno  # 教师号
        self.salary = salary  # 工资

    def getTno(self):
        return self.tno

    def getSalary(self):
        return self.salary

# 实例化一个学生对象
student = Student(input("enter student's name:"), input("enter student's age:"), input("enter student sno:"), input("enter student's mark:"))
# 实例化一个教师对象
teacher = Teacher(input("enter teacher's name:"), input("enter teacher's age:"), input("enter teacher's tno:"), input("enter teacher's salary:"))

# 输出学生对象的信息
print("student: name:{},age:{},sno:{},mark:{}".format(student.getName(), student.getAge(), student.getSno(), student.getMark()))
# 输出教师对象的信息
print("teacher: name:{},age:{},tno:{},salary:{}".format(teacher.getName(), teacher.getAge(), teacher.getTno(), teacher.getSalary()))

