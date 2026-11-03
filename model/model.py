from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

from database.DB_connect import get_connection
from model.strumento import Strumento


class DepositoStrumenti:
    def __init__(self, nome: str, responsabile: str):
        self.nome = nome
        self.responsabile = responsabile

    def set_responsabile(self, nuovo_responsabile: str):
        self.responsabile = nuovo_responsabile

    def get_all_strumenti(self) -> list[Strumento]:
        cnx = get_connection()
        if cnx is None:
            return []

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM strumento"
        cursor.execute(query)

        risultati = []
        for row in cursor:
            # Converte il booleano da tinyint/int se presente nel DB
            disponibile = bool(row.get("disponibile", True))
            strumento = Strumento(
                codice=row["codice"],
                tipo=row["tipo"],
                marca=row["marca"],
                anno_acquisto=row["anno_acquisto"],
                valore=row["valore"],
                disponibile=disponibile
            )
            risultati.append(strumento)

        cursor.close()
        cnx.close()
        return risultati

    def get_strumenti_per_tipo(self, tipo: str) -> list[Strumento]:
        cnx = get_connection()
        if cnx is None:
            return []

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM strumento WHERE LOWER(tipo) = LOWER(%s)"
        cursor.execute(query, (tipo.strip(),))

        risultati = []
        for row in cursor:
            disponibile = bool(row.get("disponibile", True))
            strumento = Strumento(
                codice=row["codice"],
                tipo=row["tipo"],
                marca=row["marca"],
                anno_acquisto=row["anno_acquisto"],
                valore=row["valore"],
                disponibile=disponibile
            )
            risultati.append(strumento)

        cursor.close()
        cnx.close()
        return risultati