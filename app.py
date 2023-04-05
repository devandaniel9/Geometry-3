# Title

# List import
import numpy as np
import math
import streamlit as st

# from PIL import Image
from PIL import Image, ImageDraw, ImageFont

# Menjalankan program
# streamlit run 'Geometri 4.py'

# @import fonts/Roboto-Regular.ttf;

aaa = """
	<style>
	@import fonts/Roboto-Regular.ttf;

	html, body, [class*="css"]  {
	font-family: 'Roboto', sans-serif;
	}
	</style>
"""

streamlit_style = """
	<style>
	@import fonts;

	[class*="css"]  {
	font-family: 'roboto';
	}
	</style>
"""

def color(text, c):
    return f"<font color={c}>{text}</font>"

st.markdown(streamlit_style, unsafe_allow_html=True)
# st.write(f"The next word is {color('red','yellow')}", unsafe_allow_html=True)

def stw(text):
    return st.markdown(text, unsafe_allow_html=True)

st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',
unsafe_allow_html=True
)

# Streamlit
# st.write("""# Geometri 3""")
# st.write('# :red[Program Geometri]')
# st.markdown("# <u><font color='yellow'>Program Geometri</font></u>", unsafe_allow_html=True)
st.markdown("# <font color='#ffd080'>Program Geometri</font>", unsafe_allow_html=True)

# -----

# stw(color('Dibuat oleh','#ffb0a0'))
st.write('### **Dibuat oleh Devan Daniel**')
stw(f"**{color('Geometri','#d0ff80')}** adalah bangun yang punya sisi, luas, dan volume. Ada banyak jenis geometri dan bisa melihat gambarnya.")
# st.text('Link')
st.write('Program Geometri terdiri dari Bangun Datar, Bangun Ruang, Sudut, dan Pythagoras')
st.write('Lebih lengkap di tab Definisi')
st.write('')

# st.write('## **Pengaturan**')
# with st.expander("Tampilkan"):
# st.write('## **Satuan**')
satuan_list = ['Tidak ada', 'Centimeter (cm)', 'Meter (m)']
# satuan = st.radio('Pilih satuan', satuan_list)
satuan = 'Tidak ada'
if satuan == satuan_list[0]: sat = ''
elif satuan == satuan_list[1]: sat = 'cm'
else: sat = 'm'
st.write('### **Link**')
st.write('Link program Bangun Datar dan Bangun Ruang:  \nhttps://devandaniel9-shape-program-devan-7zwso4.streamlit.app/')
# st.write('### **Lanjutan**')
# st.write('[Coming Soon]')
# st.write('### **Tentang**')
# st.write('Copyright © ?????')
# st.write('Dibuat oleh Devan Daniel')
# st.write('### **Reset**')
# st.button('Reset Settings')
st.write('')

# st.write('## **Geometri**')
check1 = st.checkbox('Hasil Gambar')
check2 = st.checkbox('Langkah Penyelesaian')

if check1:
    resolution = 1000

    im = Image.new('RGB', (resolution,resolution))
    draw = ImageDraw.Draw(im)

    font_list = [
        "arial.ttf",
        "ariblk.ttf",
        "Roboto-Regular.ttf",
        "consola.ttf",
        "FreeSans.ttf",
        "FreeSansBold.ttf"
    ]

    font_index = 0
    font = font_list[font_index]

    def roboto(size):
        # return ImageFont.truetype("ariblk.ttf", size=size, encoding='utf-32')
        return ImageFont.truetype(f"fonts/{font}", size=size)

st.write('')
geometri_list = ["Bangun Datar", "Bangun Ruang", "Sudut", "Pythagoras", "Definisi"]
geometri = st.selectbox("Pilih jenis Geometri:", geometri_list)

digit = 3
def fungsi(angka):
    a = round(angka, digit)
    if round(angka, digit) == round(angka, 0):
        angka = int(a)
    else:
        angka = a
   
    return angka

# print(fungsi(3.99999999))

# oi = open image

def open_image(nama):
    try:
        # img = Image.open(f"{bentuk}.png")
        img = Image.open(f'images/{nama}')
        # st.image(img, width=200)
        st.image(img, width=300)
    except FileNotFoundError:
        img = ""

def fsatuan(satuan, power):
    if satuan != '':
        if power <= 1: return f'{satuan}'
        else: return f' {satuan}^{power}'
    return ''

if geometri == geometri_list[0]:
    st.write('**Bangun Datar** adalah bangun yang 2 dimensi dalam geometri. Terdapat satuan panjang dan lebar.')
    st.write('Luas Bangun Datar adalah melihat keseluruhan bangun datar. Sedangkan Keliling Bangun Datar adalah keliling pada pinggir bangun tersebut.')
    st.write('Simbol Luas adalah L dan Keliling adalah K')
    st.write()

    bentuk_list = ["Persegi", "Persegi Panjang", "Jajar Genjang", "Trapesium", "Segitiga", "Segilima", "Lingkaran", "Elips"]
    bentuk = st.selectbox(f"Pilih jenis {geometri}:", bentuk_list)

    if bentuk == bentuk_list[0]:
        col = st.columns(2)
        with col[0]: open_image("Persegi.png")
        with col[1]:
            # stw(f"<font size='5'><b>{bentuk}</b></font>")
            st.write('**Persegi** dalam bangun datar adalah kedua sisi yang sama, dengan panjang dan lebar yang sama. Persegi mempunyai diagonal yang miring.')
            st.write('Disini akan mencari Luas dan Keliling persegi')
        st.write('### **Rumus**')
        st.latex(r"L = sisi\times sisi")
        # ■□
        st.latex(r"L□ = s^2 = s\times s")
        st.latex(r"K□ = 4\times s")
        # sisi = st.number_input("Sisi (cm)")

        st.write('### **Input**')
        sisi = float(st.text_input("Sisi", value=2))
        st.write('## **Hasil Penyelesaian**')
        luas = sisi**2
        keliling = 4*sisi
        diagonal = np.sqrt(2)*sisi
        # st.markdown(f"Luas = {fungsi(luas)}")
        # st.markdown(f"Keliling = {fungsi(keliling)}")
        # st.markdown(f"Diagonal = {fungsi(diagonal)}")
        st.write(f"Luas = {fungsi(luas)} {fsatuan(sat,2)}")
        st.write(f"Keliling = {fungsi(keliling)} {fsatuan(sat,1)}")
        st.write(f"Diagonal = {fungsi(diagonal)} {fsatuan(sat,1)}")

    if bentuk == bentuk_list[1]:
        col = st.columns(2)
        with col[0]: open_image("Persegi Panjang.png")
        with col[1]: st.write('**Persegi Panjang** adalah bangun yang terdiri dari dua sisi, yaitu panjang (p) dan lebar (l).')
        st.write('### **Rumus**')
        st.latex(r"L = panjang\times lebar")
        st.latex(r"L▭ = p\times l")
        st.latex(r"K▭ = 2\times (p+l)")

        st.write('### **Input**')
        col = st.columns(2)
        with col[0]: panjang = float(st.text_input("Panjang", value=2))
        with col[1]: lebar = float(st.text_input("Lebar", value=3))
        st.write('## **Hasil Penyelesaian**')
        luas = panjang*lebar
        keliling = 2*(panjang+lebar)
        diagonal = np.sqrt(panjang**2+lebar**2)
        st.write(f"Luas = {fungsi(luas)} {fsatuan(sat,2)}")
        st.write(f"Keliling = {fungsi(keliling)} {fsatuan(sat,1)}")
        st.write(f"Diagonal = {fungsi(diagonal)} {fsatuan(sat,1)}")

    if bentuk == bentuk_list[2]:
        open_image("Jajar Genjang.png")
        st.write('**Jajar Genjang** adalah alas yang sejajar dengan sisi miring')
        st.write('### **Rumus**')
        st.latex(r"L = alas\times tinggi")
        st.latex(r"L▱ = a\times t")

        st.write('### **Input**')
        col1 = st.columns(2)
        with col1[0]: alas = float(st.text_input("Alas", value=2))
        with col1[1]: tinggi = float(st.text_input("Tinggi", value=3))
        st.write('## **Hasil Penyelesaian**')
        luas = alas*tinggi
        st.write(f"Luas = {fungsi(luas)} {fsatuan(sat,2)}")

    if bentuk == bentuk_list[3]:
        open_image("Trapesium.png")
        st.write('**Trapesium** adalah 4 sisi dengan satu pasang sisi sejajar')
        st.write('### **Rumus**')
        st.latex(r"L = \frac{a+b}{2}\times t")
        st.write('### **Input**')
        sisi_a = float(st.text_input("Sisi a", value=2))
        sisi_b = float(st.text_input("Sisi b", value=3))
        tinggi = float(st.text_input("Tinggi", value=4))
        st.write('## **Hasil Penyelesaian**')
        luas = (sisi_a+sisi_b)*tinggi/2
        st.write(f"Luas = {fungsi(luas)} {fsatuan(sat,2)}")

    if bentuk == bentuk_list[4]:
        open_image("Segitiga.png")
        st.write('**Segitiga** adalah bangun yang terdiri dari 3 siri, yaitu alas dan 2 sisi miring. Terdapat alas (a) dan tinggi (t)')
        st.write('Ada 4 jenis segitiga, yaitu Segitiga Siku-Siku, Segitiga Sama Sisi, Segitiga Sama Kaki, dan Segitiga Sembarang')
        bangun_list = ["Segitiga Siku-Siku", "Segitiga Sama Sisi", "Segitiga Sama Kaki", "Segitiga Sembarang"]
        bangun = st.selectbox(f"Pilih jenis {bentuk}:", bangun_list)
        if bangun == bangun_list[0]:
            open_image("triangle1.jpg")
            st.write('### **Rumus**')
            st.write('[Coming Soon]')
            st.write('### **Input**')
            alas = float(st.text_input("Alas", value=4))
            tinggi = float(st.text_input("Tinggi", value=3))
            st.write('## **Hasil Penyelesaian**')
            luas = alas*tinggi/2
            st.write(f"Luas = {fungsi(luas)} {fsatuan(sat,2)}")
        if bangun == bangun_list[1]:
            open_image("triangle2.png")
            st.write('### **Rumus**')
            st.write('[Coming Soon]')
            st.write('### **Input**')
            st.write('[Coming Soon]')
        if bangun == bangun_list[2]:
            open_image("triangle3.jpg")
            st.write('### **Rumus**')
            st.write('[Coming Soon]')
            st.write('### **Input**')
            st.write('[Coming Soon]')
        if bangun == bangun_list[3]:
            open_image("custom.jpg")
            st.write('### **Rumus**')
            st.latex(r"L = \sqrt{S(S-a)(S-b)(S-c)}")
            st.latex(r"S = \frac{a+b+c}{2}")
            st.latex(r"K = a+b+c")
            st.write('### **Input**')
            col1 = st.columns(2)
            col2 = st.columns(2)
            with col1[0]:
                a = int(st.text_input("Sisi A", value=5))
            with col1[1]:
                b = int(st.text_input("Sisi B", value=9))
            with col2[0]:
                c = int(st.text_input("Sisi C", value=7))

            st.write('## **Hasil Penyelesaian**')

            if check1:
                st.write('## **Hasil Gambar**')

                draw.text((20,20), 'Segitiga Sembarang', fill='white', font=roboto(60))

                hasil = (a**2+b**2-c**2)/(2*a*b)
                hasil2 = (a**2+c**2-b**2)/(2*a*c)
                # print(hasil,hasil2)
                # print(round(np.rad2deg(np.arccos(hasil)),1))

                x = b*hasil
                y = b*(1-hasil**2)**0.5

                # c = 2

                x2 = c*hasil2
                y2 = c*(1-hasil2**2)**0.5

                xa = 100
                ya = 200
                size = 40

                draw.polygon((xa,ya,xa+100*a,ya,xa+100*x,ya+100*y), fill=(32,32,32))
                draw.ellipse((xa-10,ya-10,xa+10,ya+10), fill='white')
                draw.line((xa,ya,xa+100*a,ya), fill='white', width=2)
                draw.text((xa+50*a,ya-(3*size)//5), str(a), fill='white', font=roboto(size), anchor='mm')
                draw.ellipse((xa-10+100*a,ya-10,xa+10+100*a,ya+10), fill='white')
                draw.line((xa,ya,xa+100*x,ya+100*y), fill='white', width=2)
                draw.text((xa+50*x-size//10*y,ya+50*y+size//10*x), str(b), fill='white', font=roboto(size), anchor='mm')
                draw.ellipse((xa-10+100*x,ya-10+100*y,xa+10+100*x,ya+10+100*y), fill='white')
                draw.line((xa+100*a,ya,xa+100*(a-x2),ya+100*y2), fill='white', width=2)
                draw.text((xa+100*a-50*x2+size//10*y2,ya+50*y2+size//10*x2), str(c), fill='white', font=roboto(size), anchor='mm')

                s = (a+b+c)/2
                luas = (s*(s-a)*(s-b)*(s-c))**0.5
                keliling = a+b+c

                draw.text((20,860), f"Luas: {fungsi(luas)}\nKeliling: {fungsi(keliling)}", fill='white', font=roboto(50))

                im.save("preview.png")
                st.image("preview.png")

    if bentuk == bentuk_list[5]:
        open_image("segilima.jpg")
        st.write('**Segilima** atau Pentagon adalah bangun yang terdiri dari 5 sisi')
        st.write('### **Rumus**')
        st.write('### **Input**')

    if bentuk == bentuk_list[6]:
        col = st.columns(2)
        with col[0]: open_image("Lingkaran.png")
        with col[1]:
            st.write('**Lingkaran** adalah bangun datar yang berbentuk bulat dan melengkung. Ada hubungannya dengan pi (π)')
            st.write('Bilangan pi (π) kira-kira 3.14 atau 22/7. Konstanta pi (π) = 3.14159...')
        st.write('### **Rumus**')
        st.latex(r"L = pi\times radius^2")
        st.latex(r"L⊙ = \pi r^2")
        st.latex(r"K⊙ = 2\pi r")

        st.write('### **Input**')
        radius = float(st.text_input("Radius", value=2))
        st.write('## **Hasil Penyelesaian**')
        diameter = 2*radius
        luas = math.pi*radius**2
        keliling = 2*math.pi*radius
        st.write(f"Diameter = {fungsi(diameter)} {fsatuan(sat,1)}")
        st.write(f"Luas = {fungsi(luas)} {fsatuan(sat,2)}")
        st.write(f"Keliling = {fungsi(keliling)} {fsatuan(sat,1)}")

    if bentuk == bentuk_list[7]:
        open_image("Elips.png")
        st.write('**Elips (ellipse)** adalah lingkaran yang lonjong, dengan panjang dan lebar yang berbeda.')
        st.write('### **Rumus**')
        st.latex(r"L = \pi \times p \times l")
        st.latex(r"K \approx \pi \sqrt{p^2+l^2}")

        st.write('### **Input**')
        panjang = float(st.text_input("Panjang", value=2))
        lebar = float(st.text_input("Lebar", value=3))
        st.write('## **Hasil Penyelesaian**')
        luas = math.pi*panjang*lebar/4
        keliling = math.pi*np.sqrt(panjang**2+lebar**2)
        st.write(f"Luas = {fungsi(luas)} {fsatuan(sat,2)}")
        st.write(f"Keliling = {fungsi(keliling)} {fsatuan(sat,1)}")

if geometri == geometri_list[1]:
    st.write('**Bangun Ruang** adalah bangun yang 3 dimensi dalam geometri. Terdapat satuan panjang, lebar dan tinggi.')
    st.write('Volume adalah melihat isi bangun ruang. Sedangkan Luas Permukaan adalah luas di permukaan bangun ruang, berdasarkan jaring-jaring bangun ruang.')

    bentuk_list = ["Kubus", "Balok", "Prisma", "Limas", "Bola", "Elipsoid"]
    bentuk = st.selectbox(f"Pilih jenis {geometri}:", bentuk_list)

    if bentuk == bentuk_list[0]:
        open_image("Kubus.png")
        st.write('**Kubus** dalam bangun ruang adalah ketiga sisi yang sama')
        st.write('### **Rumus**')
        st.write('Volume')
        st.latex(r"V = {sisi}^3")
        st.latex(r"V = s^3 = s\times s\times s")
        st.write('')
        st.write('Luas Permukaan')
        st.latex(r"L = 6s^2")

        st.write('### **Input**')
        sisi = float(st.text_input("Sisi", value=2))
        st.write('## **Hasil Penyelesaian**')
        volume = sisi**3
        luas_permukaan = 6*sisi**2
        diagonal = np.sqrt(3)*sisi
        st.write(f"Volume = {fungsi(volume)} {fsatuan(sat,3)}")
        st.write(f"Luas Permukaan = {fungsi(luas_permukaan)} {fsatuan(sat,2)}")
        st.write(f"Diagonal = {fungsi(diagonal)} {fsatuan(sat,1)}")

    if bentuk == bentuk_list[1]:
        open_image("Balok.png")
        st.write('**Balok** adalah ketiga sisi yang terdiri dari panjang (p), lebar (l) dan tinggi (t)')
        st.write('### **Rumus**')
        st.latex(r"V = p\times l\times t")

        st.write('### **Input**')
        col1 = st.columns(2)
        col2 = st.columns(2)
        with col1[0]:
            panjang = float(st.text_input("Panjang", value=2))
        with col1[1]:
            lebar = float(st.text_input("Lebar", value=3))
        with col2[0]:
            tinggi = float(st.text_input("Tinggi", value=4))
        
        st.write('## **Hasil Penyelesaian**')
        volume = panjang*lebar*tinggi
        luas_permukaan = 2*(panjang*lebar+panjang*tinggi+lebar*tinggi)
        diagonal = np.sqrt(panjang**2+lebar**2+tinggi**2)
        st.markdown(f"Volume = {fungsi(volume)} {fsatuan(sat,3)}")
        st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)} {fsatuan(sat,2)}")
        st.markdown(f"Diagonal = {fungsi(diagonal)} {fsatuan(sat,1)}")
        st.write('## **Langkah Penyelesaian**')
        with st.expander("Tampilkan"):
            st.write("""
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)
            st.image("https://static.streamlit.io/examples/dice.jpg")

    if bentuk == bentuk_list[2]:
        open_image("Prisma Segitiga.jpg")
        st.write('**Prisma** adalah alas atas dan bawah yang sama. Jenis prisma adalah Prisma Segitiga, Prisma Segiempat (Kubus), dan Tabung.')
        st.write('Volume prisma sama dengan luas alas dikali tinggi prisma.')
        st.write('### **Rumus Prisma**')
        st.latex(r"V_{prisma} = L_{alas} \times tinggi prisma")
        st.latex(r"V_{prisma} = L_{alas} \times t_p")
        bangun_list = ["Prisma Segitiga", "Tabung"]
        bangun = st.selectbox(f"Pilih jenis {bentuk}:", bangun_list)
    
        if bangun == bangun_list[0]:
            open_image("Prisma Segitiga.jpg")
            st.write('### **Rumus**')
            st.latex(r"V_{p△} = \frac{a\times t}{2} \times t_p")

            st.write('### **Input**')
            col1 = st.columns(2)
            col2 = st.columns(2)
            with col1[0]: alas = float(st.text_input("Alas", value=2))
            with col1[1]: tinggi = float(st.text_input("Tinggi", value=3))
            with col2[0]: tinggi_prisma = float(st.text_input("Tinggi Prisma", value=4))

            st.write('## **Hasil Penyelesaian**')
            volume = 1/2*alas*tinggi*tinggi_prisma
            st.markdown(f"Volume = {fungsi(volume)} {fsatuan(sat,3)}")
        else:
            open_image("tabung.png")
            st.write('**Tabung** bisa disebut juga dengan Prisma Lingkaran')
            st.write('### **Rumus**')
            st.latex(r"L_{tabung} = L_{p⊙} = \pi r^2 \times t_p")

            st.write('### **Input**')
            col = st.columns(2)
            with col[0]: radius = float(st.text_input("Radius", value=2))
            with col[1]: tinggi_prisma = float(st.text_input("Tinggi Prisma", value=3))

            st.write('## **Hasil Penyelesaian**')
            diameter = 2*radius
            volume = math.pi*radius**2*tinggi_prisma
            luas_permukaan = 2*math.pi*radius*(radius+tinggi_prisma)
            st.markdown(f"Diameter = {fungsi(diameter)} {fsatuan(sat,1)}")
            st.markdown(f"Volume = {fungsi(volume)} {fsatuan(sat,3)}")
            st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)} {fsatuan(sat,2)}")

    if bentuk == bentuk_list[3]:
        open_image("Limas Segiempat.png")
        st.write('### **Rumus Limas**')
        st.latex(r"V_{limas} = \frac{1}{3} \times L_{alas} \times tinggi prisma")
        st.latex(r"V_{limas} = \frac{1}{3} \times L_{alas} \times t_p")
        bangun_list = ["Limas Segitiga", "Limas Segiempat", "Kerucut"]
        bangun = st.selectbox(f"Pilih jenis {bentuk}:", bangun_list)
        if bangun == bangun_list[0]:
            open_image("Limas Segitiga.png")
            st.write('### **Rumus**')
            st.write('[Coming Soon]')
            st.write('### **Input**')
            col1 = st.columns(2)
            col2 = st.columns(2)
            with col1[0]: alas = float(st.text_input("Alas", value=2))
            with col1[1]: tinggi = float(st.text_input("Tinggi", value=3))
            with col2[0]: tinggi_limas = float(st.text_input("Tinggi Limas", value=4))
            st.write('## **Hasil Penyelesaian**')
            volume = 1/6*alas*tinggi*tinggi_limas
            st.markdown(f"Volume = {fungsi(volume)} {fsatuan(sat,3)}")
        elif bangun == bangun_list[1]:
            open_image("Limas Segiempat.png")
            st.write('### **Rumus**')
            st.write('[Coming Soon]')
            st.write('### **Input**')
            col1 = st.columns(2)
            col2 = st.columns(2)
            with col1[0]: panjang = float(st.text_input("Panjang", value=2))
            with col1[1]: lebar = float(st.text_input("Lebar", value=3))
            with col2[0]: tinggi_limas = float(st.text_input("Tinggi Limas", value=4))
            st.write('## **Hasil Penyelesaian**')
            volume = 1/3*panjang*lebar*tinggi_limas
            luas_permukaan = panjang*lebar+panjang*np.sqrt(lebar**2/4+tinggi_limas**2)+lebar*np.sqrt(panjang**2/4+tinggi_limas**2)
            st.markdown(f"Volume = {fungsi(volume)} {fsatuan(sat,3)}")
            st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)} {fsatuan(sat,2)}")
        else:
            open_image("Kerucut.png")
            st.write('### **Rumus**')
            st.write('[Coming Soon]')
            st.write('### **Input**')
            col = st.columns(2)
            with col[0]: radius = float(st.text_input("Radius", value=2))
            with col[1]: tinggi_prisma = float(st.text_input("Tinggi Limas", value=3))
            st.write('## **Hasil Penyelesaian**')
            diameter = 2*radius
            volume = 1/3*math.pi*radius**2*tinggi_prisma
            luas_permukaan = math.pi*radius**2+2*math.pi*radius*np.sqrt(radius**2+tinggi_prisma**2)
            st.markdown(f"Diameter = {fungsi(diameter)} {fsatuan(sat,1)}")
            st.markdown(f"Volume = {fungsi(volume)} {fsatuan(sat,3)}")
            st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)} {fsatuan(sat,2)}")

    if bentuk == bentuk_list[4]:
        open_image("sphere.jpg")
        st.write('**Bola** adalah bangun ruang yang melengkung dan tidak punya sisi.')
        st.write('### **Rumus**')
        st.latex(r"V = \frac{4}{3} \times pi \times radius^3")
        st.latex(r"V = \frac{4}{3} \pi r^3")
        st.latex(r"L = 4\pi r^2")

        st.write('### **Input**')
        radius = float(st.text_input("Radius", value=2))
        st.write('## **Hasil Penyelesaian**')
        diameter = 2*radius
        volume = 4/3*math.pi*radius**3
        luas_permukaan = 4*math.pi*radius**2
        st.markdown(f"Diameter = {fungsi(diameter)} {fsatuan(sat,1)}")
        st.markdown(f"Volume = {fungsi(volume)} {fsatuan(sat,3)}")
        st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)} {fsatuan(sat,2)}")

    if bentuk == bentuk_list[5]:
        st.write('### **Rumus**')
        st.latex(r"V = \pi \times p \times l \times t")
        st.latex(r"L \approx \pi \times (p^2+l^2+t^2)")
        st.write('### **Input**')
        col1 = st.columns(2)
        col2 = st.columns(2)
        with col1[0]: panjang = float(st.text_input("Panjang", value=2))
        with col1[1]: lebar = float(st.text_input("Lebar", value=3))
        with col2[0]: tinggi = float(st.text_input("Tinggi", value=4))
        st.write('## **Hasil Penyelesaian**')
        volume = 1/6*math.pi*panjang*lebar*tinggi
        luas_permukaan = math.pi*(panjang**2+lebar**2+tinggi**2)
        st.markdown(f"Volume = {fungsi(volume)} {fsatuan(sat,3)}")
        st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)} {fsatuan(sat,2)}")

if geometri == geometri_list[2]:
    bentuk_list = ["Sudut Penyiku", "Sudut Pelurus", "Sudut 360 derajat"]
    bentuk = st.selectbox(f"Pilih jenis {geometri}:", bentuk_list)

    if bentuk == bentuk_list[0]:
        sudut = float(st.text_input("Sudut", value=20))
        sudut_2 = 90 - sudut
        st.markdown(f"Sudut Penyiku = {round(sudut_2, 3)}")

    elif bentuk == bentuk_list[1]:
        sudut = float(st.text_input("Sudut", value=20))
        sudut_2 = 180 - sudut
        st.markdown(f"Sudut Pelurus = {round(sudut_2, 3)}")

    else:
        sudut = float(st.text_input("Sudut", value=20))
        sudut_2 = 360 - sudut
        st.markdown(f"Sudut 360 derajat = {round(sudut_2, 3)}")
    
if geometri == geometri_list[3]:
    bentuk_list = ["2 Sumbu", "3 Sumbu", "Tegak Lurus"]
    bentuk = st.selectbox(f"Pilih jenis {geometri}:", bentuk_list)

    if bentuk == bentuk_list[0]:
        st.write('Input bulat')
        st.write('### **Rumus**')
        st.latex(r'a^2+b^2=c^2')
        st.write('### **Input**')
        col = st.columns(2)
        with col[0]: a = int(st.text_input("Sisi a", value=12))
        with col[1]: b = int(st.text_input("Sisi b", value=5))

        st.write('## **Hasil Penyelesaian**')

        st.latex(fr"{a}^2+{b}^2 = {a**2+b**2}")
        st.latex(fr"c^2 = {a**2+b**2}")

        c = (a**2+b**2)**0.5

        if c == round(c, 10):
            st.latex(fr"c = \sqrt{{{a**2+b**2}}} = {fungsi(c)}")
        else:
            st.latex(fr"c = \sqrt{{{a**2+b**2}}}")

        if check1:
            st.write('## **Hasil Gambar**')

            draw.text((20,20), 'Pythagoras', fill='white', font=roboto(60))

            xa = 100
            ya = 200
            p = 30
            size = 40

            draw.polygon((xa,ya,xa+p*a,ya,xa,ya+p*b), fill=(32,32,32))
            draw.line((xa,ya,xa+p*a,ya,xa,ya+p*b,xa,ya), fill='white', width=2)
            for a1 in range(1,a):
                draw.line((xa+p*a1,ya,xa+p*a1,ya+p//3), fill='white', width=2)
            for b1 in range(1,b):
                draw.line((xa,ya+p*b1,xa+p//3,ya+p*b1), fill='white', width=2)
            for c1 in range(1,int(c+0.500001)):
                draw.line((xa+p*(a-a/c*c1),ya+p*b/c*c1,xa+p*(a-a/c*c1)-p//3*b/c,ya+p*b/c*c1-p//3*a/c), fill='white', width=2)
            draw.text((xa+p//2*a,ya-(3*size)//4), str(a), fill='white', font=roboto(size), anchor='mm')
            draw.text((xa-(3*size)//4,ya+p//2*b), str(b), fill='white', font=roboto(size), anchor='mm')
            draw.text((xa+p//2*a+30*b/c,ya+p//2*b+30*a/c), str(fungsi(c)), fill=(128,255,128), font=roboto(size), anchor='mm')

            draw.line((xa+p*(a+b)+50,ya,xa+p*(a+b)+50,ya+p*(a+b)), fill=(255,255,128), width=2)
            draw.line((xa+p*(a+b)+40,ya,xa+p*(a+b)+60,ya), fill=(255,255,128), width=2)
            draw.line((xa+p*(a+b)+40,ya+p*(a+b),xa+p*(a+b)+60,ya+p*(a+b)), fill=(255,255,128), width=2)
            draw.text((xa+p*(a+b)+70,ya+p//2*(a+b)), str(a+b), fill=(128,255,128), font=roboto(size), anchor='lm')

            draw.polygon((xa+p*a,ya,xa+p*(a+b),ya,xa+p*(a+b),ya+p*a), fill=(32,32,32))
            draw.line((xa+p*a,ya,xa+p*(a+b),ya,xa+p*(a+b),ya+p*a,xa+p*a,ya), fill='white', width=2)
            draw.polygon((xa+p*(a+b),ya+p*a,xa+p*(a+b),ya+p*(a+b),xa+p*b,ya+p*(a+b)), fill=(32,32,32))
            draw.line((xa+p*(a+b),ya+p*a,xa+p*(a+b),ya+p*(a+b),xa+p*b,ya+p*(a+b),xa+p*(a+b),ya+p*a), fill='white', width=2)
            draw.polygon((xa+p*b,ya+p*(a+b),xa,ya+p*(a+b),xa,ya+p*b), fill=(32,32,32))
            draw.line((xa+p*b,ya+p*(a+b),xa,ya+p*(a+b),xa,ya+p*b,xa+p*b,ya+p*(a+b)), fill='white', width=2)

            # draw.line((xa,ya+100*b), fill='white', width=2)
            
            luas = a*b/2
            diagonal = c
            keliling = a+b+diagonal

            # draw.text((20,860), f"Luas: {fungsi(luas)}\nKeliling: {fungsi(keliling)}", fill='white', font=roboto(50))

            # im.save("output.png")
            im.save("preview.png")
            st.image("preview.png")

if geometri == geometri_list[4]:
    st.write('## **Definisi dan Penjelasan**')

    st.write("Geometri adalah bangun yang punya sisi, luas, dan volume. Ada banyak jenis geometri dan bisa melihat gambarnya.")
    st.write('Geometri adalah cabang matematika yang mempelajari tentang bentuk, ukuran, posisi, dan sifat-sifat ruang. Dalam geometri, kita mempelajari tentang objek-objek seperti titik, garis, bidang, sudut, dan bangun ruang seperti kubus, bola, dan prisma. Geometri juga melibatkan penggunaan konsep matematika seperti koordinat, persamaan, dan transformasi untuk memahami dan menganalisis objek-objek geometris. Geometri sangat penting di banyak bidang, termasuk fisika, arsitektur, teknik, dan ilmu komputer.')
    st.write("Luas dan Keliling")
    st.write('Bilangan pi (π) kira-kira 3.14 atau 22/7. Konstanta pi (π) = 3.14159... Bilangan pi adalah bilangan irasional, juga bilangan ?????. Ia juga termasuk')

# st.write('## **Hasil Persamaan**')

# f"baca {angka}" = "baca " + str(angka)
# print = st.write
