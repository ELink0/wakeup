import random

class Semaforo:
    def __init__ (self):
        self.processoDormindo = []
        self.contador = 0

    def down(self, processo):
        if self.contador > 0:
            self.contador -= 1
        elif:
            self.processoDormindo.append(processo)

    def up(self, processo):
        if self.processoDormindo == None:
            self.contador += 1
        else:
            random.choice(processoDormindo)
            down()


class Processo:
