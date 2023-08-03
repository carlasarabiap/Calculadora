import flet as ft
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    border_radius,
    colors,
    UserControl,
)
from flet_core import MainAxisAlignment


# ¡¡¡no trae el resultado de la operación para continuar una nueva operación!!!


def main(page: ft.Page):
    page.title = "Calculadora"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    def button_clicked(e):

        if e.control.text == "CE":
            resp.value = ""
            pantalla.value = ""
        elif e.control.text == "C":
            resp.value = ""
            pantalla.value = pantalla.value
        elif e.control.text == "%":
            resp.value = pantalla.value
            pantalla.value = ""
            if resp.value[-1] == "/" or resp.value[-1] == "*" or resp.value[-1] == "-" or resp.value[-1] == "+":
                resp.value = resp.value[:-1]
            resp.value += "%"
        elif e.control.text == "/":
            if resp.value[-1] == "%" or resp.value[-1] == "*" or resp.value[-1] == "-" or resp.value[-1] == "+":
                resp.value = resp.value[:-1]
            resp.value += "/"
        elif e.control.text == "7":
            resp.value += "7"
        elif e.control.text == "8":
            resp.value += "8"
        elif e.control.text == "9":
            resp.value += "9"
        elif e.control.text == "*":
            if resp.value[-1] == "/" or resp.value[-1] == "%" or resp.value[-1] == "-" or resp.value[-1] == "+":
                resp.value = resp.value[:-1]
            resp.value += "*"
        elif e.control.text == "4":
            resp.value += "4"
        elif e.control.text == "5":
            resp.value += "5"
        elif e.control.text == "6":
            resp.value += "6"
        elif e.control.text == "-":
            if resp.value[-1] == "/" or resp.value[-1] == "*" or resp.value[-1] == "%" or resp.value[-1] == "+":
                resp.value = resp.value[:-1]
            resp.value += "-"
        elif e.control.text == "1":
            resp.value += "1"
        elif e.control.text == "2":
            resp.value += "2"
        elif e.control.text == "3":
            resp.value += "3"
        elif e.control.text == "+":
            if resp.value[-1] == "/" or resp.value[-1] == "*" or resp.value[-1] == "-" or resp.value[-1] == "%":
                resp.value = resp.value[:-1]
            resp.value += "+"
        elif e.control.text == "0":
            resp.value += "0"
        elif e.control.text == "00":
            resp.value += "00"
        elif e.control.text == ".":
            resp.value += "."
        elif e.control.text == "=":
            total = eval(resp.value)
            pantalla.value = total
            resp.value = ""


        page.update()

    pantalla = ft.Text(value="", width=300)
    resp = ft.TextField(value="", width=300)

    ce = ft.ElevatedButton(text="CE", on_click=button_clicked)
    c = ft.ElevatedButton(text="C", on_click=button_clicked)
    porcentaje = ft.ElevatedButton(text="%", on_click=button_clicked)
    divide = ft.ElevatedButton(text="/", on_click=button_clicked)
    siete = ft.ElevatedButton(text="7", on_click=button_clicked)
    ocho = ft.ElevatedButton(text="8", on_click=button_clicked)
    nueve = ft.ElevatedButton(text="9", on_click=button_clicked)
    multiplica = ft.ElevatedButton(text="*", on_click=button_clicked)
    cuatro = ft.ElevatedButton(text="4", on_click=button_clicked)
    cinco = ft.ElevatedButton(text="5", on_click=button_clicked)
    seis = ft.ElevatedButton(text="6", on_click=button_clicked)
    resta = ft.ElevatedButton(text="-", on_click=button_clicked)
    uno = ft.ElevatedButton(text="1", on_click=button_clicked)
    dos = ft.ElevatedButton(text="2", on_click=button_clicked)
    tres = ft.ElevatedButton(text="3", on_click=button_clicked)
    suma = ft.ElevatedButton(text="+", on_click=button_clicked)
    cero = ft.ElevatedButton(text="0", on_click=button_clicked)
    dCero = ft.ElevatedButton(text="00", on_click=button_clicked)
    punto = ft.ElevatedButton(text=".", on_click=button_clicked)
    igual = ft.ElevatedButton(text="=", on_click=button_clicked)


    row1 = resp
    row2 = pantalla
    row3 = ft.Row([ce, c, porcentaje, divide], alignment=MainAxisAlignment.CENTER)
    row4 = ft.Row([siete, ocho, nueve, multiplica], alignment=MainAxisAlignment.CENTER)
    row5 = ft.Row([cuatro, cinco, seis, resta], alignment=MainAxisAlignment.CENTER)
    row6 = ft.Row([uno, dos, tres, suma], alignment=MainAxisAlignment.CENTER)
    row7 = ft.Row([cero, dCero, punto, igual], alignment=MainAxisAlignment.CENTER)

    page.add(row1, row2, row3, row4, row5, row6, row7)



ft.app(target=main)