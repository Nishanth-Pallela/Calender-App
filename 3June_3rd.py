import streamlit as st
import os
import functions

if not os.path.exists("June_3rd.txt"):
    with open("June_3rd.txt", 'w') as file:
        pass
todos = functions.read_file('June_3rd.txt')


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todo(todos)


st.title("June 3rd, 2023")
st.subheader('Enter any todos or events below')
st.write("The app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label=' ', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')
