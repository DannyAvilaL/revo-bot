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
        """
        Returns the full name of the student
        """
        return self.nombre_completo

    @property
    def get_user_name(self):
        """Returns the user name of the student"""
        return self.user_name
    
    @property
    def get_user_number(self):
        """Returns the discord # of the student"""
        return self.user_number

    def change_user(self, new_user: str):
        """
        Updates the discord user info of the student.
        new_user: 'NewUser#1234'
        """
        self.user_name = new_user[:4:]
        self.user_number = new_user[5::]
        