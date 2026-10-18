from __future__ import annotations


class Pet:
    def __init__(self, name: str = "", age: int = 0, pet_type: str = ""):
        self.name = name
        self.age = age
        self.pet_type = pet_type
        self.tasks = []


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
    ):
        self.name = name
        self.age = age
        self.email = email
        self.pets = pets if pets is not None else []

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

        pet = self.find_pet(pet_name)
        if not pet:
            return False

        pet.tasks.append(Task(duration=duration, task_type=task_type, priority=priority, name=name))
        return True

    def AddTask(self, duration: int, type: str, priority: int, name: str, pet_name: str) -> bool:
        return self.add_task(duration, type, priority, name, pet_name)

    def remove_task(self, pet_name: str, name: str) -> bool:
        pet = self.find_pet(pet_name)
        if not pet:
            return False
        for task in pet.tasks:
            if task.name == name:
                pet.tasks.remove(task)
                return True
        return False

    def RemoveTask(self, pet_name: str, name: str) -> bool:
        return self.remove_task(pet_name, name)

    def edit_task(self, pet_name: str, name: str, duration: int, priority: int) -> bool:
        pet = self.find_pet(pet_name)
        if not pet:
            return False
        for task in pet.tasks:
            if task.name == name:
                task.duration = duration
                task.priority = priority
                return True
        return False

    def EditTask(self, pet_name: str, name: str, duration: int, priority: int) -> bool:
        return self.edit_task(pet_name, name, duration, priority)

    def generate_schedule(self, duration: int, pet_name: str) -> list[Task]:
        pet = self.find_pet(pet_name)
        if not pet:
            return []
        selected_tasks: list[Task] = []
        remaining_time = duration

        for task in sorted(pet.tasks, key=lambda item: item.priority, reverse=True):
            if task.duration <= remaining_time:
                selected_tasks.append(task)
                remaining_time -= task.duration

        return selected_tasks

    def GenerateSchedule(self, duration: int, pet_name: str) -> list[Task]:
        return self.generate_schedule(duration, pet_name)


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
    person.tasks = []
else:
    person.tasks = [Task(duration=task["duration_minutes"], task_type=task["priority"], priority={"low": 1, "medium": 2, "high": 3}[task["priority"]], name=task["title"]) for task in st.session_state.tasks]

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
    person.add_tasks(duration=int(duration), task_type=priority, priority={"low": 1, "medium": 2, "high": 3}[priority], name=task_title, pet_name=pet_name)

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    selected = person.generate_schedule(duration, pet_name)
    st.warning(
        "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
    )
    markdown_list = "\n".join([f"- {item.name} , {item.duration} minutes, {item.priority}" for item in selected])
    st.markdown(
        markdown_list
    )
