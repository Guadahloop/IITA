import flet as ft
import json
import os
from datetime import datetime

# Constantes
class LifeCalendar:
    def __init__(self, data_file="datos_fecha.json"):
        self.ANIOS = 90
        self.SEMANAS_ANIO = 52
        self.TOTAL_SEMANAS = self.ANIOS * self.SEMANAS_ANIO
        self.COLOR_SEMANA_VIVIDA = "#FF6347"
        self.data_file = data_file
        self.fecha_nacimiento = self.cargar_fecha()

# Función para calcular semanas vividas
    def calcular_semanas_vividas(self, fecha_str):
        nacimiento = datetime.strptime(fecha_str, "%d-%m-%Y")
        hoy = datetime.today()
        return (hoy - nacimiento).days // 7

    def guardar_fecha(self, fecha_str):
        with open(self.data_file, "w") as f:
            json.dump({"fecha_nacimiento": fecha_str}, f)

    def cargar_fecha(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                return data.get("fecha_nacimiento")
        return None

    def borrar_datos(self):
        if os.path.exists(self.data_file):
            os.remove(self.data_file)

# Mostrar calendario
def mostrar_calendario(page: ft.Page, calendario: LifeCalendar):
    semanas_vividas = calendario.calcular_semanas_vividas(calendario.fecha_nacimiento)
    contador = ft.Text(
        f"Semanas vividas: {semanas_vividas} / {calendario.TOTAL_SEMANAS}",
        size=16,
        weight="bold"
    )

    # Mensajes según las semanas vividas
    if semanas_vividas <= 1000:
        mensaje = "¡Estás comenzando este increíble viaje! 💫"
    elif semanas_vividas <= 2000:
        mensaje = "⏳😉"
    elif semanas_vividas <= 3000:
        mensaje = "⏱️🔥"
    else:
        mensaje = "🎓💡"

    mensaje_texto = ft.Text(mensaje, size=14, weight="bold", color="blue", text_align="center")

    filas = []
    for anio in range(calendario.ANIOS):
        fila = []
        label = ft.Text(f"Año {anio}", width=60, text_align="center")

        for semana in range(calendario.SEMANAS_ANIO):
            id_semana = anio * calendario.SEMANAS_ANIO + semana
            color = calendario.COLOR_SEMANA_VIVIDA if id_semana < semanas_vividas else "white"
            cuadrado = ft.Container(
                width=10,
                height=10,
                bgcolor=color,
                border=ft.border.all(0.3, "gray")
            )
            fila.append(cuadrado)

        filas.append(ft.Row([label] + fila, spacing=1, alignment=ft.MainAxisAlignment.CENTER))

    volver_btn = ft.ElevatedButton(
        "Calcular otra fecha",
        on_click=lambda e: reiniciar_app(page, calendario)
    )

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Tu vida en semanas", size=24, weight="bold", text_align="center"),
                    mensaje_texto,
                    contador,
                    volver_btn
                ] + filas,
                scroll=ft.ScrollMode.ALWAYS,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        )
    )

# Pantalla inicial para ingresar la fecha
def mostrar_pantalla_input(page: ft.Page, calendario: LifeCalendar):
    page.clean()
    fecha_input = ft.TextField(
    label="Fecha de nacimiento",
    hint_text="dd-mm-yyyy",
    width=300,
    text_align=ft.TextAlign.CENTER
)

    def confirmar_fecha(e):
        fecha_str = fecha_input.value.strip()
        try:
            if not fecha_str:
                raise ValueError("Campo vacío")
            fecha = datetime.strptime(fecha_str, "%d-%m-%Y")
            if fecha > datetime.today():
                raise ValueError("Fecha futura")
            calendario.guardar_fecha(fecha_str)
            calendario.fecha_nacimiento = fecha_str
            page.clean()
            mostrar_calendario(page, calendario)
        except ValueError as ve:
            mensaje_error = str(ve)
            if mensaje_error == "Campo vacío":
                texto_error = "El campo no puede estar vacío."
            elif mensaje_error == "Fecha futura":
                texto_error = "La fecha no puede ser en el futuro."
            else:
                texto_error = "Fecha inválida. Usá el formato dd-mm-yyyy."
            page.snack_bar.content = ft.Text(texto_error)
            page.snack_bar.open = True
            page.update()
    page.add(
    ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column(
            [
                ft.Text("Ingresá tu fecha de nacimiento", size=20, weight="bold"),
                fecha_input,
                ft.ElevatedButton("Confirmar", on_click=confirmar_fecha)
            ],
            spacing=20,
            horizontal_alignment="center"
        ),
        expand=True,
        padding=20
    )
)

# Reiniciar app
def reiniciar_app(page: ft.Page, calendario: LifeCalendar):
    calendario.borrar_datos()
    calendario.fecha_nacimiento = None
    mostrar_pantalla_input(page, calendario)

# Construccion principal
def build_page(page: ft.Page):
    calendario = LifeCalendar()
    page.title = "Life Calendar"
    page.scroll = "auto"
    page.snack_bar = ft.SnackBar(content=ft.Text(""), bgcolor="white")
    page.overlay.append(page.snack_bar)

    if calendario.fecha_nacimiento:
        mostrar_calendario(page, calendario)
    else:
        mostrar_pantalla_input(page, calendario)

# Main
def main(page: ft.Page):
    build_page(page)

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)



