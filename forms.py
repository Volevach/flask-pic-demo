from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from picutil import check_picture_size

class GuideForm(FlaskForm):
    header_img = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')

def validate_header_img(flaskform, field):
    check = check_picture_size(field.data)
    print(field.data) #Prints correct file <FileStorage: 'test.jpg' ('image/jpeg')
    if check:
        print('Check') #Prints 'Check' so it is True
        raise ValidationError("Uploaded picture is too small") # so is here something wrong???

