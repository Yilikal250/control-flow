age = 0

while age < 18:
  age = int(input("Enter your age (must be 18 or older): "))


task = input("Enter your task:")
Priority = input("(high/medium/low)")
time_bound = input("Is it time-bound? (yes/no):")
match Priority:
    case "low":
        PriorityMsg = "is a low priority task.Consider completing it when you have free time. "
    case "high":
        PriorityMsg = "is a high priority task that requires immediate attention today!"
    case "medium": 
        PriorityMsg = "is a high medium task"
if time_bound == "yes":
   Reminder = "Reminder: 'Finish project report' is a high priority task that requires immediate attention today!"
else:
   Reminder = "Note: 'Read a book' is a low priority task. Consider completing it when you have free time." 
    
   
            