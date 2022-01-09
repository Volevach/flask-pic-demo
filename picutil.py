from PIL import Image
import imghdr

ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif'}

def check_picture_size(picture):
    i = Image.open(picture)
    if (i.size[0] < 1750) or (i.size[1] < 1000):
        return True

def allowed_file(file_ext):
    return file_ext in ALLOWED_EXTENSIONS

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')