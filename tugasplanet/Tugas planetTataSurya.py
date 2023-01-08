import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#membuat class dengan planet 
class Planet(object):
    #memberikan properti pada class planet
    namaPlanet = {
        'Saturnus' : "Planet Saturnus adalah salah satu planet dalam tata surya kita. Ini adalah planet kedua terbesar setelah Jupiter dan memiliki sistem tanda tangan yang indah, termasuk ikatannya yang terkenal. Saturnus terkenal karena memiliki sekitar 62 satelit alami yang tercatat, termasuk Titan, yang merupakan satelit terbesar kedua di Tata Surya setelah Ganymedes di Jupiter. Planet ini juga memiliki sistem angin yang kuat dengan angin yang mencapai kecepatan hingga 1800 kilometer per jam.\n\nBerikut ini adalah beberapa informasi tentang planet Saturnus:\n 1.Jarak Matahari: Saturnus berada pada jarak rata-rata\n 1,4 miliar kilometer (9,5 juta mil) dari Matahari.\n 2.Jumlah satelit: Saturnus memiliki sekitar 62 satelit alami yang tercatat.\n 3.Diameter: Diameter Saturnus adalah sekitar 120.000 kilometer, yang\nmembuatnya planet kedua terbesar dalam Tata Surya setelah Jupiter.\n 4.Massa: Massa Saturnus adalah sekitar 95 kali massa Bumi.\n 5.Rotasi: Saturnus memiliki waktu rotasi yang cukup panjang, dengan\nwaktu satu rotasi sekitar 10,7 jam di atas ekuator.\n 6.Orbit: Saturnus memiliki orbit yang cukup jauh dari Matahari, dengan\nwaktu yang diperlukan untuk satu orbit sekitar 29,5 tahun. ",
        'Bumi' : "Bumi adalah planet ketiga terdekat dari Matahari dalam Tata Surya, dan merupakan satu-satunya tempat di mana manusia dan kehidupan yang diketahui dapat bertahan.Bumi terdiri dari sejumlah lapisan yang terdiri dari inti yang terdiri dari besi dan nikel,mantel yang terdiri dari silikat, dan kulit bumi yang terdiri dari kerak  samudera dan daratan.Bumi juga memiliki atmosfer yang terdiri dari berbagai gas, termasuk oksigen, yang diperlukan untuk kelangsungan hidup manusia.Bumi juga memiliki satu satelit alami yang disebut Bulan, yang merupakan objek terbesar di sistem tata surya setelah Bumi sendiri.\n\nBerikut adalah beberapa properti Bumi:\n 1.Jarak dari Matahari: Bumi berada sekitar 149,6 juta kilometer (93 juta mil) dari Matahari.\n 2.Jumlah satelit: Bumi memiliki satu satelit alami yang disebut Bulan.\n 3.Massa: Massa Bumi sekitar 5,97 x 10^24 kilogram.\n 4.Diameter: Diameter Bumi sekitar 12,742 kilometer (7.917 mil) pada equator-nya.\n 5.Rotasi: Bumi berputar pada sumbunya sendiri sekitar kurang \ndari 24 jam, yang menyebabkan adanya siang dan malam.\n 6.Orbit: Bumi mengelilingi Matahari dalam orbit elips sekitar 365,25 hari.",
        'Jupiter' : "Jupiter adalah planet terbesar dalam tata surya kita. Ini adalah planet gas besar yang terdiri dari hidrogen dan helium. Jupiter memiliki beberapa satelit alami yang sangat besar, termasuk Io, Europa, dan Ganymede. Ini juga memiliki sistem angin yang kuat, dengan angin yang bergerak pada kecepatan yang sangat tinggi di atmosfer planet. Jupiter memiliki warna oranye yang khas yang disebabkan oleh senyawa yang disebut amonia.\n\nBerikut adalah beberapa fakta tentang Jupiter:\n 1.Jarak Jupiter dari Matahari adalah sekitar 778 juta kilometer (485 juta mil).\n Ini adalah planet kelima dari Matahari dalam tata surya kita.\n 2.Jupiter memiliki sekitar 79 satelit alami yang tercatat. Beberapa \nsatelit terbesar adalah Io, Europa, Ganymede, dan Callisto.\n 3.Diameter Jupiter adalah sekitar 142.984 kilometer (88.846 mil),\n yang membuatnya planet terbesar di tata surya kita.\n 4.Massa Jupiter adalah sekitar 1,8986 x 10^27 kg, atau sekitar 317,8 kali massa Bumi.\n 5.Rotasi Jupiter memakan waktu sekitar 9,9 jam untuk mengelilingi sumbu\n rotasi. Ini membuatnya planet tercepat dalam tata surya kita.\n 6.Orbit Jupiter mengelilingi Matahari dalam waktu sekitar 11,86 tahun.\n Ini membuatnya planet terjauh dari Matahari yang memerlukan\nwaktu terlama untuk mengelilingi Matahari.",
        'Uranus' : "Uranus adalah planet ke-7 dari Matahari dalam Tata Surya. Uranus merupakan planet terluar yang tergolong dalam kelompok planet luar (atau planet tua) yang terdiri atas Jupiter, Saturnus, Uranus, dan Neptunus. Uranus adalah planet gas yang terdiri terutama dari hidrogen, helium, dan air yang dikelilingi oleh atmosfer yang terdiri dari metana. Planet ini memiliki satelit-satelit yang indah  dan memiliki sistem angin yang kuat. Uranus memiliki rotasi yang sangat aneh, dengan sumbu rotasinya yang terletak sejajar dengan orbitnya di sekitar Matahari, sehingga waktu rotasinya sama dengan waktu orbitnya selama sekitar 84 tahun Bumi. \n\nBerikut adalah beberapa informasi mengenai Uranus:\n 1.Jarak Matahari: Uranus berada pada jarak rata-rata sekitar 2,8 miliar kilometer dari Matahari.\n 2.Jumlah satelit: Uranus memiliki 27 satelit yang diketahui saat ini.\n 3.Diameter: Diameter Uranus sekitar 51.118 kilometer, lebih kecil dari diameter\nJupiter dan Saturnus, namun lebih besar dari diameter Neptunus.\n 4.Massa: Massa Uranus sekitar 14,5 kali massa Bumi.\n 5.Rotasi: Uranus memiliki rotasi yang sangat aneh, dengan sumbu rotasinya\n yang terletak sejajar dengan orbitnya di sekitar Matahari. Hal ini menyebabkan\n waktu rotasinya sama dengan waktu orbitnya selama sekitar 84 tahun Bumi.\n6.Orbit: Uranus memiliki orbit elips yang melingkar di sekitar Matahari,\n dengan periode orbit sekitar 84 tahun Bumi.",
        'Neptunus' : "neptunes adalah planet ke-8 dari Matahari dan merupakan planet terluar di Tata Surya. Neptune memiliki satelit alami bernama Triton yang merupakan satelit terbesar kedua setelah satelit alami Ganymedes milik planet Jupiter. Neptunes memiliki diameter sekitar 49.500 km dan memiliki massa yang hampir setara dengan 17 kali massa Bumi. Neptunes memiliki atmosfer yang terdiri dari hidrogen, helium, dan metana yang menyebabkan warna biru pada planet ini. Neptunes  memiliki orbit yang memiliki panjang sekitar 4.498 juta km dari Matahari dan membutuhkan waktu sekitar 164 tahun untuk mengelilingi Matahari.\n\nBerikut adalah beberapa fakta tentang neptunus: \n 1.Jarak Matahari ke Neptunes bervariasi antara sekitar 2,7 juta km hingga \n sekitar 4,5 juta km, dengan jarak rata-rata sekitar 4,0 juta km.\n 2.Neptunes memiliki 13 satelit alami yang tercatat, dengan Triton sebagai satelit terbesar \n.3 Diameter Neptune sekitar 49.500 km, yang membuatnya lebih kecil dari \nJupiter tetapi lebih besar dari Uranus \n 4.Massa Neptune sekitar 17 kali massa Bumi \n 5. Rotasi Neptune membutuhkan waktu sekitar 16 jam untuk sekali putar pada sumbunya sendiri. \n 6.  Orbit Neptunes memiliki panjang sekitar 4,5 juta km dari Matahari\n dan membutuhkan waktu sekitar 164 tahun untuk mengelilingi Matahari.",
        'Mars' : "Planet Mars adalah planet kedua dari Matahari dalam Tata Surya. Planet ini terkenal karena warna merahnya yang disebabkan oleh oksida besi di permukaannya. Mars memiliki satelit alami bernama Phobos dan Deimos. Mars juga merupakan planet yang paling mirip dengan Bumi dari segi ukurannya dan juga memiliki sejarah yang dulu pernah memiliki air di permukaannya. Beberapa misi luar angkasa telah dikirim ke Mars untuk mengeksplorasi planet ini dan untuk mencari tanda-tanda keberadaan kehidupan di masa lalu.\n\nBerikut adalah beberapa informasi tentang Mars:\n 1.Jarak Matahari: Mars berjarak sekitar 228 juta kilometer (142 juta mil) dari Matahari.\n 2.Jumlah satelit: Mars memiliki 2 satelit alami bernama Phobos dan Deimos. \n 3.Diameter: Diameter Mars sekitar 6.792 kilometer (4.212 mil), sekitar 53% dari diameter Bumi.\n 4.Massa: Massa Mars sekitar 6,39 × 10^23 kg, sekitar 11% dari massa Bumi.\n 5.Rotasi: Mars memiliki rotasi yang cukup mirip dengan Bumi, dengan waktu rotasi\n sekitar 24,6 jam. Namun, karena Mars memiliki masa siklus sideris yang \nlebih panjang daripada Bumi, satu yang di Mars (waktu yang diperlukan]\n untuk rotasi sekitar sumbunya sendiri) terdiri dari sekitar 24,6 jam Bumi.\n 5.Orbit: Mars memiliki orbit yang cukup elips, dengan jarak terjauhnya dari \nMatahari sekitar 249 juta kilometer (154 juta mil) dan jarak terdekatnya sekitar\n 206 juta kilometer (128 juta mil). Ini berarti bahwa Mars memiliki jarak yang bervariasi\n dari Matahari selama tahun-tahunnya.",
        'Venus' : "Venus adalah planet kedua dari Matahari dalam Tata Surya. Ini adalah planet terdekat dengan ukuran yang sama dengan Bumi, dan juga merupakan planet terpanas di Tata Surya. Venus memiliki atmosfer yang tebal yang terdiri dari karbon dioksida dan nitrogen, dan tidak memiliki air di permukaannya. Venus juga memiliki periode rotasi yang sangat panjang, sehingga hari di Venus terasa lebih lama daripada hari di Bumi.\n\n Berikut ini adalah beberapa informasi mengenai Venus:\n 1.Jarak Matahari: Venus berada pada jarak kira-kira 41 juta km\n (26 juta mil) dari Matahari, yang membuatnya planet kedua dari Matahari.\n 2,Jumlah satelit: Venus tidak memiliki satelit.\n 3.Diameter: Diameter Venus adalah kira-kira 12.104 km (7.521 mil),\n yang sedikit lebih kecil dari diameter Bumi.\n 4.Massa: Massa Venus adalah kira-kira 4,87 x 10^24 kg, yang hampir\n sama dengan massa Bumi.\n 5.Rotasi: Venus memiliki periode rotasi yang sangat panjang, sekitar 243 hari bumi.\n Ini berarti bahwa hari di Venus terasa lebih lama daripada hari di Bumi.\n 6.Orbit: Venus memiliki orbit elips yang agak melengkung yang membawanya \nsekitar 41 juta km (26 juta mil) dari Matahari pada titik terjauhnya (aphelion) \ndan kira-kira 38 juta km (24 juta mil) pada titik terdekatnya (perihelion).",
        'Merkurius' : "Merkurius adalah planet terkecil dalam Tata Surya. Ini adalah planet terdekat dengan Matahari dan memiliki siklus orbit yang paling cepat di antara semua planet. Merkurius memiliki diameter hanya sekitar sepertiga dari Bumi dan tidak memiliki satelit atau atmosfer yang signifikan. Planet ini terkenal karena suhu permukaannya yang sangat tinggi dan rendah, berkisar antara -173 derajat Celsius di malam hari hingga 427 derajat Celsius di siang hari. Merkurius juga memiliki pola rotasi yang unik, dengan waktu rotasi yang sama dengan waktu revolusinya, sehingga satu sisi planet selalu menghadap Matahari.\n\nBerikut adalah beberapa informasi tentang Merkurius:\n 1.jarak Matahari: Merkurius berada pada jarak rata-rata 57,9 juta kilometer dari Matahari,\n yang merupakan jarak terdekat antara planet dengan Matahari dalam Tata Surya.\n 2.Jumlah satelit: Merkurius tidak memiliki satelit \n 3.Diameter: Diameter Merkurius sekitar 4.880 kilometer, lebih kecil dari Bumi namun\n lebih besar dari Pluton\n 4.Massa: Massa Merkurius adalah sekitar 3,3% massa Bumi.\n 5.Rotasi: Waktu rotasi Merkurius adalah sekitar 58,7 hari Bumi, yang sama\n dengan waktu revolusinya. Ini berarti satu sisi planet selalu menghadap Matahari.\n 6.Orbit: Merkurius memiliki orbit yang paling terbelakang dari semua planet,\n dengan waktu revolusi sekitar 87,97 hari Bumi. Ini juga merupakan planet dengan\n elips orbit paling tidak teratur di antara semua planet.",
        'kelompokMANGGA' : "NAMA KELOMPOK: \n 1. MH ANGGA KUSUMA WARDANY (L200220133)\n 2. NADIA ALIFA(L200220170)\n 3. DIMAS RIZKI P(L200220196) \n4. DZAKY RAYSSA BUNTORO(L200220117)\n 5. BRILIAN (L00220152)\n 6. ZALRA TUNJUNG SAFIRA(L200220163),\n 7. FAJAR HASAN ABDULLAH(L200220106)",
    }
    # memberikan objek nama
    def __init__(self, nama):
        self.nama = nama
    # menampilkan gambar yang akan ditampilkan
    def showImage(self):
        for i in Planet.namaPlanet:
            if i == self.nama:# Buka gambar planet
                return Image.open(i + ".jpg")
    # menampilkan deskripsi planet atau properti planet
    def showTeks(self):
        for i in Planet.namaPlanet:
            if i == self.nama:
                return Planet.namaPlanet[i]


# Buat jendela utama
root = tk.Tk()
root.title("Planet Tata Surya")
root.geometry("1200x1080")

# Buat menu utama
menu = tk.Menu(root)
root.config(menu=menu)

# Buat menu File
file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=None)
file_menu.add_command(label='Open', command=None)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

# Buat Edit menu
edit_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Undo', command=None)
edit_menu.add_command(label='Redo', command=None)

# buat View menu
view_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label='View', menu=view_menu)
view_menu.add_command(label='Zoom In', command=None)
view_menu.add_command(label='Zoom Out', command=None)

# buat Help menu
help_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=None)

# Buat objek gaya untuk menyesuaikan tampilan widget
style = ttk.Style()
style.configure('.', font=('TimesNewRoman', 12), padding=10)

# Buat label untuk menampilkan judul
title = ttk.Label(root, text="Planet Tata Surya")
title.pack(side='top', fill='x')

# Buat kotak kombo untuk memungkinkan pengguna memilih planet
planet_combo = ttk.Combobox(root, values=list(Planet.namaPlanet.keys()))
planet_combo.pack(side='top', fill='x')

# Buat label untuk menampilkan gambar
image_label = ttk.Label(root)
image_label.pack(side='left')

# Buat label untuk menampilkan informasi
info_label = ttk.Label(root, text="", wraplength=400)
info_label.pack(side='left')

# Buat fungsi untuk memperbarui gambar dan informasi saat pengguna memilih planet
def update_planet(*args):
    planet_name = planet_combo.get()
    planet = Planet(planet_name)
    image = planet.showImage()
    image = ImageTk.PhotoImage(image)
    image_label.configure(image=image)
    image_label.image = image
    info_label.configure(text=planet.showTeks())

# Ikat fungsi update_planet ke acara "pilih" kotak kombo
planet_combo.bind('<<ComboboxSelected>>', update_planet)

# Mulai loop acara GUI
root.mainloop()

