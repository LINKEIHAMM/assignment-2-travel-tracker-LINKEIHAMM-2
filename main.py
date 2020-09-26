from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button
from place import Place
from placecollection import PlaceCollection

WATCHED_COLOR = (0.35, 0.35, 0, 1)
UNWATCHED_COLOR = (0, 0.35, 0.35, 1)


class TravelTrackerApp(App):
    collection: PlaceCollection
    current_key = StringProperty()
    columns = ListProperty()
    status_text = StringProperty()
    num_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.title = "Movies To Watch 2.0"
        self.collection = PlaceCollection()
        self.collection.load_places("places.csv")
        self.collection.sort("year")
        self.columns = ["Year", "Category", "Title", 'Watched']

    def build(self):
        """Build an application"""
        # app title
        self.title = "TravelTrackerApp"
        self.root = Builder.load_file('app.kv')

        self.current_key = 'Year'
        # all the valid actions
        self.actions = ["Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"]
        # clear all widgets
        self.clear_all()
        # create widgets
        self.create_widgets()
        self.status_text = ""
        self.num_text = "To watch: {}. Watched: {}".format(self.collection.un_visited(),
                                                           self.collection.un_visited())
        return self.root

    def change_state(self, key):
        """Handle change of spinner selection, output result to label widget """
        index = self.columns.index(key)
        keys = ["year", "category", "title", "is_watched"]
        self.collection.sort(keys[index])
        self.clear_all()
        self.create_widgets()

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""

        id = 0
        for places in self.collection.places:
            # create a button for each data entry, specifying the text and id
            name: str = "{} ({} from {})".format(places.name, places.country, places.visited)
            temp_button = Button(text=name, id=str(id), background_color=UNWATCHED_COLOR)
            if places.is_visited is True:
                temp_button = Button(text=name, id=str(id), background_color=WATCHED_COLOR)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)
            id += 1

    def press_entry(self, instance):
        """Handle pressing entry buttons.
        :param instance: the Kivy button instance that was clicked"""

        # get name (dictionary key) from the id of Button we clicked on
        print(instance.id)
        index = int(instance.id)

        # update status text
        movie = self.collection.movies[index]
        if movie.is_watched:
            # if you have watched the movie, set it unwatched
            self.status_text = "You have watched {}".format(movie.title)
            movie.to_unwatch()
        else:
            # if you have not watch the movie, set it watched
            self.status_text = "You watched {}".format(movie.title)
            movie.to_watch()
        self.num_text = "To watch: {}. Watched: {}".format(self.collection.get_number_of_unwatched(),
                                                           self.collection.get_number_of_watched())
        self.clear_all()
        self.create_widgets()

    def clear_all(self):
        """Clear all of the widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()

    def clear_input(self):
        """Cleat the text input"""

        self.root.ids.title_input.text = ""
        self.root.ids.year_input.text = ""
        self.root.ids.category_input.text = ""
        self.status_text = ""

    def add_movie(self, title, year, category):
        """Add movie to the collection"""

        title = title.strip()
        year = year.strip()
        category = category.strip()
        if title == "" or year == "" or category == "":
            self.status_text = "All fields must be completed"
            return
        try:
            year = int(year)
        except:
            # if the year is not a number
            self.status_text = "Please enter a valid number"
            return
        if year < 0:
            # if year is not valid
            self.status_text = "Please enter a valid number"
            return
        if category not in self.actions:
            # if invalid category
            self.status_text = "·	The category must be one of the following: " \
                               "Action, Comedy, Documentary, Drama, Fantasy, Thriller"
            return
        place = place(title, year, category, False)
        self.collection.add(place)
        self.collection.sort("year")  # sort by year
        self.clear_all()  # redraw the widgets
        self.clear_input()
        self.create_widgets()

    def on_stop(self):
        """Exit event, save all the movies"""

        self.collection.save("places.csv")


if __name__ == '__main__':
    TravelTrackerApp().run()
