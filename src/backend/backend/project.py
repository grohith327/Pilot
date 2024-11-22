from .element import Element


class Project:
    """
    Class that represents a project.
    """

    def __init__(self, id: str, name: str, elements: list[Element]):
        self.id = id
        self.name = name
        self.elements = elements
        # Add a bandit algorithm type
