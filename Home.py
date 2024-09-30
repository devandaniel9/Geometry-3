# Title

# List import
import numpy as np
import math
import streamlit as st

# from PIL import Image
from PIL import Image, ImageDraw, ImageFont

# Menjalankan program
# streamlit run 'Geometri 4 - 3.py'
# streamlit run Home.py

# @import fonts/Roboto-Regular.ttf;

st.set_page_config(
    page_title="Geometri 4",
    page_icon="🧊",
)

aaa = """
<style>
	@import fonts/Roboto-Regular.ttf;

	html, body, [class*="css"]  {
	font-family: 'Roboto', sans-serif;
	}

    [data-testid="stSidebar"] {
        background-color: #ffffff20;
    }
</style>
"""

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
        background-color: rgb(0,0,0,0);
    }
</style>
"""

st.markdown(streamlit_style, unsafe_allow_html=True)

def color(text, c):
    return f"<font color={c}>{text}</font>"

# st.write(f"The next word is {color('red','yellow')}", unsafe_allow_html=True)

def stw(text):
    return st.markdown(text, unsafe_allow_html=True)

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

# Streamlit
# st.write("""# Geometri 3""")
# st.write('# :red[Program Geometri]')
# st.markdown("# <u><font color='yellow'>Program Geometri</font></u>", unsafe_allow_html=True)
st.markdown("# <font color='#ffd080'>Program Geometri</font> 🧊", unsafe_allow_html=True)

# -----

# stw(color('Dibuat oleh','#ffb0a0'))
# st.write('#### **Dibuat oleh Devan Daniel - Kelas 9**')

# open_image("geometry.jpg", 700)

# color = #204884

st.write('**Made by Devan Daniel - Kelas 9**')
st.write('')
stw(f"**{color('Geometri','#d0ff80')}** adalah bangun yang punya sisi, luas, dan volume. Ada banyak jenis geometri dan bisa melihat gambarnya.")
# st.text('Link')
st.markdown('''
Ada beberapa fitur di program ini, yaitu:
- Program Geometri terdiri dari Bangun Datar, Bangun Ruang, Sudut, dan Pythagoras
- Program ini dapat menampilkan langkah penyelesaian dan grafik solusi dari soal
- Silahkan masukkan jenis persamaan dan input di menu bawah
- Agar bisa melihat informasi, klik tombol informasi program ini

Version: 1.6<br>
Last updated: 30 Sept 2024 (Untuk dapat mengakses link ini)<br>
Last updated: 18 Mei 2023 (Perubahan isi program ini)

<style>
.myDiv {
  background-color: #185476;
  padding: 10px;
}
</style>
<div class="myDiv">
<font size=4><b>Link:</b></font>
<br>
Link website saya:<br>
<a href=https://devandaniel9.github.io/index.html>Website Saya</a><br>
Link program Equation Solver:<br>
<a href=https://devandaniel9-equation-solver-4.streamlit.app/>Equation Solver</a><br>
Link bangun datar dan bangun ruang: (Program Lama)<br>
<a href=https://devandaniel9-shape-program-devan-7zwso4.streamlit.app/>Bangun Datar dan Bangun Ruang</a>
</div><br>
''', unsafe_allow_html=True)

side = '''with st.sidebar:
    st.write("\n\nHahaha hihihi")'''

def add_bg_from_local(image_file):
    import base64
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
# add_bg_from_local('background.jpg')

st.write('## **Pengaturan**')

# lisp = line_split

def lisp(baris):
    hasil = baris.split(' ')
    return hasil[-1]

def check(text):
    if text == 'True' or text == 'true': return True
    else: return False

file = open("data.txt", "r")
baris = file.readlines()

# st.write(f"Hasil: {lisp(baris[3])}")
satuan_list_index = int(lisp(baris[0]))
satuan2_list_index = int(lisp(baris[1]))
digit_default = int(lisp(baris[2]))
step_check = check(lisp(baris[3]))
# st.write(bool('hahaha'))
step2_check = check(lisp(baris[4]))
check1_default = check(lisp(baris[5]))

st.write('### **Satuan**')
col = st.columns(2)
satuan_list = ['Tidak ada', 'Centimeter (cm)', 'Meter (m)', 'Inci (in)']
with col[0]: satuan = st.radio('Pilih satuan', satuan_list, index=satuan_list_index)
# satuan = 'Tidak ada'
if satuan == satuan_list[0]: sat = ''
elif satuan == satuan_list[1]: sat = 'cm'
elif satuan == satuan_list[2]: sat = 'm'
else: sat = 'in'

st.write(satuan_list.index(satuan))

satuan2_list = ['cm^2', 'cm2', 'cm²', 'cm kuadrat']
if satuan != satuan_list[0]: 
    # satuan2_list = [f'{sat}^2', f'{sat}2', f'{sat}²']
    # satuan2_list = ['cm^2', 'cm2', 'cm²', 'cm kuadrat']
    with col[1]: satuan2 = st.radio('Pilih bentuk satuan', satuan2_list, index=satuan2_list_index)
else:
    satuan2 = 'cm^2'

st.write('')

st.write('### **Digit Precision**')
digit = int(st.slider("Digit (2-10)", value=digit_default, min_value=2, max_value=10))
st.write('')

st.write('### **Langkah Penyelesaian**')
st.write('Langkah Penyelesaian bertujuan untuk menjelaskan bagaimana cara menyelesaikan soal-soal dengan langkah-langkah di bawahnya.')
step = st.checkbox('Langkah Penyelesaian (Coming Soon)', value=step_check)
if step:
    step2 = '''step_list = ['Tidak ada penjelasan', 'Dengan penjelasan']
    step = st.radio('Pilih opsi', step_list)
    step_check'''
    step2 = st.checkbox(label="Dengan penjelasan (Coming Soon)", value=step2_check)
else:
    step2 = False
st.write('')

st.write('### **Hasil Gambar**')
check1 = st.checkbox('Hasil Gambar', value=check1_default)
st.write('')

# st.write('### **Lanjutan**')
# st.write('[Coming Soon]')
st.write('### **Reset**')
st.write('Reset Settings untuk mengembalikan pengaturan ke semula')
reset = st.button('Reset Settings', key='RunBtn', on_click=None)
if reset:
    file = open("data_default.txt", "r")
    baris = file.readlines()
    # st.write(baris)
    # st.write(lisp(baris[0]))
    file2 = open("data.txt", "w")
    teks = f"""satuan_list_index: {lisp(baris[0])}satuan2_list_index: {lisp(baris[1])}digit_default: {lisp(baris[2])}step_check: {lisp(baris[3])}step2_check: {lisp(baris[4])}check1_default: {lisp(baris[5])}
    """
    file2.write(teks)

st.write('')

st.write('## **Jenis Geometri**')

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

# st.write('')
geometri_list = ["Bangun Datar", "Bangun Ruang", "Sudut", "Pythagoras", "Transformasi", "Definisi"]
geometri = st.selectbox("Pilih jenis Geometri:", geometri_list)

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
            if satuan2 == satuan2_list[0]: return f' {satuan}^{power}'
            elif satuan2 == satuan2_list[1]: return f' {satuan}{power}'
            elif satuan2 == satuan2_list[2]:
                if power == 2: return f' {satuan}²'
                else: return f' {satuan}³'
            else:
                if power == 2: return f' {satuan} kuadrat'
                else: return f' {satuan} kubik'
    return ''

teks = f"""satuan_list_index: {satuan_list.index(satuan)}
satuan2_list_index: {satuan2_list.index(satuan2)}
digit_default: {digit}
step_check: {step}
step2_check: {step2}
check1_default: {check1}
"""

# st.write(teks)

file = open("data.txt", "w")
file.write(teks)
file = open("data.txt", "r")

# st.write('a')
