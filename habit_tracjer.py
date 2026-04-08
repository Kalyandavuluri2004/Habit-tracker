import json
from datetime import datetime
print("Welcome to Personal Habit Tracker!")
try:
    with open("habits.json", "r") as f:
        habits = json.load(f)
except:
    habits = {}
while True:
    print("\n--- Habit Tracker Menu ---")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit Done")
    print("4. Delete Habit")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter habit name: ")
        goal = int(input("Enter goal (days): "))
        if name in habits:
            print("Habit already exists!")
        else:
            habits[name] = {
                "streak": 0,
                "goal": goal,
                "last_done": ""
            }
            print("Habit added")
            with open("habits.json", "w") as f:
                json.dump(habits, f)
    elif choice == "2":
        if not habits:
            print("No habits found")
        else:
            for h in habits:
                print(h, "→", habits[h]["streak"], "/", habits[h]["goal"])
    elif choice == "3":
        name = input("Enter habit name: ")
        if name in habits:
            today = str(datetime.now().date())
            if habits[name]["last_done"] == today:
                print("Already completed today!")
            else:
                habits[name]["streak"] += 1
                habits[name]["last_done"] = today
                print("Habit updated")
                with open("habits.json", "w") as f:
                    json.dump(habits, f)
        else:
            print("Habit not found")
    elif choice == "4":
        name = input("Enter habit name: ")
        if name in habits:
            del habits[name]
            print("Habit deleted")
            with open("habits.json", "w") as f:
                json.dump(habits, f)
        else:
            print("Habit not found")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
