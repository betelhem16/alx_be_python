while True:

    task = input("Enter your task: ")


    priority = input("Priority (high/medium/low): ").lower()

   
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Use match-case for priority handling
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a high priority task. Try to complete it soon.")

        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a medium priority task. Plan to address it when possible.")

        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

        case _:
            print("Invalid priority. Please enter high, medium, or low.")

    # Ask if the user wants to input another task
    repeat = input("Do you want to add another task? (yes/no): ").lower()
    if repeat != "yes":
        break
