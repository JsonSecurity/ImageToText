from PIL import Image
from time import sleep as delay

import pytesseract
import signal
import glob
import sys

import utilscript as u

# download and install tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def signal_handler(sig, frame):
    print(f'\n\n{u._A} Saliendo...')
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)

def image_to_text(image_path):
    try:
        print(image_path)
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)

        return text
    except Exception as e:
        return [False, e]

def dir_image(path):
    files = glob.glob(f'{path}\\**\\*.png', recursive=True)
    u.bar(1, "Verifying", 80)

    if not files:
        print(f'\n{u._T} No image found\n')
        sys.exit(1)

    print(f'\n{u._T} Path images:\n')
    for file in files:
        print(f'{u._V} {file}')
        delay(.1)
    
    return files

def save_file(text):
    with open('trace.txt', 'a') as file:
        file.write(f'\n\n{text}')

if __name__ == '__main__':
    u.clear()
    #print(u.banner)
    print(u.tesseract_banner)
    
    path = "c:\\src\\images\\"

    images_path = dir_image(path)
    print(f'\n{u._T} Converting to text...\n')

    for path in images_path:
        texto_extraido = image_to_text(path)

        if texto_extraido[0]:
            save_file(texto_extraido)
        else:
            print(f'\n{u._T} {texto_extraido[1]}\n')
