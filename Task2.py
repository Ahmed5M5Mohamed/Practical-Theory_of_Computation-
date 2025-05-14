def check_an_bn(word):
    memory = []

    stage = "a"

    for letter in word:
        if letter == "a" and stage == "a":
            memory.append("a")
        elif letter == "b":
            if not memory:
                return False
            memory.pop()
            stage = "b"
        else:
            return False

    return not memory

# إدخال المستخدم
user_input = input("Enter the strings separated by space: ")
examples = user_input.split()

for example in examples:
    result = check_an_bn(example)
    if result:
        print(f"The string '{example}' is valid.")
    else:
        print(f"The string '{example}' is not valid.")
