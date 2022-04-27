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

from config import SCOPES, KEY, SHEET_NAME

credentials = Credentials.from_service_account_file(KEY, scopes = SCOPES)
gs = gspread.authorize(credentials)

sh = None

def open_google_sheets() -> str:
    global sh
    try:
        sh = gs.open(SHEET_NAME)
        return "Sheets open"
    except:
        return "Conection error."

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

def new_discord_student(discord_user: 'list[str]') -> bool:
    """
    Function that will modify the state of the student
    as "DENTRO" in the column '¿Dentro del server?'
    """
    pass

def get_cell_value(cell: str) -> str:
    return sh.sheet1.get(cell)
