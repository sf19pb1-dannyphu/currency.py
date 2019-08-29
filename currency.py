"""
currency.py

Convert US dollars to other currencies.
Also times how long it took program to run.

"""

import sys
import timeit

#       EUR  GBP  CNY
rate = [.90, .82, 7.14]


def my_function():

    print("Convert your dollars to EUR, GBP, and CNY")
    print()

    while True:
        try:
            dol = float(input("How many US Dollars do you have? "))
        except EOFError:
            sys.exit(1)
        except KeyboardInterrupt:
            sys.exit(1)
        except ValueError:
            print()
            print("Please enter a numerical amount.")
        else:
            break

    conv = (f"""\
{dol:.2f} USD converts to:
{rate[0]*dol:.2f} EUR
{rate[1]*dol:.2f} GBP
{rate[2]*dol:.2f} CNY
""")
    print()
    print(conv)


#my_function() -no need to call function, it's being called below
secs = timeit.timeit(my_function, number = 1)
print(f"Note: this program took {secs:.2f} seconds to run")
print()

sys.exit(0)
