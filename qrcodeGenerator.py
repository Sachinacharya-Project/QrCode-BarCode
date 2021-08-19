##############################################################
# IMPORTING ESSENTIALS FILES
###############################################################
import os
import pyqrcode
import barcode
from barcode.writer import ImageWriter
os.system("cls")

def CreateQRCode():
    os.system("cls")
    data = str(input("DATA YOU WANNA GENERATE: "))
    print("\n")
    output = str(input("File Name: "))
    qr = pyqrcode.create(data)
    qr.png(f"Output\\{output}", scale=8)
    print("CODE GENERATED")

def BarcodeCreator():
    os.system("cls")
    print("IT ONLY GENERATE ALPHANUMERIC BARCODE ONLY\n\n")
    data = input("DATA YOU WANNA GENERATE: ")
    output = str(input("FILE NAME: "))
    data = str(data)
    a = barcode.get_barcode_class("code128")
    b = a(data, writer=ImageWriter())
    b.save(f"Output\\{output}")
    print("CODE GENERATED")

def MainFunction():
    while True:
        option = input("Wanna Create (Q): QR CODE or (B): BARCODE or (E) EXIT: ")

        if str(option).lower() == "q":
            CreateQRCode()
        elif str(option).lower() == "b":
            print("OPTION BARCODE CHOOSEN")
            BarcodeCreator()
        elif str(option).lower() == "e":
            print("PRESS CTRL-C")
        else:
            print("WRONG OPTION CHOOSEN")
            break
# 
# qr = pyqrcode.create("Hello World")

# qr.png("abc.png", scale=8)
