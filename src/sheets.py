"""
Program that access the google sheets and gets/update
the information of the students ans users into the cells.

COLUMN -- NAME
---------------
A1    ---- Matrícula
B1    ---- Nombre completo
C1    ---- Discord User
D1    ---- Discord #
E1    ---- ¿Dentro del server?

Starting from row 2 the users are registered
"""

import gspread
from google.oauth2.service_account import Credentials
from student import Student

from config import SCOPES, KEY, SHEET_NAME

credentials = Credentials.from_service_account_file(KEY, scopes = SCOPES)
gs = gspread.authorize(credentials)

sh = worksheet =  None

def open_google_sheets() -> bool:
    global sh, worksheet
    try:
        sh = gs.open(SHEET_NAME)
        worksheet = sh.get_worksheet(0)
        return True
    except Exception as  e:
        print(e)
        return False

def get_valid_student(full_name: str) -> bool:
    """
    Function that registers the student name into the excel sheets
    along with the discord username.
    """
    pass

def get_joined_student(discord_user: 'list[str]') -> bool:
    """
    Function that evaluates if the student is already
    registered into the server.
    """
    pass

def new_discord_student(student: Student, row: int) -> bool:
    """
    Function that will register the new student into the 
    google sheet database.
    Arguments: Student - class
    """
    try:
        student_name = student.nombre_completo
        student_disc = student.user_name
        student_disc_id = student.user_number
        student_id = student.matricula
        student_data = [student_id, student_name, student_disc, student_disc_id, "SI"]
        worksheet.insert_row(student_data, row)
        print("Usuario registrado con éxito")
        return True
    except Exception as e:
        print(e)
        return False
        
    

def get_last_row() -> 'list[str]':
    student_list = worksheet.col_values(1)
    return len(student_list)
