dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
res = {}
sort = []


# Create an empty list to store the keys in the desired order
keys = []

# Iterate through the keys in the dictionary and append them to the list in the desired order
for key in dict1:
    if key == 1:
        keys.insert(0, key)
    elif key == 3:
        keys.insert(1, key)
    elif key == 4:
        keys.insert(2, key)
    elif key == 2:
        keys.insert(3, key)
    elif key == 0:
        keys.insert(4, key)

# Use the list of keys to retrieve the values from the dictionary in the desired order
sorted_d = {key: dict1[key] for key in keys}

print(sorted_d) 