def create_array(x, y, z, w):
    # def create_array(x, y, z, value):

    return [[[w for _ in range(z)] for _ in range(y)] for _ in range(x)]

array = create_array(3, 4, 5, 11)
# for layer in array:
#     for row in layer:
#         print(row)
#     print()
print(array)
