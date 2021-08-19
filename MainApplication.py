import qrcodeGenerator
import qrcodeScanner
import os
os.system("cls")
option = str(input("""Choose Option
    (G)ENERATE QRCODE OR BARCODE 
    (S)CAN QRCODE WITH CAMERA
    (M) SCAN QRCODE LOCALLY 
    (Z) EXIT: 
""")).lower()

while True:
    if option == "g":
        qrcodeGenerator.MainFunction()
    elif option == "s":
        qrcodeScanner.MainFunc()
    elif option == "m":
        print("QRCODE")
    elif option == "z":
        print("Exiting...")
        break