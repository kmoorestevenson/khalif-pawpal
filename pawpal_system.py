class Pet:
    def __init__(
        self,
        name: str = "",
        age: int = 0,
        petType: str = "",
        pet_type: str | None = None,
        tasks: list["Task"] | None = None,
    ):
        if pet_type is not None and petType == "":
            petType = pet_type
        self.name = name
        self.age = age
        self.petType = petType
        self.tasks = tasks if tasks is not None else []


class Task:
    def __init__(
        self,
        date: int,
        type: str = "",
        priority: int = 0,
        name: str = "",
    ):
        self.date = date
        self.type = type
        self.priority = priority
        self.name = name
        self.completed = False

    def mark_complete(self) -> bool:
        self.completed = True
        return True

    def MarkComplete(self) -> bool:
        return self.mark_complete()


class Owner:
    def __init__(self, name: str = "", age: int = 0, pets: list[Pet] | None = None):
        self.name = name
        self.age = age
        self.pets = pets if pets is not None else []
        self.scheduler = Scheduler(self)

    def addPet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def add_pet(self, pet: Pet) -> None:
        self.addPet(pet)

    def removePet(self, pet: Pet) -> bool:
        if pet in self.pets:
            self.pets.remove(pet)
            return True
        return False

    def remove_pet(self, pet: Pet) -> bool:
        return self.removePet(pet)

    def find_pet(self, name: str) -> Pet | None:
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

    def FindPet(self, name: str) -> Pet | None:
        return self.find_pet(name)

    def add_task(self, pet_name: str, date: int, type: str, priority: int, name: str) -> bool:
        return self.scheduler.AddTask(pet_name, date, type, priority, name)

    def add_tasks(self, pet_name: str, date: int, type: str, priority: int, name: str) -> bool:
        return self.add_task(pet_name, date, type, priority, name)

    def AddTask(self, pet_name: str, date: int, type: str, priority: int, name: str) -> bool:
        return self.add_task(pet_name, date, type, priority, name)

    def remove_task(self, pet_name: str, name: str) -> bool:
        return self.scheduler.RemoveTask(pet_name, name)

    def RemoveTask(self, pet_name: str, name: str) -> bool:
        return self.remove_task(pet_name, name)

    def edit_task(self, pet_name: str, name: str, date: int, priority: int) -> bool:
        return self.scheduler.EditTask(pet_name, name, date, priority)

    def EditTask(self, pet_name: str, name: str, date: int, priority: int) -> bool:
        return self.edit_task(pet_name, name, date, priority)

    def mark_complete(self, pet_name: str, name: str) -> bool:
        return self.scheduler.MarkComplete(pet_name, name)

    def MarkComplete(self, pet_name: str, name: str) -> bool:
        return self.mark_complete(pet_name, name)

    def generate_schedule(self, cutoff_date: int, pet_name: str) -> list[Task]:
        return self.scheduler.GenerateSchedule(cutoff_date, pet_name)

    def GenerateSchedule(self, cutoff_date: int, pet_name: str) -> list[Task]:
        return self.generate_schedule(cutoff_date, pet_name)


class Scheduler:
    def __init__(self, owner: Owner | None = None):
        self.owner = owner

    def UpdateCompletedTask(self, tasks: list[Task], date: int) -> None:
        for task in tasks:
            if not task.completed and task.date < date:
                task.mark_complete()

    def update_completed_task(self, tasks: list[Task], date: int) -> None:
        self.UpdateCompletedTask(tasks, date)

    def GetPetTasks(self, pet_name: str) -> list[Task]:
        if self.owner is None:
            return []

        pet = self.owner.find_pet(pet_name)
        return pet.tasks if pet is not None else []

    def get_pet_tasks(self, pet_name: str) -> list[Task]:
        return self.GetPetTasks(pet_name)

    def AddTask(self, pet_name: str, date: int, type: str, priority: int, name: str) -> bool:
        if self.owner is None:
            return False

        pet = self.owner.find_pet(pet_name)
        if pet is None:
            return False

        if any(task.name == name for task in pet.tasks):
            return False

        pet.tasks.append(Task(date=date, type=type, priority=priority, name=name))
        return True

    def RemoveTask(self, pet_name: str, name: str) -> bool:
        if self.owner is None:
            return False

        pet = self.owner.find_pet(pet_name)
        if pet is None:
            return False

        for task in pet.tasks:
            if task.name == name:
                pet.tasks.remove(task)
                return True
        return False

    def EditTask(self, pet_name: str, name: str, date: int, priority: int) -> bool:
        if self.owner is None:
            return False

        pet = self.owner.find_pet(pet_name)
        if pet is None:
            return False

        for task in pet.tasks:
            if task.name == name:
                task.date = date
                task.priority = priority
                return True
        return False

    def MarkComplete(self, pet_name: str, name: str) -> bool:
        if self.owner is None:
            return False

        pet = self.owner.find_pet(pet_name)
        if pet is None:
            return False

        for task in pet.tasks:
            if task.name == name:
                task.mark_complete()
                return True
        return False

    def mark_complete(self, pet_name: str, name: str) -> bool:
        return self.MarkComplete(pet_name, name)

    def GenerateSchedule(self, cutoff_date: int, pet_name: str) -> list[Task]:
        if self.owner is None:
            return []

        pet = self.owner.find_pet(pet_name)
        if pet is None:
            return []

        pending_tasks = [
            task for task in pet.tasks if not task.completed and task.date <= cutoff_date
        ]
        return sorted(pending_tasks, key=lambda task: (task.date, -task.priority))