class AnaMuharebe():
    renga ="5 km"
    speed = "70 km"
    price = "15 M$"
    armor = "15mm anti balistic"
    def __init__(self):
        self.harp = "Main Harp(Crash War)"
        self.radar = "20 km Aselsan"
class Obus():
    renga = "100 km"
    speed = "75 km"
    price = "25 M$"
    cannon = "150mm anti infaret,tank"
    def __init__(self):
        self.harp = "Back War(Bombardment)"
        self.radar = "180 km Lockheed Martin"
class multiplayer(Obus,AnaMuharebe):
    def __init__(self):
        AnaMuharebe.__init__(self)
        Obus.__init__(self)


Altay = multiplayer()
print (Altay.renga,Altay.speed,Altay.armor,Altay.cannon)