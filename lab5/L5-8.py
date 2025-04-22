class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty!")
        else:
            print(f"Dequeued: {self.queue.pop(0)}")

    def front(self):
        if not self.queue:
            print("Queue is empty!")
        else:
            print(f"Front Element: {self.queue[0]}")

    def display(self):
        print("Queue:", self.queue)

def menu():
    q = Queue()
    while True:
        print("\n--- Queue Menu ---")
        print("1. Enqueue\n2. Dequeue\n3. Front\n4. Display\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            item = input("Enter item to enqueue: ")
            q.enqueue(item)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.front()
        elif choice == '4':
            q.display()
        elif choice == '5':
            print("Exiting Queue Menu.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
