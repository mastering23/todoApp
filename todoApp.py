pageLimit = 10
op = ""
task = ""
todoList = ["banana", "apple", "banana", "apple", "banana", "apple", "banana", "apple", "banana", "mango", "lime",
            "grape", "apple", "orange", "cherry", "banana", "apple", "banana", "apple", "banana", "apple"]

menu = """
+-----------------------+
  Todo List 📋 | Menu
+-----------------------+
1) add
2) edit
3) removed
4) view
5) Setting
00) Exit
Option type the Number for :
"""
def appSetting():
  print("change the page Limitation")
  setValue = input("Type the limitation : ")
  return setValue

def view(pageLimit):
  page = 0
  sizeData = (len(todoList))
  pages = pageLimit / sizeData
  start = 0 - pageLimit
  while (True):
    op = input("N for Next | B for Back | Q for QUit : ").lower()
    if (op == "q"):
      print("exiting view....")
      break
    elif (op == "n"):
      page += 1
      start += pageLimit
      displayItemsByPage(page, pageLimit, sizeData, start)

    elif (op == "b"):
      if( start <= 0 ):
        print("You are already at the beginning of the list")
        continue

      page -= 1
      start -= pageLimit
      displayItemsByPage(page, pageLimit, sizeData, start)



def displayItemsByPage(page, pageLimit, sizeData, start):
  for i in range(start, pageLimit * page):
    if i > sizeData - 1:
      print("No more data after this point....")
      break
    else:
      print(i, ":", todoList[i])


def displayList():
  print("+----------------+")
  print("    Todo List :   ")
  print("+----------------+")

  for index, item in enumerate(todoList):
    print(index, item)


def addTask():
  task = input("Enter your Task :  ")
  print("---------------------------------->Processing")
  todoList.append(task)

  print(f"Task : {task} was adding todo list")

  displayList()


def editTask():
  print("---------------------------------->Processing")

  if (len(todoList) == 0):

    print("TodoList is Empty")

  else:

    displayList()

    findTask = int(input("Edit Mode | Type the index's task # : "))
    newTask = input("Enter new Task to be replace for : ")

    todoList.remove(todoList[findTask])
    todoList.insert(findTask, newTask)

    displayList()


def removedTask():
  if (len(todoList) == 0):

    print("TodoList is Empty")

  else:
    displayList()

    removedTask = int(input("Remove Mode | Type the index's task # : "))
    todoList.remove(todoList[removedTask])

    displayList()


def Menu():
  global pageLimit
  while True:
    print(menu)
    op = int(input())
    if op == 1:
      addTask()
    elif op == 2:
      editTask()
    elif op == 3:
      removedTask()
    elif op == 4:
      view(pageLimit)
    elif op == 5:
      pageLimit = int (appSetting())
    elif op == 00:
      print("exiting")
      break

    else:
      print("Invalid option, please try again")


Menu()
