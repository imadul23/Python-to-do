import json
file= open("data.json", "r")
x=file.read()
finaldata=json.loads(x)
print(type(finaldata))


def generateID():
    if finaldata:
        # print('my list is not empty')
        last_item_id = finaldata[-1]['id']
        return last_item_id + 1
        # last_item = my_list[-1]
    else:
        return 1
        # print("The list is empty!")

newID=generateID()

print(newID)

# for a in finaldata:
#     print(a)

new_task = {
    "id": newID,
    "title": "Finish Python assignment new",
    "completed": False,
    "created_at": "2026-07-04",
    "due_date": "2026-07-08"
}

finaldata.append(new_task)

print(finaldata)

# with open('data.json', 'w') as data_json:
#     json.dump(finaldata, data_json, indent=4)

write_file= open("data.json", "w")
json.dump(finaldata, write_file, indent=4) 


def sum(x):
    return x + 1

h=int(input())
z=sum(h)
print(z)