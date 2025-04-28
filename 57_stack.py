def push(stack, item):
    """Push an item onto the stack."""
    stack.append(item)
    print(f"Pushed: {item}")

def pop(stack):
    """Pop an item from the stack. Returns the item or None if the stack is empty."""
    if not is_empty(stack):
        item = stack.pop()
        print(f"Popped: {item}")
        return item
    else:
        print("Stack is empty. Cannot pop.")
        return None

def is_empty(stack):
    """Check if the stack is empty."""
    return len(stack) == 0

def main():
    stack = []
    
    while True:
        action = input("Enter 'push <value>' to push, 'pop' to pop, or 'exit' to quit: ").strip().lower()
        
        if action.startswith("push"):
            try:
                value = action.split()[1]
                push(stack, value)
            except IndexError:
                print("Please provide a value to push.")
        
        elif action == "pop":
            pop(stack)
        
        elif action == "exit":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid command. Please enter 'push <value>', 'pop', or 'exit'.")

        print(f"Current stack: {stack}")

if __name__ == "__main__":
    main()