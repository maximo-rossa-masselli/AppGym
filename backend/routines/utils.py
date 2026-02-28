import qrcode
from io import BytesIO
from django.core.files import File
import os


def generar_qr_para_gym(gym):
    base_url = os.getenv("RENDER_EXTERNAL_HOSTNAME")
    if base_url:
        print("Usando url de render")
        full_url = f"https://{base_url}/public/{gym.qr_token}/"
    else:
        print("Usando url localhost")
        full_url = f"http://127.0.0.1:8000/api/public/{gym.qr_token}/"
    qr = qrcode.make(full_url)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    filename = f"gym_{gym.name}_qr.png"
    gym.qr_image.save(filename, File(buffer), save=False)