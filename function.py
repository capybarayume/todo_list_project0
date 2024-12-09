FILE_PATH="todos_stuff.txt"

def get_todo(filepath=FILE_PATH):
    with open(filepath, "r")as file_local:
        todo_local=file_local.readlines()
    return todo_local

def write_todos(todos_word,filepath=FILE_PATH):
    with open(filepath, "w")as file:
        file.writelines(todos_word)



if __name__=="__main__":
   print("Hello")