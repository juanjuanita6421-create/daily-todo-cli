import json
from pathlib import Path

TODO_FILE = Path("todos.json")

def load_todos():
    if TODO_FILE.exists():
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2)

def show_todos(todos):
    if not todos:
        print("✅ No pending tasks!")
        return
    for i, todo in enumerate(todos, start=1):
        print(f"{i}. {todo}")

def main():
    todos = load_todos()
    while True:
        print("\n--- Daily To-Do CLI ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                todos.append(task)
                save_todos(todos)
                print("✅ Task added.")
        elif choice == "3":
            show_todos(todos)
            idx = input("Enter task number to remove: ").strip()
            if idx.isdigit() and 0 < int(idx) <= len(todos):
                removed = todos.pop(int(idx) - 1)
                save_todos(todos)
                print(f"❌ Removed: {removed}")
            else:
                print("Invalid number.")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
