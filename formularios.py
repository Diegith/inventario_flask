from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, SelectField, RadioField, FileField, FloatField, TextAreaField, EmailField
from markupsafe import Markup
from wtforms.validators import InputRequired, Regexp
from flask_wtf.file import FileField, FileAllowed, FileRequired

class Login(FlaskForm):
    username_value = Markup('<span class="input-group-text" id="basic-addon1"><i class="fas fa-user-tie p-2"></i>Usuario</span>')
    username = StringField(username_value,validators = [InputRequired(message='Campo obligatorio'),validators.Regexp('\w+', flags=0, message='caracteres no permitidos')])
    password_value = Markup('<span class="input-group-text" id="basic-addon1"><i class="fas fa-key p-2"></i>Contraseña</span>')

    password = PasswordField(password_value, validators = [InputRequired(message='Campo obligatorio')])

    ingresar = SubmitField('Ingresar')

class FormPart(FlaskForm):

    nombres = StringField('Nombres',validators = [InputRequired(message='Campo obligatorio'),validators.Regexp('/^[A-Za-z0-9\s]+$/g', flags=0, message='caracteres no permitidos')])
    apellidos = StringField('Apellidos',validators = [InputRequired(message='Campo obligatorio'),validators.Regexp('/^[A-Za-z0-9\s]+$/g', flags=0, message='caracteres no permitidos')])
    tipo_documento = RadioField('Tipo Documento', choices=[('C.C','C.C'),('T.I','T.I'),('C.E','C.E')],default='C.C')
    numero_documento = StringField('No Documento',validators = [InputRequired(message='Campo obligatorio'),validators.Regexp('/^[A-Za-z0-9\s]+$/g', flags=0, message='caracteres no permitidos')])
    email = EmailField('Email',validators = [InputRequired(message='Campo obligatorio'),validators.Regexp("^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", flags=0, message='correo no valido')])
    celular = StringField('Celular',validators = [InputRequired(message='Campo obligatorio'),validators.Regexp('^(\d{10})$', flags=0, message='caracteres no permitidos')])
    direccion = StringField('Dirección',validators = [InputRequired(message='Campo obligatorio')],default='ingrese la dirección')
    username = StringField('Nombre de Usuario',validators = [InputRequired(message='Campo obligatorio'),validators.Regexp('\w+', flags=0, message='caracteres no permitidos')])
    password = PasswordField('Contraseña', validators = [InputRequired(message='Campo obligatorio'),validators.Regexp('^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$', flags=0, message='caracteres no permitidos')])
    confirm_password = PasswordField('Confirmar Contraseña', validators = [InputRequired(message='Campo obligatorio'),validators.Regexp('^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$', flags=0, message='caracteres no permitidos')])
    roles = SelectField('Asignar Rol', choices=[(1,'Super Administrador'), (2,'Administrador'),(3,'Usuario Final') ],default=3)
    autorizacion = RadioField('Autorizacion de Datos', choices=[('si','Autorizo el manejo y almacenamiento de datos personales')],default='si')
    crear = SubmitField('Crear Usuario')
    actualizar = SubmitField('Actualizar Usuario')

    #proveedor
    nombresProveedor = StringField('Nombre Proveedor',validators = [InputRequired(message='Campo obligatorio'),validators.Regexp('/^[A-Za-z0-9\s]+$/g', flags=0, message='caracteres no permitidos')])
    logo = FileField('Logo Proveedor', validators=[FileAllowed(['jpg', 'png'])])
    actualizarProveedor = SubmitField('Actualizar Proveedor')
    #producto
    nombresProducto = StringField('Nombre Producto',validators = [InputRequired(message='Campo obligatorio'),validators.Regexp('/^[A-Za-z0-9\s]+$/g', flags=0, message='caracteres no permitidos')])
    cantidadMinima = FloatField('Cantidad Mínima del producto',validators = [InputRequired(message='Campo obligatorio')])
    cantidadDisponible = FloatField('Cantidad Disponible del producto',validators = [InputRequired(message='Campo obligatorio')])
    descripcion = TextAreaField('Descripción del Producto')
    img1 = FileField('Primera imagen del producto', validators=[FileAllowed(['jpg', 'png'])])
    img2 = FileField('Segunda imagen del producto', validators=[FileAllowed(['jpg', 'png'])])
    img3 = FileField('Tercera imagen del producto', validators=[FileAllowed(['jpg', 'png'])])
    actualizarProducto = SubmitField('Actualizar Producto')