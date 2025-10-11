cup_size = input("Enter the size of cup you want: ").lower()
cup_quantity = int(input("Enter the no of cups you want: "))

if cup_size == "small" or cup_size == "medium" or cup_size == "large":
    if cup_size == "small":
        bill = cup_quantity*10
    elif cup_size == "medium":
        bill = cup_quantity*15
    elif cup_size == "large":
        bill = cup_quantity*20
    print(f"Perfect your bill for {cup_quantity} {cup_size} cups is: {bill}")
else:
    print("Enter a valid cup size!")

# 10 15 20