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
# add_bg_from_local('background2.jpg')

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
st.markdown("# <font color='#ffd080'>Transformasi</font>", unsafe_allow_html=True)
st.write('**Transformasi dalam Geometri**')
st.write('')

col = st.columns(2)
with col[0]: open_image("transformation.png")
with col[1]: st.write('**Transformasi** adalah bangun yang 2 dimensi dalam geometri. Terdapat satuan panjang dan lebar.')

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

# nama_list = ["Translation","Reflection","Dilation","Rotation","Kesebangunan","Bangun Datar"]
nama_list = ["Translasi","Refleksi","Dilatasi","Rotasi","Kesebangunan","Bangun Datar"]
nama = st.selectbox("Pilih jenis Transformasi:", nama_list)

st.write(f'### **{nama}**')
if nama == nama_list[0]:
    col = st.columns(2)
    with col[0]: open_image("translation.png")
    with col[1]:
        # stw(f"<font size='5'><b>{bentuk}</b></font>")
        st.write('**Translasi** dalam transformasi adalah blablabla.')
        st.write('Disini akan mencari Luas dan Keliling persegi')

    st.write('### **Rumus**')
    st.latex(r"A(x,y) \rightarrow A'(x+x_1,y+y_1)")
    
    st.write('### **Input**')
    col1 = st.columns(2)
    col2 = st.columns(2)
    with col1[0]: x = float(st.text_input("x", value=3))
    with col1[1]: y = float(st.text_input("y", value=4))
    with col2[0]: x1 = float(st.text_input("x1", value=2))
    with col2[1]: y1 = float(st.text_input("y1", value=3))
    
    xa = x+x1
    ya = y+y1
    st.write('## **Hasil Penyelesaian**')
    st.latex(fr"A({fungsi(x)},{fungsi(y)}) \rightarrow A'({fungsi(xa)},{fungsi(ya)})")

if nama == nama_list[1]:
    col = st.columns(2)
    with col[0]: open_image("reflection.png")

    st.write('### **Rumus**')
    st.latex(r"A(x,y) \rightarrow A'(2x_1-x,2y_1-y)")

    st.write('### **Input**')
    col1 = st.columns(2)
    col2 = st.columns(2)
    with col1[0]: x = float(st.text_input("x", value=3))
    with col1[1]: y = float(st.text_input("y", value=4))
    with col2[0]: x1 = float(st.text_input("x1", value=2))
    with col2[1]: y1 = float(st.text_input("y1", value=3))
    xa = 2*x1-x
    ya = 2*y1-y
    st.write('## **Hasil Penyelesaian**')
    st.latex(fr"A({fungsi(x)},{fungsi(y)}) \rightarrow A'({fungsi(xa)},{fungsi(ya)})")

if nama == nama_list[2]:
    col = st.columns(2)
    with col[0]: open_image("dilation.png")

    st.write('### **Rumus**')
    st.latex(r"A(x,y) \rightarrow A'(k(x-x_1)-x,k(y-y_1)-y)")

    st.write('### **Input**')
    col1 = st.columns(2)
    col2 = st.columns(2)
    col3 = st.columns(2)
    # 2,1,4,2,3
    with col1[0]: x = float(st.text_input("x", value=2))
    with col1[1]: y = float(st.text_input("y", value=1))
    with col2[0]: x1 = float(st.text_input("x1", value=4))
    with col2[1]: y1 = float(st.text_input("y1", value=2))
    with col3[0]: k = float(st.text_input("k", value=3))
    xa = k*(x-x1)+x1
    ya = k*(y-y1)+y1
    st.write('## **Hasil Penyelesaian**')
    st.latex(fr"A({fungsi(x)},{fungsi(y)}) \rightarrow A'({fungsi(xa)},{fungsi(ya)})")

if nama == nama_list[3]:
    col = st.columns(2)
    with col[0]: open_image("rotation.png")

    st.write('### **Input**')
    col1 = st.columns(2)
    col2 = st.columns(2)
    with col1[0]: x = float(st.text_input("x", value=3))
    with col1[1]: y = float(st.text_input("y", value=4))
    with col2[0]: x1 = float(st.text_input("x1", value=2))
    with col2[1]: y1 = float(st.text_input("y1", value=2))
    # 0 = 90*, 1 = 270*
    bentuk_list = ["90°", "270°"]
    bentuk = st.selectbox(f"Sudut Rotasi", bentuk_list)

    st.write('### **Rumus**')

    if bentuk == bentuk_list[0]:
        st.latex(r"A(x,y) \rightarrow A'(-y+x_1+y_1,x-x_1+y_1)")
        xa = -y+x1+y1
        ya = x-x1+y1
    if bentuk == bentuk_list[1]:
        st.latex(r"A(x,y) \rightarrow A'(y+x_1-y_1,-x+x_1+y_1)")
        xa = y+x1-y1
        ya = -x+x1+y1

    st.write('## **Hasil Penyelesaian**')
    st.latex(fr"A({fungsi(x)},{fungsi(y)}) \rightarrow A'({fungsi(xa)},{fungsi(ya)})")

resolution = 1000

# tambah = 200
tambah = 0

# RGB, RGBA
im = Image.new('RGB', (resolution,resolution+tambah))
draw = ImageDraw.Draw(im, 'RGBA')

# font = ImageFont.truetype("roboto.ttf", size=50)

xb = 1
yb = 0
zoom = 0.2
zoom2 = 1

# x += 1e-10
# zoom += 1e-14
zoom = 1/zoom

def floor(a, b):
    return round(a-a%b,12)

# grid = 0.2
grid = 10**int(floor(np.log10(zoom/2),1))
grid2 = 10**int(floor(np.log10(zoom2*zoom/2),1))
# print(grid)

x_start = xb-zoom
x_end = xb+zoom

y_start = yb+zoom2*zoom
y_end = yb-zoom2*zoom

x_check = True
x_check_2 = True
y_check = True
y_check_2 = True

abc = 0
abc2 = 0

width = 2

font_list = [
    "arial.ttf",
    "ariblk.ttf",
    "Roboto-Regular.ttf",
    "consola.ttf",
    "FreeSans.ttf",
    "FreeSansBold.ttf"
]

font_index = 2
font = font_list[font_index]

def roboto(size):
    # return ImageFont.truetype("ariblk.ttf", size=size, encoding='utf-32')
    return ImageFont.truetype(f"fonts/{font}", size=size)

# Garis

def equation_line(y_current, fill, point=None, sign="="):
    if point != None:
        if a == round(resolution*(point-x_start)/(x_end-x_start)):
            b = resolution*(y_current-y_start)/(y_end-y_start)
            draw.ellipse((a-5, b-5, a+5, b+5), fill=fill)
            # fill2 = (255,255,255)
            fill2 = (128,255,128)
            draw.text((a+5, b), f"{name_list[point_index]}({fungsi(x_current)}, {fungsi(y_current)})", fill=fill2, font=roboto(20))
    # return y_current

def color(index):
    # 240,120,0,60,300,180,30
    # (0,0,255,32)
    # daftar = [(0,0,255),(0,255,0),(255,0,0),(255,255,0),(255,0,255),(0,255,255),(255,128,0),(128,0,255),(0,255,128),(0,128,255),(128,255,0),(255,0,128)]
    daftar = [(255,255,255),(128,128,255),(255,255,255)]
    return daftar[index]

for a in range(resolution):
    x_current = x_start+a*(x_end-x_start)/resolution
    x_check = x_current <= 1e-12

    if x_current+1e-12 >= floor(x_start,grid)+grid*(abc+1) and x_check_2:
        if x_current >= -1e-12 and x_check:
            draw.line((a,0,a,resolution), fill=(128,128,128))
            x_check = False
        else:
            draw.line((a,0,a,resolution), fill=(64,64,64))
        x_grid = round(resolution*y_start/(y_start-y_end))
        if x_grid < 0: x_grid = 0
        if x_grid >= resolution: x_grid = resolution
        if fungsi(round(x_current,3)) != 0:
            draw.text((a,x_grid+5), str(fungsi(round(x_current,3))), fill=(255,255,255), font=roboto(15))
        abc += 1
        x_check_2 = False
    else:
        x_check_2 = True

    y_current = y_start+a*(y_end-y_start)/resolution
    # if a >= 0:
        # print(y_current)

    y_check = y_current >= -1e-12

    if y_current-1e-12 <= grid2+floor(y_start,grid2)-grid2*(abc2+1) and y_check_2:
        if y_current <= 1e-12 and y_check:
            draw.line((0,a,resolution,a), fill=(128,128,128))
            y_check = False
        else:
            draw.line((0,a,resolution,a), fill=(64,64,64))
        y_grid = round(resolution*x_start/(x_start-x_end))
        if y_grid < 0: y_grid = 0
        if y_grid >= resolution: y_grid = resolution
        if fungsi(round(y_current,3)) != 0:
            draw.text((y_grid+5,a), str(fungsi(round(y_current,3))), fill=(255,255,255), font=roboto(15))
        # 0.1+0.2-0.3 = 1e-15
        # 1+2-3 = 0
        abc2 += 1
        y_check_2 = False
    else:
        y_check_2 = True

point = [[x,y],[x1,y1],[xa,ya]]
# name_list = ['A','B','C','D','E','F','G','H']
name_list = ['A','P',"A'"]
# point_index = 2

for point_index in range(len(point)):
    for a in range(resolution):
        x_current = x_start+a*(x_end-x_start)/resolution+1e-14
        prev_y_current = y_current
        point2 = point[point_index]
        prev_y_current = y_current
        y_current = point2[1]
        # print(y_current)
        equation_line(point2[1], color(point_index), point2[0])
        # equation_line(point2[1], (255,255,255), point2[0])

draw.text((20,20), nama, fill='white', font=roboto(60))

if nama == nama_list[3]:
    draw.text((20,100), f"Sudut rotasi: {bentuk}", fill='white', font=roboto(40))

im.save("preview.png")
st.image("preview.png", width=500)
# im.show()

with open("preview.png", "rb") as file:
    btn = st.download_button(
        label="Download Image",
        data=file,
        file_name="grafik.png"
    )