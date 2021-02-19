class Pokemon:

    def __init__(self, name, types, imag):
        self.name = name
        self.types = types
        self.imag = imag



    def __str__(self):
        return "{name} - tipo: {coxinha}".format(name=self.name, coxinha=self.types)



