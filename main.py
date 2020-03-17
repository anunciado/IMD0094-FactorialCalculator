from walrus import Database
from argparse import ArgumentParser
from math import factorial

def main():
    # Setting pattern for redis
    pattern = 'factorial:'

    # Searching for parameters passed in the terminal
    ap = ArgumentParser()
    ap.add_argument("-a", "--address", required=True, help="address for connection with redis")
    ap.add_argument("-p", "--port", required=True, help="port for connection with redis")
    args = vars(ap.parse_args())

    # Instantiating an object that connects to a redis database using the parameters passed
    db = Database(host=args['address'], port=int(args['port']), db=0)
    print("--- Welcome to Factorial Calculator ---")
    while True:
        number = input("Please enter a non negative integer number: ")

        # Checking if the entered string is alphanumeric or, if it is a number, less than 0
        try:
            if number.isalpha() == True or int(number) < 0:
                print("You didn't write non negative integer!")
            else:
                # Checking if the number has already been calculated and is in the cache
                if(db.get(pattern + number) is None):
                    print("--- Calculating factorial ---")
                    # Setting result in cache
                    db[pattern + number] = factorial(int(number))
                else:
                    print("--- Fetching result in cache ---")
                # Fetching result in cache
                print(db[pattern + number].decode())
        except ValueError:
                print("You didn't write non negative integer!")


if __name__ == '__main__':
    main()
