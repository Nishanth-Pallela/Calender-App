import streamlit as st
import os
import functions

FILEPATH = 'June_5th.txt'

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass
todos = functions.read_file(FILEPATH)


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todo(todos)


st.title("June 5th, 2023")
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
