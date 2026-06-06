# Four experiments on the Streamlit app.
#
# TIP: commit your working version to git first. Then experiment freely
# and `git reset --hard` to roll back when you're done.
#
# --- Experiment 1: WIDGET ORDER MATTERS ---
# Move `st.text_input(...)` ABOVE the checkbox loop and refresh —
# the input box now appears above the todos instead of below. The
# call order is the visual order.
#
# --- Experiment 2: BASIC MARKDOWN INSIDE st.write() ---
# st.write renders Markdown-flavored text. Wrap a word in `**` for
# bold or `*` for italic:
#       st.write("This app is to increase your **productivity**.")
# Refresh — "productivity" is bold. Use `*productivity*` for italics.
#
# --- Experiment 3: RESPONSIVE LAYOUT ---
# Resize the browser window or open the URL on a phone — Streamlit
# widgets shrink and stack automatically. No extra CSS needed for
# basic responsiveness.
#
# --- Experiment 4: MULTI-PAGE APPS ---
# Create a `pages/` folder next to web.py (the name MUST be `pages`).
# Each .py file inside becomes a new page in the auto-generated
# sidebar. See pages/about.py for an example.

import functions
import streamlit as st


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your **productivity**.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
