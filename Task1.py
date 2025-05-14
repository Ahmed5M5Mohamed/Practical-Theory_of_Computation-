def check_divisible_by_three_ones(s):
    count = 0
    for ch in s:
        if ch == '1':
            count += 1
        elif ch != '0':
            return False
    return count % 3 == 0

user_input = input("Enter binary strings separated by space: ")

inputs = user_input.split()

for string in inputs:
    if check_divisible_by_three_ones(string):
        print("The string", string, "is accepted.")
    else:
        print("The string", string, "is rejected.")
