"""..."""
from place import Place


# Create your PlaceCollection class in this file


class PlaceCollection:
    """..."""
    def __init__(self):
        self.places = []

    def load_places(self, filename):
        import csv
        with open(filename) as f:
            data = [row for row in csv.reader(f, delimiter=',', quotechar='|')]
        for row in data:
            place = Place(row[0], row[1], int(row[2]), row[3] == 'v')
            self.places.append(place)

    def add_place(self, place):
        self.places.append(place)

    def save_places(self, filename):
        with open(filename, 'w') as f:
            for p in self.places:
                f.write(str(p))
                f.write('\n')

    def sort(self, strategy):
        self.places.sort(
            key=lambda o: getattr(o, strategy)
        )

    def un_visited(self):
        return len([p for p in self.places if not p.is_visited])

    def __str__(self):
        return '\n'.join(str(place) for place in self.places)

    def list_places(self):
        for i, p in enumerate(self.places):
            print(p.str(i + 1))

    @property
    def place_size(self):
        return len(self.places)
