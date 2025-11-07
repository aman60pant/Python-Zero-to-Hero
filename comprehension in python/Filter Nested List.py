given_list = [[1,2,3],[4,5,6],[7,8,9]]

even_list = [x for row in given_list for x in row if x % 2 == 0]

print(even_list)