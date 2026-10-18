from __future__ import annotations


class Pet:
    def __init__(self, name: str = "", age: int = 0, pet_type: str = ""):
        self.name = name
        self.age = age
        self.pet_type = pet_type


class Task:
    def __init__(self, duration: int = 0, task_type: str = "", priority: int = 0, name: str = ""):
        self.duration = duration
        self.type = task_type
        self.priority = priority
        self.name = name


class Person:
    def __init__(
        self,
        name: str = "",
        age: int = 0,
        email: str = "",
        pets: list[Pet] | None = None,
        tasks: list[Task] | None = None,
    ):
        self.name = name
        self.age = age
        self.email = email
        self.pets = pets if pets is not None else []
        self.tasks = tasks if tasks is not None else []

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> bool:
        if pet in self.pets:
            self.pets.remove(pet)
            return True
        return False

    def find_pet(self, name: str) -> Pet | None:
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

    def FindPet(self, name: str) -> Pet | None:
        return self.find_pet(name)

    def add_task(self, duration: int, task_type: str, priority: int, name: str, pet_name: str) -> bool:
        if any(task.name == name for task in self.tasks):
            return False
        
        if not any(pet.name == pet_name for pet in self.pets):
            return False

        
        self.tasks.append(Task(duration=duration, task_type=task_type, priority=priority, name=name))
        return True

    def AddTask(self, duration: int, type: str, priority: int, name: str, pet_name: str) -> bool:
        return self.add_task(duration, type, priority, name, pet_name)

    def remove_task(self, name: str) -> bool:
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                return True
        return False

    def RemoveTask(self, name: str) -> bool:
        return self.remove_task(name)

    def edit_task(self, name: str, duration: int, priority: int) -> bool:
        for task in self.tasks:
            if task.name == name:
                task.duration = duration
                task.priority = priority
                return True
        return False

    def EditTask(self, name: str, duration: int, priority: int) -> bool:
        return self.edit_task(name, duration, priority)

    def generate_schedule(self, duration: int) -> list[Task]:
        selected_tasks: list[Task] = []
        remaining_time = duration

        for task in sorted(self.tasks, key=lambda item: item.priority, reverse=True):
            if task.duration <= remaining_time:
                selected_tasks.append(task)
                remaining_time -= task.duration

        return selected_tasks

    def GenerateSchedule(self, duration: int):
        return self.generate_schedule(duration)


import streamlit as st

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
- Represent pet care tasks (what needs to happen, how long it takes, priority)
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

person = Person(name = owner_name)
person.add_pet(Pet(name=pet_name, pet_type=species))

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.warning(
        "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
    )
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )
