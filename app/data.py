from csv import reader


def read_countries() -> list[list[str, str]]:
    with open("app/countries-in-the-world.csv") as csvfile:
        return list(reader(csvfile))
