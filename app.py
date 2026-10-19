from __future__ import annotations

import streamlit as st
import pawpal_system as pawpal
from datetime import datetime

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
    At minimum, your system should:
    - Represent pet care tasks (what needs to happen, date, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

owner = pawpal.Owner(name = owner_name)
owner.add_pet(pawpal.Pet(name=pet_name, pet_type=species))

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

owner.find_pet(pet_name).tasks = [
    pawpal.Task(
        date=task["date"],
        type=task["priority"],
        priority={"low": 1, "medium": 2, "high": 3}[task["priority"]],
        name=task["title"],
    )
    for task in st.session_state.tasks
]

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    task_date = st.datetime_input("Task date")
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    date_value = int(task_date.timestamp())
    st.session_state.tasks.append(
        {"title": task_title, "date": date_value, "priority": priority}
    )
    owner.add_task(
        pet_name,
        date_value,
        priority,
        {"low": 1, "medium": 2, "high": 3}[priority],
        task_title,
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")
selected = []

col2_1, col2_2 = st.columns(2)
with col2_1:
   cutoff_date = st.datetime_input("Cutoff date")
with col2_2:
    if st.button("Generate schedule"):
        pet_tasks = owner.scheduler.GetPetTasks(pet_name)
        cutoff_date_value = int(cutoff_date.timestamp())
        owner.scheduler.UpdateCompletedTask(pet_tasks, int(datetime.now().timestamp()))

        selected = owner.generate_schedule(cutoff_date_value, pet_name)

prev_time = 0
for item in selected:
    if item.date != prev_time:
        st.markdown(f"- {datetime.fromtimestamp(item.date)}: {item.name}")
    else:
        st.markdown(f":red[- {datetime.fromtimestamp(item.date)}: {item.name}]")

    prev_time = item.date