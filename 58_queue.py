# Initialize an empty list to represent the queue
queue = []

# Function to push (enqueue) an element to the queue
def push(element):
    queue.append(element)
    print(f"Pushed: {element}")

# Function to pop (dequeue) an element from the queue
def pop():
    if not is_empty():
        element = queue.pop(0)  # Remove the first element
        print(f"Popped: {element}")
        return element
    else:
        print("Queue is empty!")
        return None

# Function to check if the queue is empty
def is_empty():
    return len(queue) == 0

# Function to get the size of the queue
def size():
    return len(queue)

# Main loop to take user input
while True:
    command = input("Enter command (push <value>, pop, size, exit): ").strip().lower()
    
    if command.startswith("push"):
        try:
            # Extract the value to push
            _, value = command.split()
            push(value)
        except ValueError:
            print("Invalid command. Use 'push <value>' to add an element.")
    
    elif command == "pop":
        pop()
    
    elif command == "size":
        print(f"Queue size: {size()}")
    
    elif command == "exit":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid command. Please use 'push <value>', 'pop', 'size', or 'exit'.")