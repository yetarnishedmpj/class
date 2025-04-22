class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.stack:
            print("Stack is empty!")
        else:
            print(f"Popped: {self.stack.pop()}")

    def peek(self):
        if not self.stack:
            print("Stack is empty!")
        else:
            print(f"Top Element: {self.stack[-1]}")

    def display(self):
        print("Stack:", self.stack)

def menu():
    s = Stack()
    while True:
        print("\n--- Stack Menu ---")
        print("1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            item = input("Enter item to push: ")
            s.push(item)
        elif choice == '2':
            s.pop()
        elif choice == '3':
            s.peek()
        elif choice == '4':
            s.display()
        elif choice == '5':
            print("Exiting Stack Menu.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
