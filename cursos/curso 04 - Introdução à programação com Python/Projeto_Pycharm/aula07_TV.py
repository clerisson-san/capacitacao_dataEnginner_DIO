# Implemtar métodos

class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 2

        print("Televisão On/Off: {}".format(self.ligada))
        print("Televisão canal: {}".format(self.canal))

# É um MÉTODO (Não retorna nada, ao contrario da FUNÇÃO)
    def power(self):
        if self.ligada:
            self.ligada = False
            print("\nTelevisão On/Off: {}".format(self.ligada))
        else:
            self.ligada = True
            print("\nTelevisão On/Off: {}".format(self.ligada))

# Método mudança de canal de
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
            print("\nTelevisão Canal: {}".format(self.canal))
        else:
            print("\nTelevisão On/Off: {}".format(self.ligada))

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1
            print("\nTelevisão Canal: {}".format(self.canal))
        else:
            print("\nTelevisão On/Off: {}".format(self.ligada))


if __name__ == "__main__":

    televisao = Televisao()

    televisao.power()
    televisao.power()
    televisao.power()

    televisao.aumenta_canal()
    televisao.aumenta_canal()

    televisao.diminui_canal()
    televisao.diminui_canal()
    televisao.diminui_canal()
