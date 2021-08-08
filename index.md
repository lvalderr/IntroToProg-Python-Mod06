# Welcome to Python Functions

#### Luis Valderrama
#### 08/08/2021
#### IT FDN 110 A
#### Module 06
You can view the repository for this assignment in [Intro to Prog Python Mod06](https://github.com/lvalderr/IntroToProg-Python-Mod06) 

## Intro
During the sixth module, I learned the concepts of working with Functions. This document covers the steps to create a script named, _Assignment06_Starter.py_ (Python script), designed to prompt the user to select from a six-option menu and execute the program based on the selection. The six options are 1) Display current tasks, 2) Add a new task, 3) Remove an existing task, 4) Save data to file, 5) Reload data from file, and 6) Exit program. The script is designed to run in PyCharm and Command Prompt, applying concepts learned throughout this module. The following steps were taken to create the Python Script using PyCharm as the Integrated Development Environment (IDE).

## 1.0	Assignment06_Starter.py Program Set UP
In this section we look at the initial set up of the program script.

### 1.1.	Script Header and Objective
As mentioned in prior documents, the first part of the script outlines not only the title, description, date, and change log. But it also provides the reader with a high-level objective of the script and what it is designed to do. (Figure 1.1)

```markdown
# -------------------------------------------------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class, When the program starts, load each "row" of data in "ToDoToDoList.txt" into a python Dictionary. Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# LValderrama,7.31.2021,Created started script
# LValderrama, 8.07.2021, Modified writing to file, print from list option 4 and 1
# LValderrama, 8.07.2021, Modified remove from list option 3
# -------------------------------------------------------------------------------------------------------------------- #

# Objective:
# The Assignment06.py script is designed to:
# 1. Present a menu of choices for the user to select from.
#       1) Display current data
#       2) Add a new Task
#       3) Remove an existing Task
#       4) Save Data to File
#       5) Reload Data from File
#       6) Exit Program
# 2. Execute the program based on the choice made by the user
```
**Figure 1.1: Script Header and Objective**

### 1.2.	Pseudo-Code
Before developing the script, the steps are outlined in the form of Pseudo-Code (Figure 1.2) to help translate the objective into the programing code and develop a usable program. In this example, there are 4 core steps that may expand into sub-steps as the script develops.

```markdown
# Data --------------------------------------------------------------------------------------------------------------- #
# Declare variables and constants
# Processing Data ---------------------------------------------------------------------------------------------------- #
# Presentation, IO: Input and Output --------------------------------------------------------------------------------- #
# Main Body of the Script -------------------------------------------------------------------------------------------- #
# Step 1 - When the program starts, load data from ToDoFile.txt
# Step 2 - Display a menu of choices to the user
# Step 3 Display menu of options
# Step 4 Process user's menu choice
```
**Figure 1.2: Pseudo-Code**

### 1.3.	Declaring Variables and Constants
As best practice, the variables and constants are declared before inserting the codes. (Figure 1.3)

```markdown
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions
```
**Figure 1.3: Declaring Variables and Constants**

### 1.4.	Class Processor
This assignment uses four processing functions as outlined below in (Figure 1.4). Each function will be used for a specific process in the Menu of Options and will be called based upon the user’s input. I set up a Class Processor to group the functions, variables and constants using @staticmethod to define the utility methods or group logically related functions into the class. These functions are intended to process the data based on the user’s input. Then, I insert the variables, parameters for each function.

Note: each function will be examined in more detail as we start looking at section 2.0 Menu of Options. 

![Figure 1 4 Class Processor](https://user-images.githubusercontent.com/83881803/128637803-28666b4f-33d6-450d-9607-e30fb152b4ef.png)

**Figure 1.4: Class Processor**

### 1.5.	Class IO (Input/Outputs)
This assignment uses six additional functions as outlined below in (Figure 1.5). Each function will be used for a specific process in the Menu of Options and will be called based on the user’s input. A Class IO (input/output) is set up to group the functions, variables and constants using @staticmethod. These functions are intended to take input from the user and display prompts and results. Then, I insert the variables for each function.

Note: each function will be examined in more detail as we start looking at section 2.0 Menu of Options. 

![Figure 1 5 Class IO](https://user-images.githubusercontent.com/83881803/128638005-78a80a83-2cde-4fc6-ae7c-f5f519d70aef.png)

**Figure 1.5: Class IO (Inputs/Outputs)**

### 1.6.	Loading Data from Text File to the Table
When the program starts it opens the ToDoList.txt and loads the two-column content into a list held in a table named lstTable as shown in (Figure 1.6.a).

The function is defined using def followed by the name of the function, in this case **read_data_from_file** and the variable given is **file_name** which represents the text file ToDoList.txt where the list of tasks is saved. The parameters are entered as well as a return which is this example is the lstTable. The actual function code is entered to open the .txt file, retrieve the data, and place it in the lstTable in the form of append. The .txt file is then closed, and a return will display the items in the lstTable.

```markdown
@staticmethod
def read_data_from_file(file_name):
    """
    Reads data from a file into a list of dictionary rows

    :param file_name: (string) strFileName = ToDoFile.txt
    :return: (list) dictionary rows
    """
    lstTable = []
    objFile = open(file_name, "r")
    for row in objFile:
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0].strip(), "Priority": lstRow[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
    return lstTable
```
**Figure 1.6.a: Class Processor. read_data_from_file**

The **Class Processor. read_data_from_file** function is called outside of the While loop that will contain the Menu of Options. (Figure 1.6.b.). Additionally, the variable strFileName represents the ToDoFile.txt where the information is held (Figure 1.6.c). 

```markdown
# Step 1 - When the program starts, load data from ToDoFile.txt
lstTable = Processor.read_data_from_file(strFileName)
```
**Figure 1.6.b: Calling the function. read_data_from_file**

![Figure 1 6c View of ToDoFile](https://user-images.githubusercontent.com/83881803/128638020-34c0e98e-0a7b-41fa-83a1-da52eecf8a43.png)

**Figure 1.6.c: View of ToDoFile.txt content**

## 2.0	Menu of Options Set Up
In this assignment, the program initiates with a menu that offers six choices. 1) Show current tasks, 2) Add a new task, 3) Remove an existing task, 4) Save data to file, 5) Reload data from file, and 6) Exit program. The menu is defined in the **Class IO** (input/output) as **print_menu_tasks**, without variables. (Figure 2.0.a) 

```markdown
@staticmethod
def print_menu_Tasks():
    """ Display a menu of choices to the user

    :return: Nothing
    """
    print('''
    Menu of Options
    1) Display current tasks
    2) Add a new task
    3) Remove an existing task
    4) Save data to file
    5) Reload data from file
    6) Exit program
    ''')
    print()  # Adding extra line
```
**Figure 2.0.a: Class IO. print_menu_tasks**

An **input()** function is defined as **IO.input_menu_choice()** in the form of a string. This input is established to get a choice from 1 – 6 from the user (Figure 2.0.b). The choice will then activate the corresponding function and the program will process the data accordingly.

```markdown
@staticmethod
def input_menu_choice():
    """ Gets the menu choice from a user

    :return: string
    """
    choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
    print()  # Add an extra line for looks
    return choice
```
**Figure 2.0.b: Class IO. input_menu_choice**

Another **input()** function is defined as **IO.input_press_to_continue**. This input is established for the sole purpose of pausing the program before advancing to the next step and allow the user to control when the program should continue. (Figure 2.0.c.)

```markdown
@staticmethod
def input_press_to_continue(optional_message=''):
    """ Pause program and show a message before continuing

    :param optional_message: An optional message to display
    :return: Nothing
    """
    print(optional_message)
    input('Press the [Enter] key to continue.')
return choice
```
**Figure 2.0.c: Class IO. input_press_to_continue**

The functions previously described are called at the beginning of the **while(True)** loop. The program will continue to loop through until a break is reached. (Figure 2.0.d.)

```markdown
while (True):
# Step 3 Display menu of options
    IO.print_menu_Tasks()
    strChoice = IO.input_menu_choice()
```
**Figure 2.0.d: Calling the function**

Displayed below in (Figure2.0.e.) is the program as it starts running in PyCharm. The user can also double click on the .py file itself and the program will start running in Command Prompt by default. The image below shows the Menu of Options 1 - 6 which is the result of calling the function **IO.print_menu_choice()** while the **input()** identified as “Which option would you like to perform? [1 to 6] is the result of calling the function **strChoice = IO.input_menu_choice()**.

![Figure 2 0 e Menu of Options](https://user-images.githubusercontent.com/83881803/128638030-10bd3446-e435-4757-8923-0d057064f990.png)

**Figure 2.0.e: Menu of Options shown in PyCharm and Command Prompt as the program starts running**

### 2.1.	Display Current Tasks (Menu Option 1)
In this section we examine the programing to execute option 1 from the Menu of Options (Figure 2.1.a)

There is no processing function. However, there is an Input/Output function that is defined as **print_current_tasks_in_list** with the variable, **list_of_rows**, which is used to hold the data in the form of a two-column list. The function prints the data in the form of a list of tasks and priorities. The **print()** is set up to “unpack” the data. 

```markdown
@staticmethod
def print_current_tasks_in_list(list_of_rows):
    """ Shows the current Tasks in the list of dictionaries rows

    :param list_of_rows: (list) split data into list
    :return: Nothing
    """
    print("******* The current items ToDo are: *******")
    for row in lstTable:  # Displaying rows below in the form of a vertical list
        print(row["Task"] + ',' + row["Priority"])  # Unpacking
    print("*******************************************")
    print()  # Add an extra line for looks
```
**Figure 2.1.a.: Class IO.print_current_tasks_in_lists (Menu Option 1)**

The function previously described is called within the **while(True)** loop when the user enters “1” in the input_menu_choice as prompted by the message “Which option would you like to perform? [1 – 6]”. The next function called is **input_press_to_continue()** which is intended to pause the program until the user presses Enter to proceed. (Figure 2.1.b.)

```markdown
# Step 4 Process user's menu choice
    if strChoice.strip() == '1':
        IO.print_current_tasks_in_list(lstTable)
        IO.input_press_to_continue()
        continue
```
**Figure 2.1.b.: Calling the function (Menu Option 1)**

Displayed below in (Figure2.1.c.) is the program as it runs in PyCharm and in Command Prompt after the functions are called as previously mentioned.

![Figure 2 1 c Results from Menu of Option 1](https://user-images.githubusercontent.com/83881803/128638040-1ff8ab24-cee3-4370-8b57-287de0a05d08.png)

**Figure 2.1.c.: Results from Menu Option 1 displayed in PyCharm and Command Prompt**

### 2.2.	Add a New Task (Menu Option 2)

In this section we examine the programing to execute option 2 from the Menu of Options (Figure 2.2.a.)

The processing function is defined as **add_data_to_list** with the variables, **list_of_rows, task, priority** in the form of strings. The function itself takes the task and priority entered by the user and appends the **lstTable** that holds the data with the new items. The function **returns** a value in the form of an expression immediately after the user enters the new data. The value is the list of tasks and priorities.

```markdown
@staticmethod
def add_data_to_list(list_of_rows, task, priority):
    """ Adds task and priorities to list

    :type list_of_rows:
    :param list_of_rows: (list) you want filled with file data
    :param task: (string) to do item
    :param priority: (string) the priority of the task
    :return: (list) of task and priorities
    """
    dicRow = {"Task": str(task), "Priority": str(priority)}
    list_of_rows.append(dicRow)
    return list_of_rows, 'Success'
```
**Figure 2.2.a.: Class Processor.add_data_from_file (Menu Option 2)**

The Input/Output function is defined as **input_new_task_and_priority** without parameters. The function gets two inputs, Task and Priority from the user, and it returns the entries made by the user. (Figure 2.2.b)

```markdown
@staticmethod
def input_new_task_and_priority():
    """ Adds new task and priority entered by the user
    :return: (string) Task and its corresponding priority
    """
    task = str(input("Enter a New Task: ")).strip()
    priority = str(input("Enter Priority (Top, Med, Low): ")).strip()
    print()
    return task, priority
```
**Figure 2.2.b: IO.input_new_task_and_priority (Menu Option 2)**

The functions previously described are called within the **while(True)** loop when the user enters “2” in the input_menu_choice as prompted by the message “Which option would you like to perform? [1 – 6]”. The next function called is **IO.input_new_task_and_priority()** which gets the data entered by the user, then the next function called is **Processor.add_data_to_list** which appends the lstTable with the new task and its priority. The program calls **IO.print_current_tasks_in_list** function which now displays the list updated with the new task and priority entered by the user. The last function called is **IO.input_press_to_continue()** in order to pause the program until the user presses Enter to proceed. (Figure 2.2.c.)

```markdown
elif strChoice == '2':
    tplData = IO.input_new_task_and_priority()
    Processor.add_data_to_list(lstTable, tplData[0], tplData[1])
    IO.print_current_tasks_in_list(lstTable)
    IO.input_press_to_continue()
    continue
```
**Figure 2.2.c.: Calling the function (Menu Option 2)**

Displayed below in (Figure2.2.d.) is the program as it runs in PyCharm and in Command Prompt after the functions are called as previously mentioned. 

![Figure 2 2 d Results from Menu of Options 2](https://user-images.githubusercontent.com/83881803/128638046-f5c08b50-090e-4862-8ec3-e8e25881daef.png)

**Figure 2.2.d.: Results from Menu Option 2 displayed in PyCharm and Command Prompt**

### 2.3.	Remove an Existing Task (Menu Option 3) 
In this section we examine the programing to execute option 3 from the Menu of Options. (Figure 2.3.a.)

The processing function is defined as **remove_data_from_list** with the variable, **list_of_rows**, in the form of string. The function itself gets an input from the user and compares to the list of tasks and priorities, **lstTable**. If the input is matched with an item in the list, then the function removes the task and priority from the list and displays a message confirming the item has been removed. If the input is not matched to the list, then the program prints a message indicating the item is not found. 

```markdown
@staticmethod
def remove_data_from_list(list_of_rows):
    """ Removes tasks from list

    :param list_of_rows: (list) you want filled with file data
    :return" (List) of tasks removed
    """
    while len(lstTable) > 0:
        print("Current Task list:\n", "\n".join([f"\t{item['Task']}" for item in lstTable]))  # Display current data
        term = input("Enter the Task you want to delete or type 'exit' to return to Menu of Options: ")
        if term.lower() == "exit":
            break
        for task in lstTable:
            if term in task["Task"]:  # If the task entered by the user matches the name in the list then proceed
                print(f"Removing {task['Task']}...")  # Print a message "item found" and processing removal
                list_of_rows.remove(task)  # The item is removed from the table
                break
        else:
            print(f"Task not found in list: {term}")  # Displays message indicating the task was not found!
```
**Figure 2.3.a.: Class Processor.remove_data_from_list (Menu Option 3)**

The Input/Output function is defined as **remove_data_from_list** with parameter term (Figure 2.3.b). The function gets one input from the user, and the processing function previously mentioned will run through the matching, and removal process. 

```markdown
@staticmethod
def remove_data_from_list(term):
    """ Removes tasks and priorities entered by the user

    :term: (string) this is the item the user wants to remove
    :return: (string) Task and its corresponding priority
    """
    term: input("Confirm the Task you want to delete or type 'exit' to return to Menu of Options: ")
```
**Figure 2.3.b.: IO.remove_data_from_list (Menu Option 3)**

The functions previously described are called within the **while(True)** loop when the user enters “3” in the **Processor.remove_data_to_list** which removes item entered by the user from the **lstTable**. The last function called is **IO.input_press_to_continue()** in order to pause the program until the user presses Enter to proceed. (Figure 2.3.c.)

```markdown
elif strChoice == '3':
    Processor.remove_data_from_list(lstTable)
    IO.input_press_to_continue()
    continue
```
**Figure 2.3.c.: Calling the function (Menu Option 3)**

Displayed below in (Figure2.3.d.) is the program as it runs in PyCharm and in Command Prompt after the functions are called as previously mentioned. 

![Figure 2 3 d Results from Menu of Options](https://user-images.githubusercontent.com/83881803/128638064-c6a962ef-bd6d-402e-b0f9-a8c154f55685.png)

**Figure 2.3.d.: Results from Menu Option 3 displayed in PyCharm and Command Prompt**

### 2.4.	Saving Data in .txt File (Menu Option 4)

In this section we examine the programing to execute option 4 from the Menu of Options (Figure 2.4.a)

The processing function is defined as **write_data_from_list** with the variable, **file_name** and **list_of_rows** in the form of string. The function itself opens the ToDoFile.txt and saves the data from the tasks and priorities list. The program then closes the .txt file and prints the message with confirmation the data has been saved in the ToDoFile.txt. 

```markdown
@staticmethod
def write_data_from_list(file_name, list_of_rows):
    """

    :param file_name: (string) strFileName = ToDoFile.txt
    :param list_of_rows: (list) you want filled with file data
    """
    objFile = open(file_name, 'w')
    for row in list_of_rows:
        objFile.write(row["Task"] + "," + row["Priority"] + "\n")
    objFile.close()
    print('\nYour data is saved to', file_name)
```
**Figure 2.4.a: Class Processor.write_data_from_list (Option 4)**

The function previously described is called within the while(True) loop when the user enters “4” in the **Processor.write_data_from_list**. The program also calls the **IO.print_current_tasks_in_list** function which displays the current tasks and priorities. The last function called is **IO.input_press_to_continue()** in order to pause the program until the user presses Enter to proceed. (Figure 2.4.b.)

```markdown
elif strChoice == '4':
    print('\n Would you like to save your data?')
    strSaveToFileInput = input("Enter 'y' or 'n': ")
    if (strSaveToFileInput == 'n'):
        print('Data not saved!')
    if (strSaveToFileInput == 'y'):
        Processor.write_data_from_list(strFileName, lstTable)
        print('\nYour data is saved to', strFileName)
        IO.print_current_tasks_in_list(lstTable)
        IO.input_press_to_continue()
    continue
```
**Figure 2.4.b: Calling the function (Option 4)**

Displayed below in (Figure2.4.c.) is the program as it runs in PyCharm and in Command Prompt after the functions are called as previously mentioned. 

![Figure 2 4 c View of Option 4](https://user-images.githubusercontent.com/83881803/128638069-5dfc83a9-398c-44ce-82e6-62b16855f1d5.png)

**Figure 2.4.c: View of the Option 4 as it runs in PyCharm and Command Prompt**

To view the saved data simply open the ToDoFile.txt. (Figure 2.4.d)

![Figure 2 4 d View of the ToDoFile](https://user-images.githubusercontent.com/83881803/128638082-d5a533c8-dc69-4f30-80dd-b7984542d91a.png)

**Figure 2.4.d: View of the ToDoFile.txt content**

### 2.5.	Reload Data from File (Menu Option 5)
In this section we examine the programing to execute option 5 from the Menu of Options (Figure 2.5.a)

When the user enters 5 in the **IO.input_menu_choice()** the program calls the function **lstTable = Processor.read_data_from_file(strFile)** to reload the information from the ToDoFile.txt into the list table. The program then displays the data by way of calling the function **IO.print_current_tasks_in_list(lstTable)**. The last function called is **IO.input_press_to_continue()** in order to pause the program until the user presses Enter to proceed. 

```markdown
elif strChoice == '5':
    print("This action will overwrite all unsaved tasks!")
    strAcceptOrDecline = input("Update data without saving? type 'y' or 'n' ")
    if strAcceptOrDecline.lower() == 'y':
        lstTable.clear()
        lstTable = Processor.read_data_from_file(strFileName)
        IO.print_current_tasks_in_list(lstTable)
    else:
        input("File no updated. Press Enter to go back to Menu of Options")
        IO.print_menu_Tasks()
    continue
```
**Figure 2.5.a.: Calling the function (Option 5)**

Displayed below in (Figure2.5.b.) is the program as it runs in PyCharm and in Command Prompt after the functions are called as previously mentioned.

![Figure 2 5 b Display Option 5](https://user-images.githubusercontent.com/83881803/128638085-31fadfd8-093b-4d5d-a365-9740eb726280.png)

**Figure 2.5.b.: Display Option 5 as it runs in PyCharm and Command Prompt**

### 2.6.	Exit The Program (Menu Option 6)
In this section we examine the programing to execute option 6 from the Menu of Options (Figure 2.6.a)

There is no processing or **IO** functions associated with option 6. The program simply ends when the user enters 6 and the break in the **While(True)** loop is called.

Figure 2.6.a: Calling the function (Option 6)

Displayed below in (Figure2.6.b.) is the program as it runs in PyCharm and in Command Prompt after the loop break is called when the user enters 6.

![Figure 2 6 b Display Options 6](https://user-images.githubusercontent.com/83881803/128638095-bcb9e3a8-8371-423f-891b-589acdb5ca9a.png)

Figure 2.6.b: Display Option 6 as it runs in PyCharm and Command Prompt

## Summary
To recap, the sixth module introduced me to working with Functions. The example created for this assignment, _Assignment06_Starter.py_ is the result of steps taken to develop a script designed to prompt the user to select from a six-option menu and execute the program based on the selection. The program successfully allows the user to enter, display, delete, reload, and save the data in a .txt file. The program runs in PyCharm and Command Prompt and considers the concepts and best practices learned in this module.


### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
