from walrus import Database
from argparse import ArgumentParser
from math import factorial

def main():
    ap = ArgumentParser()

    ap.add_argument("-a", "--address", required=True, help="address for connection with redis")
    ap.add_argument("-p", "--port", required=True, help="port for connection with redis")
    args = vars(ap.parse_args())

    db = Database(host=args['address'], port=int(args['port']), db=0)
    print("--- Welcome to Factorial Calculator ---")
    while True:
        number = input("Please enter a non negative integer number: ")
        if number.isalpha() == True or int(number) < 0:
            print("You didn't write non negative integer!")
        else:
            if(db.get(number) is None):
                print("--- Calculating factorial ---")
                db[number] = factorial(int(number))
            else:
                print("--- Fetching result in cache ---")
            print(db[number].decode())


if __name__ == '__main__':
    main()
