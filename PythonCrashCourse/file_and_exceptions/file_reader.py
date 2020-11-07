file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    # for line in file_object:
    #     print(line.rstrip())

    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())