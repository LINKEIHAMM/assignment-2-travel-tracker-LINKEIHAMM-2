"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place
from placecollection import PlaceCollection





def show_menu():
    print('Menus:')
    print('L - List places')
    print('A - Add new place')
    print('M - Mark a place as visited')
    print('Q - Quit')


def input_places():
    while True:
        name = input('Name: ')
        if not name.strip():
            print('Input can not be blank')
            continue
        break

    while True:
        country = input('Country: ')
        if not country.strip():
            print('Input can not be blank')
            continue
        break

    while True:
        priority = input('Priority: ')
        try:
            priority = int(priority)
            if priority <= 0:
                print('Number must be > 0')
        except:
            print('Invalid input; enter a valid number')
            continue
        break
    return Place(name, country, priority, False)


def main():
    print("Travel Tracker 1.0 - by LINKEIHAMM")
    filename = 'places.csv'
    place_collection = PlaceCollection()
    place_collection.load_places(filename)

    print(f'{len(place_collection.places)} places loaded from {filename}')

    while True:
        show_menu()
        user_input = input('>>> ')
        user_input = user_input.upper()

        if user_input not in ('L', 'A', 'M', 'Q'):
            print('Invalid menu choice')
            continue
        print(f'user input {user_input}')

        if user_input == 'L':
            place_collection.list_places()
        elif user_input == 'A':
            new_places = input_places()
            place_collection.add_place(new_places)
            print(f'{new_places.name} in {new_places.country} (priority {new_places.priority}) added to Travel Tracker')
        elif user_input == 'M':
            place_collection.list_places()
            print(f'{len(place_collection.places)} places. You still want to visit {place_collection.un_visited} places.')
            print('Enter the number of a place to mark as visited')
            while True:
                index = input('>>> ')
                try:
                    index = int(index)
                    if index <= 0:
                        print('Number must be > 0')
                        continue
                    if index > place_collection.place_size:
                        print('Invalid place number')
                        continue
                    place_collection.sort('priority')
                    place = place_collection.places[index - 1]
                    if place.visited:
                        print('That place is already visited')
                        break
                    else:
                        place.visited = True
                        print(f'{place.name} in {place.country} visited!')
                        break
                except ValueError:
                    print('Invalid input; enter a valid number')
        elif user_input == 'Q':
            print(f'{place_collection.place_size} places saved to {filename}')
            place_collection.save_places(filename)
            break


if __name__ == '__main__':
    main()
