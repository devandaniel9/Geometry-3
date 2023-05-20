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
st.markdown("# <font color='#ffd080'>Sudut</font>", unsafe_allow_html=True)
st.write('**Sudut dari Program Geometri**')
st.write('')

col = st.columns(2)
with col[0]: open_image("angle.png")
with col[1]: st.write('**Sudut** adalah blablabla. Sudut terbentuk ketika dua garis berpotongan pada satu titik.')
st.write('Luas Bangun Datar adalah melihat keseluruhan bangun datar. Sedangkan Keliling Bangun Datar adalah keliling pada pinggir bangun tersebut.')
st.write('Simbol Luas adalah L dan Keliling adalah K')

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

geometri = 'Sudut'

bentuk_list = ["Penjelasan", "Sudut Penyiku", "Sudut Pelurus", "Sudut 360 derajat", "Gambar"]
bentuk = st.selectbox(f"Pilih jenis {geometri}:", bentuk_list)

if bentuk == bentuk_list[0]:
    st.markdown('[Coming Soon]')

if bentuk == bentuk_list[1]:
    sudut = int(st.text_input("Sudut", value=20))
    sudut_2 = 90 - sudut
    st.markdown(f"Sudut Penyiku = {round(sudut_2, 3)}")

if bentuk == bentuk_list[2]:
    sudut = int(st.text_input("Sudut", value=20))
    sudut_2 = 180 - sudut
    st.markdown(f"Sudut Pelurus = {round(sudut_2, 3)}")

if bentuk == bentuk_list[3]:
    sudut = int(st.text_input("Sudut", value=20))

    st.write('## **Hasil Penyelesaian**')

    sudut_2 = 360 - sudut
    st.markdown(f"Sudut 360 derajat = {round(sudut_2, 3)}")

if bentuk == bentuk_list[4]:
    # sudut = int(st.text_input("Sudut", value=30))
    sudut = int(st.number_input("Sudut (0-360)", value=30, min_value=0, max_value=360))

    st.write('## **Pengaturan**')

    st.write('### **Busur**')

    # with col[0]: satuan = st.radio('Pilih satuan', satuan_list, index=satuan_list_index)
    st.write('Tampilkan busur')
    check2 = st.checkbox("Busur")

    if check2:
        busur_list = ['Busur penuh', 'Busur setengah']
        busur = st.radio('Pilih jenis busur', busur_list)
        busur_index = busur_list.index(busur)
    else:
        busur_index = 0

    resolution = 1000

    im = Image.new('RGB', (resolution,resolution))
    # draw = ImageDraw.Draw(im)
    draw = ImageDraw.Draw(im, 'RGBA')

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
    
    if check2:
        if busur_index == 0:
            jumlah_a = 36
        else:
            jumlah_a = 18

        for a in range(jumlah_a):
            for b in range(10):
                if b > 0:
                    draw.line((500-370*np.cos(np.deg2rad(10*a+b)),500-370*np.sin(np.deg2rad(10*a+b)),500-397*np.cos(np.deg2rad(10*a+b)),500-397*np.sin(np.deg2rad(10*a+b))), fill=(64,64,64), width=2)
            draw.pieslice((100,100,900,900), start=-10*(a+1), end=-10*a, outline=(96,96,96), width=3)

        for a in range(jumlah_a):
            draw.text((500-350*np.cos(10*a*np.pi/180),500-350*np.sin(10*a*np.pi/180)), str(10*a), fill='yellow', font=roboto(20), anchor='mm')

        if busur_index != 0:
            a = 18
            draw.text((500+350*np.cos(10*a*np.pi/180),500-350*np.sin(10*a*np.pi/180)), str(10*a), fill='yellow', font=roboto(20), anchor='mm')

    st.write('### **Sudut**')

    check3 = st.checkbox("Sudut ABC")
    check4 = st.checkbox("Juring ABC")

    if check4:
        draw.pieslice((100,100,900,900), start=180, end=180+sudut, fill=(255,255,255,64), width=3)
    
    draw.line((500,500,100,500), fill='white', width=4)
    draw.line((500,500,500-400*np.cos(sudut*np.pi/180),500-400*np.sin(sudut*np.pi/180)), fill='white', width=4)
    
    draw.pieslice((450,450,550,550), start=180, end=180+sudut, outline='white', width=3)

    if check3:
        draw.text((70,500), 'A', fill=(128,255,128), font=roboto(40), anchor='mm')
        if sudut < 5: sudut2 = 5
        elif sudut < 355: sudut2 = sudut
        else: sudut2 = 355
        draw.text((500-430*np.cos(sudut2*np.pi/180),500-430*np.sin(sudut2*np.pi/180)), 'C', fill=(128,255,128), font=roboto(40), anchor='mm')
        if sudut <= 180:
            draw.text((500+40*np.cos(sudut/2*np.pi/180),500+40*np.sin(sudut/2*np.pi/180)), 'B', fill=(128,255,128), font=roboto(40), anchor='mm')
        else:
            draw.text((500-80*np.cos(sudut/2*np.pi/180),500-80*np.sin(sudut/2*np.pi/180)), 'B', fill=(128,255,128), font=roboto(40), anchor='mm')
    
    draw.text((20,20), 'Sudut', fill='white', font=roboto(60))
    draw.text((20,100), f"Derajat: {sudut}°", fill='white', font=roboto(40))

    if sudut == 0: teks = 'Tidak Mempunyai Sudut'
    elif sudut < 90: teks = 'Sudut Lancip'
    elif sudut == 90: teks = 'Sudut Siku-Siku'
    elif sudut < 180: teks = 'Sudut Tumpul'
    elif sudut == 180: teks = 'Sudut Lurus'
    elif sudut < 360: teks = 'Sudut Refleks'
    elif sudut == 360: teks = 'Sudut Penuh'

    draw.text((20,980), teks, fill='white', font=roboto(40), anchor='lb')

    st.write('## **Gambar**')

    im.save("preview.png")
    # st.image("preview.png", width=500)
    st.image("preview.png", width=650)
    # im.show()

    with open("preview.png", "rb") as file:
        btn = st.download_button(
            label="Download Image",
            data=file,
            # file_name="grafik.png"
            file_name="image.png"
        )