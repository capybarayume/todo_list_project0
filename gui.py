import FreeSimpleGUI as sq
import function
import time
import os 

if not os.path.exists("todos_stuff.txt"):
    with open("todos_stuff.txt", "r") as file:
        pass
    
sq.theme("DarkTeal1")

clock=sq.Text('',key="clock")
label=sq.Text("Type in a TO-DO: ")
input_box=sq.InputText(tooltip="Enter-todo",key="todo")


#change image file location according to your own location
add_button=sq.Button(size=10,image_source="/Users/user/Desktop/todo_list_project0/image/add.png",tooltip="Add todo",key="Add")


list_box=sq.Listbox(values=function.get_todo(),key="todo-list",enable_events=True,size=[45,10])
edit_button=sq.Button("Edit")
complete_button=sq.Button("Complete")

layout=[[clock],[label],[input_box,add_button],[list_box,edit_button,complete_button]]

windows=sq.Window("My TODO LIST", layout=layout,font=('Helvetica', 20))

while True:
    event, values=windows.read(timeout=200)
    if windows.was_closed():
        break

    windows["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            Mytodos=function.get_todo()
            new_todo=values["todo"]+"\n"
            Mytodos.append(new_todo)
            function.write_todos(Mytodos)
            windows["todo-list"].update(values=Mytodos)
        case "Edit":
            try:
                old_todo=values["todo-list"][0]
                new_todo=values["todo"].replace("\n","")

                Mytodos=function.get_todo()
                todo_index_to_edit=Mytodos.index(old_todo)
                Mytodos[todo_index_to_edit]=new_todo+"\n"
                function.write_todos(Mytodos)
                windows["todo-list"].update(values=Mytodos)
            except:
                sq.popup("Please select the items first!",font=('Helvetica', 20))
        case "todo-list":
            windows["todo"].update(value=values["todo-list"][0])
        case "Complete":
            try:
                todo_to_complete=values["todo-list"][0]
                Mytodos=function.get_todo()
                Mytodos.remove(todo_to_complete)
                function.write_todos(Mytodos)
                windows["todo-list"].update(values=Mytodos)
                windows["todo"].update(value="")
            except:
                sq.popup("Please select the items first!",font=('Helvetica', 20))
        case sq.WIN_CLOSED:
            break

windows.close()