from myclass import Film, FilmShell
from myboxiterator import MyBoxIterator


def main () :
    film_1 = Film('v boi idut odni "stariki".', 92, "SSSR")
    print(film_1 . max_recommended_duration)
    film_1 = change_max_recommended_duration (95)
    print(film_1 . max_recommended_duration)
    print(film_1. name)
    print(film_1. duration)
    print(film_1. country)

    film_2 = Film('djentlmen udachi.', 84, "SSSR")

    shell = FilmShell ()
    print (shell. contained_film)
    shell.add(film_1)
    shell.add(film_2)
    print(shell.contained_film)
    print(shell.len())
    shell.remove(film_1)
    print(shell.contained_film)
    print(shell. contains(film_2))
    print(shell. contains(film_1))
    shell.add(film_2)
    print(shell.iterator(film_2))

    counter = MyBoxIterator(shell. contained_film)

    print(counter. __iter__())
    print(counter. __next__())


if __name__ == '__main__' :
    main()

