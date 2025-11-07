Nested_list = [[10, 15, 20], [25, 30, 35], [40, 45, 50]]

result = {x for row in Nested_list for x in row if x > 20 and x < 45}

print(result)