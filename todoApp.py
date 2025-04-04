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
Option type the Number for :
"""
def displayList():
  print("+----------------+")
  print("    Todo List :   ")
  print("+----------------+")

  for index,list in enumerate(todoList):
    print(index,list)


def addTask():

  task = input("Enter your Task :  ")
  print("---------------------------------->Processing")
  todoList.append(task)

  print(f"Task : {task} was adding todo list")

  displayList()

def editTask():

  print("---------------------------------->Processing")

  if(len(todoList) ==0):

    print("TodoList is Empty")

  else:

    displayList()

    findTask = int(input("Edit Mode | Type the index's task # : "))
    newTask = input("Enter new Task to be replace for : ")

    todoList.remove(todoList[findTask])
    todoList.insert(findTask,newTask)

    displayList()

def removedTask():
  print("Removed")


def Menu():
  while True:
    print(menu)
    op = int(input())
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
