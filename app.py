import json
import uuid
from datetime import datetime
from pathlib import Path

import streamlit as st

DATA_FILE = Path(__file__).parent / "data" / "todos.json"


def load_todos():
    try:
        if DATA_FILE.exists():
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except (json.JSONDecodeError, OSError):
        pass
    return []


def save_todos(todos):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def add_todo(text):
    todos = st.session_state.todos
    todos.append(
        {
            "id": uuid.uuid4().hex,
            "text": text.strip(),
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
    )
    save_todos(todos)


def toggle_todo(todo_id):
    for todo in st.session_state.todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
            break
    save_todos(st.session_state.todos)


def remove_todo(todo_id):
    st.session_state.todos = [t for t in st.session_state.todos if t["id"] != todo_id]
    save_todos(st.session_state.todos)


st.set_page_config(page_title="待办清单", page_icon=":ballot_box_with_check:", layout="centered")

if "todos" not in st.session_state:
    st.session_state.todos = load_todos()

st.title("我的待办清单")
st.caption("一个用 Python + Streamlit 做的小应用，数据保存在本地 JSON 文件中")

with st.form("add_form", clear_on_submit=True):
    new_task = st.text_input(
        "新任务",
        placeholder="输入要做的事情，回车或点按钮添加",
        label_visibility="collapsed",
    )
    submitted = st.form_submit_button("添加任务", type="primary")
    if submitted and new_task.strip():
        add_todo(new_task)
        st.rerun()

todos = st.session_state.todos
total = len(todos)
done_count = sum(1 for t in todos if t["done"])
remaining = total - done_count

col1, col2, col3 = st.columns(3)
col1.metric("全部任务", total)
col2.metric("已完成", done_count)
col3.metric("待完成", remaining)

st.divider()

if not todos:
    st.info("还没有任务，在上面添加一个吧。")
else:
    st.subheader("任务列表")
    for todo in todos:
        c1, c2 = st.columns([8, 1])
        with c1:
            checked = st.checkbox(
                todo["text"],
                value=todo["done"],
                key=f"chk_{todo['id']}",
            )
            if checked != todo["done"]:
                toggle_todo(todo["id"])
                st.rerun()
            if todo["done"]:
                st.caption(f"已完成 · 创建于 {todo['created_at']}")
        with c2:
            if st.button("删除", key=f"del_{todo['id']}"):
                remove_todo(todo["id"])
                st.rerun()

st.divider()
st.caption("数据保存在 data/todos.json · 用 Git 提交后即可推送到 GitHub")
