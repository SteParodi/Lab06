import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def get_nome(self):
        return self.model.nome

    def get_responsabile(self):
        return self.model.responsabile

    def conferma_responsabile(self, e):
        nuovo_resp = self.view.input_responsabile.value.strip()
        if not nuovo_resp:
            self.view.show_alert("Il nome del responsabile non può essere vuoto!")
            return

        self.model.set_responsabile(nuovo_resp)
        self.view.txt_responsabile.value = f"Responsabile: {self.model.responsabile}"
        self.view.update()

    def mostra_strumenti(self, e):
        self.view.lista_strumenti.controls.clear()
        try:
            strumenti = self.model.get_all_strumenti()
            if not strumenti:
                self.view.lista_strumenti.controls.append(ft.Text("Nessuno strumento presente nel deposito."))
            else:
                for s in strumenti:
                    self.view.lista_strumenti.controls.append(ft.Text(str(s)))
            self.view.update()
        except Exception as err:
            self.view.show_alert(f"Errore caricamento database: {err}")

    def cerca_per_tipo(self, e):
        tipo = self.view.input_tipo_strumento.value.strip()
        if not tipo:
            self.view.show_alert("Inserire il tipo di strumento da cercare!")
            return

        self.view.lista_strumenti_ricerca.controls.clear()
        try:
            risultati = self.model.get_strumenti_per_tipo(tipo)
            if not risultati:
                self.view.lista_strumenti_ricerca.controls.append(
                    ft.Text(f"Nessuno strumento trovato di tipo '{tipo}'.")
                )
            else:
                for s in risultati:
                    self.view.lista_strumenti_ricerca.controls.append(ft.Text(str(s)))
            self.view.update()
        except Exception as err:
            self.view.show_alert(f"Errore durante la ricerca: {err}")