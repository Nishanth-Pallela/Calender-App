def read_file(filepath):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def clean(arg):
    new_arg = [i.strip('\n') for i in arg]
    return new_arg


def write_todo(todos, filepath):
    with open(filepath, 'w') as file:
        file.writelines(todos)
