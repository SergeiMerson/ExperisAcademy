from abc import ABC, abstractclassmethod

class Animal(ABC):
    @classmethod(abstractclassmethod)
    def __init__(self, name, species, mass):
        self.name = name
        self.species = species
        self.mass = mass

    @staticmethod(abstractclassmethod)
    def create(name, species, mass, line_generator):
        pass


class Mammal(Animal):
    def __init__(self, name, species, mass, litter):
        super().__init__(name, species, mass)
        self.litter = litter

    @staticmethod
    def create(line_generator, name, species, mass):
        litter = int(next(line_generator))
        return line_generator, Mammal(name, species, mass, litter)


class Reptile(Animal):
    def __init__(self, name, species, mass, venomous):
        super().__init__(name, species, mass)
        self.venomous = venomous

    @staticmethod
    def create(line_generator, name, species, mass):
        venomus = next(line_generator)
        return line_generator, Reptile(name, species, mass, venomus)


class Bird(Animal):
    def __init__(self, name, species, mass, wingspan, talks, phrase=None):
        super().__init__(name, species, mass)
        self.wingspan = wingspan
        self.talks = talks
        self.phrase = phrase

    @staticmethod
    def create(line_generator, name, species, mass):
        phrase = None
        next_line = next(line_generator)
        wingspan, talks = int(next_line[0]), next_line[1]
        if talks == 'Takls':
            phrase = next(line_generator)[0]
        return line_generator, Bird(name, species, mass, wingspan, talks, phrase)


class Zoo:
    def __init__(self):
        self.catalog = {}

    def line_generator(file_path):
        with open(file_path, 'r') as zoo_file:
            for line in zoo_file:
                yield line.split()

    def process_line(self, line, class_dict):
        class_dict = {'Mammal': Mammal, 'Reptile': Reptile, 'Bird': Bird}
        if len(line) == 4:
            name, animal_type, species, weight = line[0], line[1], line[2], line[3]
            animal = class_dict[line[1]]

    def parse_file(self, file_path):
        line_gen = line_generator(file_path)
        line = next(line_gen)


file_path = 'Exercises/OOP/zoo_db.txt'


def line_generator(file_path):
    with open(file_path, 'r') as zoo_file:
        for line in zoo_file:
            yield line.split()


fff = line_generator(file_path)

class_dict = {'Mammal': Mammal, 'Reptile': Reptile, 'Bird': Bird}

def process_line(line, class_dict):
    if len(line) == 4:
        name, animal_type, species, weight  = line[0], line[1], line[2], line[3]
        animal = class_dict[line[1]]