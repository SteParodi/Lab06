import flet as ft
from UI.alert import AlertManager


class View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Lab06"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        self.alert = AlertManager(page)
        self.controller = None

        self.txt_titolo = None
        self.txt_responsabile = None
        self.input_responsabile = None
        self.lista_strumenti = None
        self.input_tipo_strumento = None
        self.lista_strumenti_ricerca = None
        self.toggle_cambia_tema = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        self.txt_titolo = ft.Text(value=self.controller.get_nome(), size=38, weight=ft.FontWeight.BOLD)
        self.txt_responsabile = ft.Text(
            value=f"Responsabile: {self.controller.get_responsabile()}",
            size=16,
            weight=ft.FontWeight.BOLD
        )

        # Sezione 2: Modifica Responsabile
        self.input_responsabile = ft.TextField(value=self.controller.get_responsabile(), label="Responsabile")
        pulsante_conferma_responsabile = ft.Button("Conferma", on_click=self.controller.conferma_responsabile)

        # Sezione 3: Lista Strumenti
        self.lista_strumenti = ft.ListView(expand=False, height=180, spacing=5, padding=10, auto_scroll=False)
        pulsante_mostra_strumenti = ft.Button("Mostra", on_click=self.controller.mostra_strumenti)

        # Sezione 4: Ricerca per Tipo
        self.input_tipo_strumento = ft.TextField(label="Tipo", width=300)
        pulsante_cerca_strumenti = ft.Button("Cerca", on_click=self.controller.cerca_per_tipo)
        self.lista_strumenti_ricerca = ft.ListView(expand=False, height=180, spacing=5, padding=10, auto_scroll=False)

        # Toggle Tema
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # Composizione Layout
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            self.txt_responsabile,
            ft.Divider(),

            # Sezione 2
            ft.Text("Modifica Informazioni", size=20),
            ft.Row(
                spacing=20,
                controls=[self.input_responsabile, pulsante_conferma_responsabile],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Divider(),

            # Sezione 3
            ft.Text("Strumenti", size=20),
            pulsante_mostra_strumenti,
            self.lista_strumenti,
            ft.Divider(),

            # Sezione 4
            ft.Text("Cerca Strumento per Tipo", size=20),
            ft.Row(
                spacing=20,
                controls=[self.input_tipo_strumento, pulsante_cerca_strumenti],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            self.lista_strumenti_ricerca
        )
        self.page.update()

    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()