from pydantic import BaseModel, constr


class TaskApartment(BaseModel):
    id: int


class TaskRoom(BaseModel):
    id: int


class Task(BaseModel):
    id: int
    name: str
    description: str
    apartment: TaskApartment
    rooms: list[TaskRoom]


class CreateTask(BaseModel):
    name: constr(max_length=32)  # type: ignore
    description: constr(max_length=128)  # type: ignore
    apartment: int
    rooms: list[int]


class UpdateTask(BaseModel):
    name: constr(max_length=32)  # type: ignore
    description: constr(max_length=128)  # type: ignore
    apartment: int
    rooms: list[int]
