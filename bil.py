#skapade en klass

class bil:

    #construktor
    def __init__(self, fabrikat, color, lager):

        self.fabrikat=fabrikat
        self.color=color
        self.lager=lager

    def setfabrikat(self, fabrikat):
        self.fabrikat=fabrikat

    def getfabrikat(self):
        return self.fabrikat

    def setcolor(self, color):
        self.color = color

    def getcolor(self):
        return self.color