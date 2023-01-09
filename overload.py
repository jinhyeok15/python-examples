from typing import overload, Type, Union
from typing_extensions import reveal_type


def introduce(name: Union[str, Type['Name'], int]) -> Union[str, Type['Introduce']]:
    if isinstance(name, str):
        return Introduce.myself_(name)
    elif isinstance(name, int):
        return None
    elif name.__class__.__name__=='Name':
        introduce = Introduce(name)
        return introduce
    raise TypeError


@overload
def introducer(name: str) -> str:
    ...

@overload
def introducer(name: Type['Name']) -> Type['Introduce']:
    ...

def introducer(name):
    if isinstance(name, str):
        return Introduce.myself_(name)
    elif isinstance(name, int):
        return None
    else:
        introduce = Introduce(name)
        return introduce


class Introduce:
    def __init__(self, name: Type['Name']):
        self.name = name

    def myself(self):
        return f"Hi my name is {self.name.my_name}"
    
    @staticmethod
    def myself_(name: str):
        return f"Hi my name is {name}"


class Name:
    def __init__(self, name: str):
        self.my_name = name


class Job:
    def __init__(self, job_name: str):
        self.my_job = job_name


if __name__=="__main__":
    reveal_type(introduce(Name("mivv")))
    reveal_type(introducer("mivv"))

    name = "mivv"
    print(introduce(name))

    name = 1
    print(introduce(name))

    name = Name("mivv")
    print(introduce(name))

    job = Job("Student")
    print(introduce(name))
