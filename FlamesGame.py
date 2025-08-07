def remove_common_chars(name1, name2):
    list1 = list(name1)
    list2 = list(name2)
    for char in name1:
        if char in list2:
            list1.remove(char)
            list2.remove(char)
    return len(list1 + list2)

def flames_result(count):
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    return flames[0]

# Main program
name1 = input("Enter first name: ").replace(" ", "").lower()
name2 = input("Enter second name: ").replace(" ", "").lower()

count = remove_common_chars(name1, name2)
result = flames_result(count)

print(f"\nRelationship status: {result}")
