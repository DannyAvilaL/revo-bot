"""
Programa que accede a google sheets y obtiene/actualiza
la información de las celdas.
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
        return "Sheets abierto"
    except:
        return "Hubo un error de Conexion"

def get_valid_student(full_name: str) -> bool:
    """
    Función que revisa que el nombre REAL del estudiante esté dentro
    de la comunidad. 
    """
    pass

def get_joined_student(discord_user: list[str]) -> bool:
    """
    Función que revisa si el estudiante ya estaba previamente
    registrado como inscrito en el servidor
    """
    pass

def new_discord_student(discord_user: list[str]) -> bool:
    """
    Función que modificará el estado del estudiante como
    'DENTRO' en la columna '¿Dentro del server?'
    """
    pass

def get_cell_value(cell: str) -> str:
    return sh.sheet1.get(cell)
