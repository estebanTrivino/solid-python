# Incorrecto

class User:

    def __init__(self, name, email)-> None:
        self.name = name
        self.email = email

    """
    El usuario no debería tener la responsabilidad de almacenar información en la base de datos
    """
    def save_to_database(self):
        # Código para guardar el usuario

    """
    El usuario no deberia tener la responsabilidad de enviar correo. 
    Si cambia la estructura del usuario, se beria afectado el envio del correo y esto no deberia ser asi
    """
    def send_email(self):
        # Código para enviar un email

# Correcto


class User:

    def __init__(self, name, email)-> None:
        self.name = name
        self.email = email

class UserService:

    def save_to_database(self, user):
        # Código para guardar el usuario

class EmailService: 
    
    def send_email(self, email, message):
        # Código para enviar un email


