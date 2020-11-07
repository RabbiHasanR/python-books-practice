cafe = bytes('café', encoding='utf_8')
print(cafe)
print(len(cafe))
print(cafe[0])
print(cafe[:4])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-3:])