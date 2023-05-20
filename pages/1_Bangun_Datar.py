# Title

# List import
import numpy as np
import math
import streamlit as st

# from PIL import Image
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(
    page_title="Geometri 4",
    page_icon="🧊",
)

streamlit_style = """
<style>
	@import fonts;

	[class*="css"]  {
	font-family: 'FreeSans';
	}

    .katex-html {
        text-align: left;
    }

    [data-testid=stSidebar] {
        background-color: #ffffff20;
    }

    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }

    div[role="listbox"] ul {
        background-color: red;
    }
</style>
"""

st.markdown(streamlit_style, unsafe_allow_html=True)

# Buka gambar
# oi = open image
def open_image(nama):
    try:
        img2 = Image.open(f'images/{nama}')
        wid, hgt = img2.size
        # im = Image.new('RGB', (resolution,resolution))
        img = Image.new('RGB', size=(wid,hgt), color='white')
        draw = ImageDraw.Draw(img)
        # img = Image.open(f"{bentuk}.png")
        img.paste(img2)
        # st.image(img, width=200)
        st.image(img, width=320)
    except FileNotFoundError:
        img = ""

# st.markdown("# <font color='#ffd080'>Program Geometri</font> 🧊", unsafe_allow_html=True)
# st.write('# Bangun Datar')
st.markdown("# <font color='#ffd080'>Bangun Datar</font>", unsafe_allow_html=True)
st.write('**Bangun Datar dari Program Geometri**')
st.write('')

col = st.columns(2)
with col[0]: open_image("2d-shapes.png")
with col[1]: st.write('**Bangun Datar** adalah bangun yang 2 dimensi dalam geometri. Terdapat satuan panjang dan lebar.')
st.write('Luas Bangun Datar adalah melihat keseluruhan bangun datar. Sedangkan Keliling Bangun Datar adalah keliling pada pinggir bangun tersebut.')
st.write('Simbol Luas adalah L dan Keliling adalah K')
st.write()

def lisp(baris):
    hasil = baris.split(' ')
    return hasil[-1]

def check(text):
    if text == 'True' or text == 'true': return True
    else: return False

file = open("data.txt", "r")
baris = file.readlines()

satuan_index = int(lisp(baris[0]))
if satuan_index == 0: sat = ''
if satuan_index == 1: sat = 'cm'
if satuan_index == 2: sat = 'm'
if satuan_index == 3: sat = 'in'
satuan2_index = int(lisp(baris[1]))
digit = int(lisp(baris[2]))
step_check = check(lisp(baris[3]))
# st.write(bool('hahaha'))
step2_check = check(lisp(baris[4]))
check1 = check(lisp(baris[5]))

# digit = 3
def fungsi(angka):
    a = round(angka, digit)
    if round(angka, digit) == round(angka, 0):
        angka = int(a)
    else:
        angka = a
   
    return angka

# print(fungsi(3.99999999))

def fsatuan(satuan, power):
    if satuan != '':
        if power <= 1: return f'{satuan}'
        else:
            # satuan2_list = ['cm^2', 'cm2', 'cm²']
            if satuan2_index == 0: return f' {satuan}^{power}'
            elif satuan2_index == 1: return f' {satuan}{power}'
            elif satuan2_index == 2:
                if power == 2: return f' {satuan}²'
                else: return f' {satuan}³'
            else:
                if power == 2: return f' {satuan} kuadrat'
                else: return f' {satuan} kubik'
    return ''

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

geometri = 'Bangun Datar'

bentuk_list = ["Persegi", "Persegi Panjang", "Jajar Genjang", "Trapesium", "Segitiga", "Lingkaran", "Segilima", "Segienam", "Elips", "Gabungan"]
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
    sisi = float(st.text_input("Sisi", value=2, help='Masukkan sisi'))
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

if bentuk == bentuk_list[6]:
    open_image("segilima.jpg")
    st.write('**Segilima** atau Pentagon adalah bangun yang terdiri dari 5 sisi')
    st.write('### **Rumus**')
    st.write('### **Input**')

if bentuk == bentuk_list[7]:
    open_image("segienam.jpg")
    st.write('**Segienam** atau Hexagon adalah bangun yang terdiri dari 6 sisi')
    st.write('### **Rumus**')
    st.write('### **Input**')

if bentuk == bentuk_list[8]:
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