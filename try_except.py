class Book:
    page = 100	


def first_example () :
    d = {}
    try:
      print (d["a"])
    except KeyError as e:
      print("Example 1, Key Error: {} ". format (e))
def second_example () :
    book_1 = Book ()
    try:
      print(book_1. name)
    except AttributeError as e:
      print("Example 2, Attribute Error: {}". format (e))
def third_example() :
    try:
      open("test", "r", encoding="utf-8"). read()
    except IOError as e:
       print("Example 3, IO Error: ()". format (e))


def main () :
    first_example ()
    second_example ()
    third_example ()



if __name__ == " __main__" :
   main ()
