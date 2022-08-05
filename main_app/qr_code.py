import qrcode
from .uploadToS3 import upload_qr_to_s3
from pathlib import Path
import os
from .helper_functions import encrypt_data
BASE_DIR = Path(__file__).resolve().parent.parent
path_to_upload = os.path.join(BASE_DIR, "media")


def generate_qr_code(room_id, hotel_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    link = "google.com"
    query_params = f"{hotel_id}/{room_id}"
    enc_ids = encrypt_data(query_params)
    qr_data = f"{link}/{enc_ids}"
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white", ).get_image()
    file_name = f"{hotel_id}_{room_id}.jpg"
    path = f"{path_to_upload}/{file_name}"
    img.save(path)
    qr_s3_url = upload_qr_to_s3(file_name=file_name, body=path)
    os.remove(path)
    return qr_s3_url
