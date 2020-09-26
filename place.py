"""..."""


# Create your Place class in this file


class Place:
    """..."""
    def __init__(self, name='', country='', priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        return f'{self.name},{self.country},{self.priority},{"v" if self.is_visited else "n"}'

    def str(self, no):
        return f'{" " if self.visited else "*"}{no}. {self.name:10s}in {self.country:10s} priority {self.priority:3d}'

    def visited(self):
        self.is_visited = True

    def unvisited(self):
        self.is_visited = False

    def is_important(self):
        return self.priority <= 2
