import os.path
import cv2
import pyqrcode
import png

# classe per la gestione delle operazioni che usufruiscono di codice QR
class GestioneQr(object):
    # metodo statico per la lettura del codice QR fornito
    @staticmethod
    def readQr(nomeFile):
        if nomeFile[0].endswith('.png'):
            img = cv2.imread(nomeFile[0])
            if img.any():
                detector = cv2.QRCodeDetector()
                data, points, straight_qrcode = detector.detectAndDecode(img)
                if points is not None:
                    return data
                else:
                    raise Exception('QR code non trovato')
        raise Exception('Nome file non corretto')


    # metodo che genera un codice QR del dato fornito, restituendo il nome del file appena creato
    @staticmethod
    def generateQr(data):
        filename = data + '.png'
        if not os.path.isfile(filename):
            img = pyqrcode.create(data)
            img.png(filename, scale=6)
            return filename
        else:
            raise Exception('File with this name already exists')