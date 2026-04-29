class Avtomobil:
    def __init__(self, model, yil, tezlik):
        self.model = model
        self.yil = yil
        self.tezlik = tezlik

    def malumot(self):
        print(f"Model: {self.model}")
        print(f"Yil: {self.yil}")
        print(f"Tezlik: {self.tezlik}")

    def tezlik_oshir(self, qiymat):
        self.tezlik += qiymat
        print(f"Yangi tezlik: {self.tezlik} km")


a1 = Avtomobil('BMW', 2022, 120)
a1.malumot()
a1.tezlik_oshir(30)
