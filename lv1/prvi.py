radni_sati = input("Unesite broj radnih sati: ")
placa = input("Unesite placu po satu: ")

#rezultat = int(radni_sati) * int(placa)

def total_euro(x, y):
    return x * y

print("Radnik je zaradio", total_euro(int(radni_sati), int(placa)), "eura")