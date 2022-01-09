from skimage import data
from skimage.filters import edges

import imghdr

ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif'}

def allowed_file(file_ext):
    return file_ext in ALLOWED_EXTENSIONS

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

