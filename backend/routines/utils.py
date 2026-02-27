import qrcode
from io import BytesIO
from django.core.files import File


def generar_qr_para_gym(gym):
    url = f"http://127.0.0.1:8000/api/public/{gym.qr_token}/"

    qr = qrcode.make(url)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    filename = f"gym_{gym.name}_qr.png"
    gym.qr_image.save(filename, File(buffer), save=False)