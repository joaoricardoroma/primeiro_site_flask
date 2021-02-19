class Pokemon:

    def __init__(self, name, types):
        self.name = name
        self.types = types
        # self.ability = ability
        # self.moves = moves


    def __str__(self):
        return "{name} - tipo: {coxinha}".format(name=self.name, coxinha=self.types)



