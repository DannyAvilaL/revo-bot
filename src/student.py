"""
Clase para manipular la informacion del alumno desde
Discord hasta el worksheet de google Sheets.
"""

class Student:

    def __init__(self, nombre: str, user: 'list[str]'):
        self.nombre_completo = nombre
        self.user_name = user[0]
        self.user_number = user[1]

    @property
    def get_nombre_completo(self):
        return self.nombre_completo

    @property
    def get_user_name(self):
        return self.user_name
    
    @property
    def get_user_numer(self):
        return self.user_number

    def change_user(self, new_user: str):
        "User#4184"
        self.user_name = new_user[:4:]
        self.user_number = new_user[5::]
        