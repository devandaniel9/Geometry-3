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
st.markdown("# <font color='#ffd080'>Bangun Ruang</font>", unsafe_allow_html=True)
st.write('**Bangun Datar dari Program Geometri**')
st.write('')

col = st.columns(2)
with col[0]: open_image("3d-shapes.png")
with col[1]: st.write('**Bangun Ruang** adalah bangun yang 3 dimensi dalam geometri. Terdapat satuan panjang, lebar dan tinggi.')
st.write('Volume adalah melihat isi bangun ruang. Sedangkan Luas Permukaan adalah luas di permukaan bangun ruang, berdasarkan jaring-jaring bangun ruang.')
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
elif satuan_index == 1: sat = 'cm'
elif satuan_index == 2: sat = 'm'
else: sat = 'in'

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

geometri = 'Bangun Ruang'

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

    st.write('### **Pertanyaan**')
    with st.expander("Mengapa tidak ada Prisma Segiempat?"):
        """
        Seperti yang sudah tau, prisma adalah kedua alas yang sama, maka selimut prisma berbentuk persegi
        Karena Prisma Segiempat dalam bentuk prisma alasnya segiempat atau persegi,
        maka Prisma Segiempat disebut juga Kubus.
        """

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