def has_no_e(word):
    if 'e' not in word:
        return True
    return False

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def uses_only(word, abilable):
    for letter in word:
        if letter not in abilable:
            return False
    return True

def uses_all(word, required):
    return uses_only(required, word)
    
filename = 'words.txt'
count_with_out_e = 0
total_count = 0
with open(filename) as file_obeject:
    lines = file_obeject.readlines()

for line in lines:
    if has_no_e(line.strip()):
        print(line)
        count_with_out_e += 1
    total_count += 1

print(count_with_out_e)
percentage = (count_with_out_e * 100) / total_count
print(f"{percentage:.2f}%")