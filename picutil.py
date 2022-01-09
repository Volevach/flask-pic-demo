from PIL import Image

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def check_picture_size(form_header_picture):
    i = Image.open(form_header_picture)
    if (i.size[0] < 1750) or (i.size[1] < 1000):
        return True

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS