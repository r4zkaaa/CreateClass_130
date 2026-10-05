class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi Panjang, panjang{self.panjang} cm, lebar{self.lebar}cm"

objek_persegi = PersegiPanjang(10, 5)
print(objek_persegi)

print("Keliling:", objek_persegi.hitung_keliling(), "cm")
print("Luas:", objek_persegi.hitung_luas(), "cm2")