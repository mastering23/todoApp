op =""
task = ""
todoList = []

menu ="""
+-----------------------+
  Todo List 📋 | Menu
+-----------------------+
1) add
2) edit
3) removed
00) Exit
Option type the Number for
"""

def addTask():
  print("add")


def editTask():
  print("edit")


def removedTask():
  print("Removed")


def Menu():
  while True:
    print(menu)
    op = int(input(":"))
    if op == 1:
        addTask()
    elif op == 2:
        editTask()
    elif op == 3:
        removedTask()
    elif op == 00 :
      print("exiting")
      break
    else:
      print("Invalid option, please try again")

Menu()
