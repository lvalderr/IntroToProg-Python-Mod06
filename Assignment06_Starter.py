# -------------------------------------------------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# LValderrama, 7.31.2021, Created started script
# LValderrama, 8.07.2021, Modified writing to file, read from file, remove from list
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

# Data --------------------------------------------------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Create ToDoFile.txt ------------------------------------------------------------------------------------------------ #
# objFile = open(strFileName, 'a')
# objFile.close()


# Processing Data ---------------------------------------------------------------------------------------------------- #
class Processor:
    """ Performs Processing Tasks"""
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


# Presentation, IO: Input and Output --------------------------------------------------------------------------------- #
class IO:
    """    Performs Input and Output Tasks    """

    @staticmethod
    def print_menu_tasks():
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

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message: An optional message to display
        :return: Nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

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

    @staticmethod
    def input_new_task_and_priority():
        """ Adds new task and priority entered by the user
        :return: (string) Task and its corresponding priority
        """
        task = str(input("Enter a New Task: ")).strip()
        priority = str(input("Enter Priority (Top, Med, Low): ")).strip()
        print()
        return task, priority

    @staticmethod
    def remove_data_from_list(term):
        """ Removes tasks and priorities entered by the user

        :term: (string) this is the item the user wants to remove
        :return: (string) Task and its corresponding priority
        """
        term: input("Confirm the Task you want to delete or type 'exit' to return to Menu of Options: ")


# Main Body of the Script -------------------------------------------------------------------------------------------- #
# Step 1 - When the program starts, load data from ToDoFile.txt
lstTable = Processor.read_data_from_file(strFileName)

# Step 2 - Display a menu of choices to the user
while (True):
# Step 3 Display menu of options
    IO.print_menu_tasks()
    strChoice = IO.input_menu_choice()

# Step 4 Process user's menu choice
    if strChoice.strip() == '1':
        IO.print_current_tasks_in_list(lstTable)
        IO.input_press_to_continue()
        continue

    elif strChoice == '2':
        tplData = IO.input_new_task_and_priority()
        Processor.add_data_to_list(lstTable, tplData[0], tplData[1])
        IO.print_current_tasks_in_list(lstTable)
        IO.input_press_to_continue()
        continue

    elif strChoice == '3':
        Processor.remove_data_from_list(lstTable)
        IO.input_press_to_continue()
        continue

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

    elif strChoice == '5':
        print("This action will overwrite all unsaved tasks!")
        strAcceptOrDecline = input("Update data without saving? type 'y' or 'n' ")
        if strAcceptOrDecline.lower() == 'y':
            lstTable.clear()
            lstTable = Processor.read_data_from_file(strFileName)
            IO.print_current_tasks_in_list(lstTable)
        else:
            input("File no updated. Press Enter to go back to Menu of Options")
            IO.print_menu_tasks()
        continue

    elif strChoice == '6':
        print("Goodbye!")
        EndProgram = input('\n(Press Enter to End Program)')
        break
