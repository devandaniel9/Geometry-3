# Title

# List import
import numpy as np
import math
import streamlit as st

from PIL import Image

# Menjalankan program
# streamlit run 'Geometri 3 - 2.py'

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

# Streamlit
# st.write("""# Geometri 3""")
# st.write('# :red[Program Geometri]')
st.markdown("# <u><font color='yellow'>Program Geometri</font></u>", unsafe_allow_html=True)
st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',
unsafe_allow_html=True
)

# -----

stw(color('Dibuat oleh','#ffb0a0'))
stw(f"**{color('Geometri','green')}** adalah bangun yang punya sisi, luas, dan volume. Ada banyak jenis geometri dan bisa melihat gambarnya.")
# st.text('Link')
st.write('')

st.write('## **Pengaturan**')
with st.expander("Tampilkan"):
    st.write('### **Satuan**')
    satuan = st.radio('Pilih satuan', ('Tidak ada', 'Centimeter (cm)', 'Meter (m)'))
    st.write('### **Link**')
    st.write('Link program Bangun Datar dan Bangun Ruang:  \nhttps://devandaniel9-shape-program-devan-7zwso4.streamlit.app/')
    st.write('### **Lanjutan**')
    st.write('[Coming Soon]')
    st.write('### **Tentang**')
    st.write('Copyright © ?????')
    st.write('Dibuat oleh Devan Daniel')
st.write('')

st.write('## **Geometri**')
st.write('Program Geometri terdiri dari Bangun Datar, Bangun Ruang, Sudut, dan Pitagoras')
st.checkbox('Langkah Penyelesaian')
st.write('')
geometri_list = ["Bangun Datar", "Bangun Ruang", "Sudut", "Pitagoras"]
geometri = st.selectbox("Pilih jenis Geometri:", geometri_list,)

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

if geometri == geometri_list[0]:
    st.write('**Bangun Datar** adalah bangun yang 2 dimensi dalam geometri. Terdapat satuan panjang dan lebar.')
    st.write('Luas Bangun Datar adalah melihat keseluruhan bangun datar. Sedangkan Keliling Bangun Datar adalah keliling pada pinggir bangun tersebut.')
    st.write('Simbol Luas adalah L dan Keliling adalah K')
    st.write()

    bentuk_list = ["Persegi", "Persegi Panjang", "Jajar Genjang", "Trapesium", "Segitiga", "Segilima", "Lingkaran", "Elips"]
    bentuk = st.selectbox(f"Pilih jenis {geometri}:", bentuk_list)

    if bentuk == bentuk_list[0]:
        open_image("Persegi.png")
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
        st.write(f"Luas = {fungsi(luas)}")
        st.write(f"Keliling = {fungsi(keliling)}")
        st.write(f"Diagonal = {fungsi(diagonal)}")

    if bentuk == bentuk_list[1]:
        open_image("Persegi Panjang.png")
        st.write('**Persegi Panjang** adalah bangun yang terdiri dari dua sisi, yaitu panjang (p) dan lebar (l).')
        st.write('### **Rumus**')
        st.latex(r"L = panjang\times lebar")
        st.latex(r"L▭ = p\times l")
        st.latex(r"K▭ = 2\times (p+l)")

        st.write('### **Input**')
        col1 = st.columns(2)
        with col1[0]: panjang = float(st.text_input("Panjang", value=2))
        with col1[1]: lebar = float(st.text_input("Lebar", value=3))
        st.write('## **Hasil Penyelesaian**')
        luas = panjang*lebar
        keliling = 2*(panjang+lebar)
        diagonal = np.sqrt(panjang**2+lebar**2)
        st.write(f"Luas = {fungsi(luas)}")
        st.write(f"Keliling = {fungsi(keliling)}")
        st.write(f"Diagonal = {fungsi(diagonal)}")

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
        st.write(f"Luas = {fungsi(luas)}")

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
        st.write(f"Luas = {fungsi(luas)}")

    if bentuk == bentuk_list[4]:
        open_image("Segitiga.png")
        st.write('**Segitiga** adalah bangun yang terdiri dari 3 siri, yaitu alas dan 2 sisi miring. Terdapat alas (a) dan tinggi (t)')
        st.write('Ada 4 jenis segitiga, yaitu Segitiga Siku-Siku, Segitiga Sama Sisi, Segitiga Sama Kaki, dan Segitiga Sembarang')
        bangun_list = ["Segitiga Siku-Siku", "Segitiga Sama Sisi", "Segitiga Sama Kaki", "Segitiga Sembarang"]
        bangun = st.selectbox(f"Pilih jenis {bentuk}:", bangun_list)
        if bangun == bangun_list[0]:
            open_image("triangle1.jpg")
            st.write('### **Rumus**')
            st.write('### **Input**')
            alas = float(st.text_input("Alas", value=4))
            tinggi = float(st.text_input("Tinggi", value=3))
            st.write('## **Hasil Penyelesaian**')
            luas = alas*tinggi/2
            st.write(f"Luas = {fungsi(luas)}")
        if bangun == bangun_list[1]:
            open_image("triangle2.png")
            st.write('### **Rumus**')
            st.write('### **Input**')
        if bangun == bangun_list[2]:
            open_image("triangle3.jpg")
            st.write('### **Rumus**')
            st.write('### **Input**')
        if bangun == bangun_list[3]:
            open_image("custom.jpg")
            st.write('### **Rumus**')
            st.write('### **Input**')

    if bentuk == bentuk_list[5]:
        open_image("segilima.jpg")
        st.write('Segilima atau Pentagon adalah bangun yang terdiri dari 5 sisi')
        st.write('### **Rumus**')
        st.write('### **Input**')

    if bentuk == bentuk_list[6]:
        open_image("Lingkaran.png")
        st.write('Lingkaran adalah bangun datar yang berbentuk bulat dan melengkung. Ada hubungannya dengan pi (π)')
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
        st.write(f"Diameter = {fungsi(diameter)}")
        st.write(f"Luas = {fungsi(luas)}")
        st.write(f"Keliling = {fungsi(keliling)}")

    if bentuk == bentuk_list[7]:
        open_image("Elips.png")
        st.write('Elips (ellipse) adalah lingkaran yang lonjong, dengan panjang dan lebar yang berbeda.')
        st.write('### **Rumus**')
        st.latex(r"L = \pi \times p \times l")
        st.latex(r"K \approx \pi \sqrt{p^2+l^2}")

        st.write('### **Input**')
        panjang = float(st.text_input("Panjang", value=2))
        lebar = float(st.text_input("Lebar", value=3))
        st.write('## **Hasil Penyelesaian**')
        luas = math.pi*panjang*lebar/4
        keliling = math.pi*np.sqrt(panjang**2+lebar**2)
        st.write(f"Luas = {fungsi(luas)}")
        st.write(f"Keliling = {fungsi(keliling)}")

if geometri == geometri_list[1]:
    st.write('Bangun Ruang adalah bangun yang 3 dimensi dalam geometri. Terdapat satuan panjang, lebar dan tinggi.')
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
        st.write(f"Volume = {fungsi(volume)}")
        st.write(f"Luas Permukaan = {fungsi(luas_permukaan)}")
        st.write(f"Diagonal = {fungsi(diagonal)}")

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
        st.markdown(f"Volume = {fungsi(volume)}")
        st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)}")
        st.markdown(f"Diagonal = {fungsi(diagonal)}")
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
            st.markdown(f"Volume = {fungsi(volume)}")
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
            st.markdown(f"Diameter = {fungsi(diameter)}")
            st.markdown(f"Volume = {fungsi(volume)}")
            st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)}")

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
            st.markdown(f"Volume = {fungsi(volume)}")
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
            st.markdown(f"Volume = {fungsi(volume)}")
            st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)}")
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
            st.markdown(f"Diameter = {fungsi(diameter)}")
            st.markdown(f"Volume = {fungsi(volume)}")
            st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)}")

    if bentuk == bentuk_list[4]:
        open_image("sphere.jpg")
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
        st.markdown(f"Diameter = {fungsi(diameter)}")
        st.markdown(f"Volume = {fungsi(volume)}")
        st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)}")

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
        st.markdown(f"Volume = {fungsi(volume)}")
        st.markdown(f"Luas Permukaan = {fungsi(luas_permukaan)}")

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

# st.write('## **Hasil Persamaan**')

# f"baca {angka}" = "baca " + str(angka)
# print = st.write
