'''Contains windows functions'''

from PIL import ImageGrab
from io import BytesIO
import win32clipboard


def clipboard_upload_img(img):
    '''upload image to clipboard'''
    output = BytesIO()
    img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


def clipboard_get_img():
    '''get image from clipboard'''
    return ImageGrab.grabclipboard()
