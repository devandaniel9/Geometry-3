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
st.markdown("# <font color='#ffd080'>Pythagoras</font>", unsafe_allow_html=True)
st.write('**Pythagoras dari Program Geometri**')
st.write('')

col = st.columns(2)
with col[0]: open_image("pythagoras.png")
with col[1]: st.write('**Pythagoras** adalah bangun yang 3 dimensi dalam geometri. Terdapat satuan panjang, lebar dan tinggi.')
st.write('Volume adalah melihat isi bangun ruang. Sedangkan Luas Permukaan adalah luas di permukaan bangun ruang, berdasarkan jaring-jaring bangun ruang.')
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

geometri = 'Pythagoras'

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