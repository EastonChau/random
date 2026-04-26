# Student Contact Book
import os
import time

def printBorder(color):
    colorDic = {
        "GREEN" : "\033[0;32m",
        "RED"   : "\033[0;31m",
        "BLUE"  : "\033[0;34m",
        "WHITE" : "\033[0m",
        "Gold": "\033[0;33m"
    }
    print(f"{colorDic[color]}={colorDic["WHITE"]}"*70)
    return 0
    
def splash():
    colorDic = {
        "GREEN" : "\033[0;32m",
        "RED"   : "\033[0;31m",
        "BLUE"  : "\033[0;34m",
        "WHITE" : "\033[0m",
        "GOLD" : "\033[0;33m"
    }
    printBorder("BLUE")
    student = r"""
    ||   ____    _____   _   _   ____    _____   _   _   _____ 
    ||  / ___|  |_   _| | | | | |  _ \  | ____| | \ | | |_   _|
    ||  \___ \    | |   | | | | | | | | |  _|   |  \| |   | |  
    ||   ___) |   | |   | |_| | | |_| | | |___  | |\  |   | |  
    ||  |____/    |_|    \___/  |____/  |_____| |_| \_|   |_|  
    """
    contact = r"""
    ||   ____     ___    _   _   _____      _       ____   _____ 
    ||  / ___|   / _ \  | \ | | |_   _|    / \     / ___| |_   _|
    ||  | |     | | | | |  \| |   | |     / _ \   | |       | |  
    ||  | |___  | |_| | | |\  |   | |    / ___ \  | |___    | |  
    ||  \____|   \___/  |_| \_|   |_|   /_/   \_\  \____|   |_|  
    """
    book = r"""
    ||   ____     ___     ___    _  __
    ||  | __ )   / _ \   / _ \  | |/ /
    ||  |  _ \  | | | | | | | | | ' / 
    ||  | |_) | | |_| | | |_| | | . \ 
    ||  |____/   \___/   \___/  |_|\_\
    """
    print(f"{colorDic["RED"]}{student}{colorDic["WHITE"]}")
    time.sleep(1)
    print(f"{colorDic["BLUE"]}{contact}{colorDic["WHITE"]}")
    time.sleep(1)
    print(f"{colorDic["GREEN"]}{book}{colorDic["WHITE"]}")
    time.sleep(1)
    print(f"{colorDic["GOLD"]}Author: Easton Chau{colorDic["WHITE"]}")
    time.sleep(1)
    printBorder("BLUE")

# Part 1: create / reload the initial list of students (list of tuples)

studentList = []
dataFileName = "data.txt"
directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, dataFileName)

def readData() :
    studentList.clear()
    try:
        
        with open(file_path, "r") as file:
            for line in file:
                columns = tuple(line.strip().split(','))
                studentList.append(columns)

    except FileNotFoundError:
        print("File Not Found")

# Part 2: display all students
def printData():
    readData()
    printBorder("RED")
    print(f"{'STUDENT DATABASE':^70}")
    printBorder("WHITE")
    print(f"{'ID':^10}|{'Name':^20}|{'Major':^40}")
    print("-"*70)
    for line in studentList:
        id = line[0]
        name = line[1]
        major = line[2]
        print(f"{id:^10}|{name:^20}|{major:^40}")
    printBorder("WHITE")
    printBorder("RED")

# Part 3: add a new student
def addStudent():
    readData()
    printBorder("RED")
    print(f"{'NEW ENTRY FORM':^70}")
    printBorder("WHITE")
    name = input("Student Name:   ")
    option = input("Computer Science (a),\n" \
    "Data Science and Engineering (b),\n" \
    "Financial Technology (c),\n"\
    "Applied Artificial Intelligence (d), &\n"\
    "Computer Engineering (e)\n"\
    "Major (a/b/c/d/e):   ")
    match option:
        case "a":
            major = "Computer Science"
        case "b":
            major = "Data Science and Engineering"
        case "c":
            major = "Financial Technology"
        case "d":
            major = "Applied Artificial Intelligence"
        case "e":
            major = "Computer Engineering"
        case _:
            print("Error: Unknown Major")
            return
    
    last_studentID = studentList[-1][0]
    new_studentID = "s2026" + str(int(last_studentID[5:])+1)

    studentTupple = (new_studentID, name, major)
    
    with open(file_path, "a") as file:
        file.write(",".join(studentTupple)+"\n")
    printBorder("RED")

# Part 4: search by ID
def search():
    readData()
    printBorder("RED")
    print(f"{'ID LOOKUP':^70}")
    printBorder("WHITE")
    searchId = input("Student ID:   ")
    canSearch = False
    for line in studentList:
        if searchId == line[0]:
            print("-"*70)
            print(f"{'Result':^70}")
            print("-"*70)
            print(f"{'ID':^10}|{'Name':^20}|{'Major':^40}")
            print(f"{searchId:^10}|{line[1]:^20}|{line[2]:^40}")
            printBorder("WHITE")
            canSearch = True
    
    if canSearch == False:
        print("-"*70)
        print(f"{'Result':^70}")
        print("-"*70)
        print(f"{'Error: Not Found':^70}")
        printBorder("WHITE")
    printBorder("RED")

# Part 5: update major for a student
def updateMajor():
    readData()
    printBorder("RED")
    print(f"{'MAJOR UPDATE':^70}")
    printBorder("WHITE")
    id = input("Student ID:   ")
    option = input("Computer Science (a),\n" \
    "Data Science and Engineering (b),\n" \
    "Financial Technology (c),\n"\
    "Applied Artificial Intelligence (d), &\n"\
    "Computer Engineering (e)\n"\
    "Major (a/b/c/d/e):   ")
    match option:
        case "a":
            major = "Computer Science"
        case "b":
            major = "Data Science and Engineering"
        case "c":
            major = "Financial Technology"
        case "d":
            major = "Applied Artificial Intelligence"
        case "e":
            major = "Computer Engineering"
        case _:
            print("Error: Unknown Major")
            return
    
    canFind = False   
    
    for i, line in enumerate(studentList):
        if id == line[0]:
            name = line[1]
            studentList[i] = (id,name,major)
            canFind = True
            
            with open(file_path, "r") as file:
                lines = file.readlines()
            lines[i] = ",".join(studentList[i]) + "\n"
            with open(file_path, "w") as file:
                file.writelines(lines)

    if canFind == False:
        print("Error: Unknown ID")
    printBorder("WHITE")
    
splash()

while(True):
    printBorder("RED")

    option = input("STUDENT DATABASE (a),\n" \
        "NEW ENTRY FORM (b),\n" \
        "ID LOOKUP (c),\n"\
        "MAJOR UPDATE (d),\n"\
        "EXIT (e), &\n"\
        "Your Option (a/b/c/d/e):   ")
    match option:
        case "a":
            printData()
        case "b":
            addStudent()
        case "c":
            search()
        case "d":
            updateMajor()
        case _:
            print("Program Ended.")
            printBorder("RED")
            break
            

