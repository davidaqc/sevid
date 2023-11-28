from OCR import OCR
from PIL import Image
import os

def run_ocr():
    ocr = OCR()

    # Verifica si existe la imagen -imagen.jpg-
    try:
        imgIn = Image.open("resources/imagen.jpg")
    except IOError:
        print("Error: No se pudo abrir la imagen")
        return 'Error'
    
    imgOut,text = ocr.recognizeText(imgIn)

    # Crea el archivo -text-out.txt- si este no existe
    if not os.path.isfile("text-out/text-out.txt"):
        open("text-out/text-out.txt", "w")

    ocr.save_text(text,"text-out/text-out.txt")
    lista =ocr.save_text_list(text)
    print(lista)
    #imgOut.show()
    imgOut.save("img-out/out.jpg")

    return lista
