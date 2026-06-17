todo_list=[
    'todo-1',
    'todo-2',
    'todo-3',
]


print('Current TODOs:')
print(todo_list)

def addTodo(new_todo):
    todo_list.append(new_todo)

addTodo("blabla")
addTodo("blabla2")
print(todo_list)
