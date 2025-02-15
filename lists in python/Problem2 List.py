Odd = [1, 3, 5, 7, 9]
Even = [2, 4, 6, 8, 10]

combine_list = Odd + Even
print(combine_list)

combine_list = [11, 17, 29] + combine_list
print(combine_list)

print(f"Present element in the list is {len(combine_list)}")
lenth = len(combine_list)
combine_list[lenth-3:] = [100, 200, 300]
print(combine_list)