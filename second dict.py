# Dictionary
# NO. 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result_dict = {}
for key in keys:
    for value in values:
        result_dict[key] = value
        values.remove(value)
        break
print(result_dict)


# ********************************
# NO. 2
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys_to_remove = ["name", "salary"]

for i in keys_to_remove:
    sample_dict.pop(i)

print(sample_dict)



