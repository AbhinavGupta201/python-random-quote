from os import sep
import random


def primary():
    # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last=len(quotes)-1

    rnd = random.randint(0, last)


    print(quotes[rnd],sep=" ",end=" ")


if __name__ == "__main__":
    print("todays Quotes:")
    primary()
    primary()
