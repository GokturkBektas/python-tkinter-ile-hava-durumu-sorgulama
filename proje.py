import tkinter as tk
import requests
def giris():
    sehir = girdi.get()
    api = "47342e54cb2b0a4273892e7130a5715d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api}"
    veri = requests.get(url)
    gelenveri = veri.json()

    if (gelenveri["cod"] != "404"):

        temp = gelenveri["main"]["temp"]
        derece = temp - 273.15
        nem = gelenveri["main"]["humidity"]
        rüzgarhizi = gelenveri["wind"]["speed"]
        gokdurum = gelenveri["weather"][0]["description"]
        ülke = gelenveri["sys"]["country"]
        cıktı = tk.Label(text=(
            f"Ülke: {ülke}\nHava Durumu: {gokdurum}\nSıcaklık: {derece:.2f}°C\nNem: {nem}%\nRüzgar Hızı: {rüzgarhizi}m/s")
            )
        cıktı.pack()

    else:
        cıktı = tk.Label(text="Bu isimde şehir bulunamadı")
        cıktı.pack()




pencere = tk.Tk()
pencere.geometry()
pencere.title("Hava Durumu")
etiket = tk.Label(text='Şehir')
etiket.pack(pady=10)
girdi = tk.Entry(pencere)
girdi.pack(pady=10)
buton = tk.Button(text="Ara",command=giris)
buton.pack(pady=10)



pencere.mainloop()