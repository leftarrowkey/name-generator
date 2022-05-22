import random

with open("names.txt", "r") as file:
    namelist = [i.strip() for i in file.readlines()]

with open("suffixes.txt", "r") as file:
    suffixes = [i.strip() for i in file.readlines()]

with open("titles.txt", "r") as file:
    titles = [i.strip() for i in file.readlines()]

with open("places.txt", "r") as file:
    places = [i.strip() for i in file.readlines()]

with open("prefixes.txt", "r") as file:
    prefixes = [i[0:i.index("\n")] for i in file.readlines()]

while True:
    names = []
    for i in range(random.randint(1, 3)):
        names.append(namelist[random.randint(0, len(namelist) - 1)])
    names.append(
            " ".join([
                "-".join([
                        prefixes[random.randint(0, len(prefixes) - 1)] +
                        namelist[random.randint(0, len(namelist) - 1)] +
                        suffixes[random.randint(0, len(suffixes) - 1)]
                        for i in range(random.randint(1, 2))])
                    for i in range(random.randint(1, 2))
                ])
            )
    if random.randint(0, 5) == 0:
        for i in range(random.randint(1, 10)):
            place = "".join([
                places[random.randint(0, len(places) - 1)] + (" " * random.randint(0, 1))
                for k in range(random.randint(1, 5))
            ])
            if place[-1] == " ":
                place = place[0:-1]
            names.append("\b, {} of {}".format(
                titles[random.randint(0, len(titles) - 1)],
                place
            ))

    print(*names)
    input()
