tasks = []
choice = ''

def int_and_in_range(value, lower, upper):
	if not str(value).isnumeric():
		return False
	elif int(value) not in range(lower,upper):
		return False
	else:
		return True

def show_list():
	if len(tasks) == 0:
		print("Your to-do list is empty")
	else:
		print("Here's what's on your to-do list:")
	for index, task in enumerate(tasks):
		print(str(index+1) +". "+ task)

while choice != 0:
	choice=int(input("\nWhat would you like to do?\n1. Add a task\n2. View tasks list\n3. Remove a task\n0. Exit\n>> "))
	if choice == 0:
		print("App is now closing, thanks for trying it out.")
	elif choice == 1:
		task = input("Enter a task: ")
		tasks.append(task)
	elif choice == 2:
		show_list()
	elif choice == 3:
		if len(tasks) == 0:
			print("Nothing to remove, your to-do list is empty")
		else:
			index = -1
			while not int_and_in_range(index, 1, len(tasks)+1):
				index = input("Enter number of the task: ")
				if not int_and_in_range(index, 1, len(tasks)+1):
					print("Invalid number, try again.")
				else:
					print("Removed task: "+ tasks[int(index)-1])
					del tasks[int(index)-1]
					break
	else:
		print("Error: Enter a valid choice.")