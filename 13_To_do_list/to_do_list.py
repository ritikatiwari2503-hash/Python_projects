tasks = []

# Added a while loop to keep the program running
while True:
    print("\n1. ADD TASKS")
    print("2. VIEW TASK")
    print("3. REMOVE TASK")
    print("4. QUIT")

    choice = input("ENTER UR CHOICE HEREE ! ")

    if choice == "1":
        # Changed the variable name from tasks to new_task to avoid overwriting the list
        new_task = input("what's your task? please enter it! ")
        tasks.append(new_task)
        print("Oh Wow! ur task is just added!!")

    elif choice == "2":
        if not tasks:
            print("Your to-do list is empty!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        task_to_remove = input("Enter the task you want to remove: ")
        # Added a safety check to prevent errors if the task doesn't exist
        if task_to_remove in tasks:
            tasks.remove(task_to_remove)
            print("Task removed!")
        else:
            print("Task not found in your list.")

    elif choice == "4":
        print("Goodbye!")
        break  # Exits the loop and ends the program

    else:
        print("Invalid choice! Please choose 1, 2, 3, or 4.")
