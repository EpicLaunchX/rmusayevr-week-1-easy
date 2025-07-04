from copy import deepcopy

age: int = 32
height: float = 1.85
name: str = "Rashad"
surname: str = "Musayev"
ID: str = name + " " + surname
last_letter: str = name[-1]
surname_slice: str = surname[1:3]
new_list: list[int] = [3, 4, 5, 6, 7]
new_awesome_list: list[int] = deepcopy(new_list)
