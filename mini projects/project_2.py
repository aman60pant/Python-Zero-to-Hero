snack = input("Hey! Enter your favourite snac: ").lower()

print(f"user said: {snack}");

if snack == "samosa" or snack == "cookies":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print("Sorry, We only serve cookies or samosa with tea")
    