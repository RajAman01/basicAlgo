class Inverter:
    def __init__(self):
        Name = ""
        i = 0
        v = 0
        Battery = True

    def Details(self):
        self.Name = Name
        self.i = i
        self.v = v
        self.Battery = Battery


class SolarInverter(Inverter):
    Inverter.Name = ""
    Inverter.i = ""
    Inverter.v = ""
    Inverter.Battery = ""
    SolarPannel = ""
    GRID = ""


Name = "PCU"
i = 2
v = 5
Battery = "True"
GRID = "True"
result = Inverter
PowerRating = i * v
print(result(Name, PowerRating, Battery, SolarInverter(i, v, Battery, GRID)))
