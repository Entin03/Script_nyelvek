#!/usr/bin/env python3


def main():
    star_wars = [("Episode I: The Phantom Menace", 1999),
                ("Episode II: Attack of the Clones", 2002),
                ("Star Wars: The Clone Wars", 2008-2020),
                ("Episode III: Revenge of the Sith", 2005),
                ("Solo: A Star Wars Story", 2018),
                ("Star Wars Rebels", 2014-2018),
                ("Rogue One: A Star Wars Story", 2016),
                ("Episode IV: A New Hope", 1977),
                ("Episode V: The Empire Strikes Back", 1980),
                ("Episode VI: Return of the Jedi", 1983),
                ("The Mandalorian", 2019),
                ("The Book of Boba Fett", 2021),
                ("Star Wars: Resistance", 2018-2020),
                ("Episode VII: The Force Awakens", 2015),
                ("Episode VIII: The Last Jedi", 2017),
                ("Episode IX: The Rise of Skywalker", 2019)]

    print("{0:^40} {1:<20}".format("Film neve", "Megjelenésének éve"))

    print("-" * 100)

    for element in star_wars:
        print("{nev:^40} {kiadas:<20}".format(nev=element[0],kiadas=element[1]))


if __name__ == "__main__":
    main()