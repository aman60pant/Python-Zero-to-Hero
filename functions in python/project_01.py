def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai!")

print("Enter \"Quit\" to exit.")
try:
    while True:
        name = input("Enter your name: ").strip().strip('"').strip("'")
        if name.lower() in ('quit', 'q'):
            break
        chai_type = input("Enter your chai type: ").strip().strip('"').strip("'")
        if chai_type.lower() in ('quit', 'q'):
            break
        print_order(name, chai_type)

except KeyboardInterrupt:
    print("\nStopped by user (Ctrl+C)")
