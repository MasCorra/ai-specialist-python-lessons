# Scrivi un programma che analizza i voti degli studenti e crea dizionari
# di statistiche utilizzando dictionary comprehension. Il programma deve:
#
# 1. Creare un dizionario con i nomi degli studenti come chiavi e liste
# di voti come valori (almeno 5 studenti con 3-4 voti ciascuno)
# 2. Utilizzare dictionary comprehension per creare un dizionario con
# le medie dei voti di ogni studente
# 3. Utilizzare dictionary comprehension per creare un dizionario che
# contiene solo gli studenti con media superiore a 6.0
# 4. Utilizzare dictionary comprehension annidata per creare un dizionario
# dove ogni studente ha un dizionario con 'media', 'voto_max' e 'voto_min'
# 5. Stampare tutti i risultati in modo formattato
def media(parametro):
    return sum(parametro) / len(parametro)

studenti = {
    "Marco": [7, 3, 6, 4],
    "Luca": [6, 7, 8],
    "Anna": [9, 8, 10, 9],
    "Giulia": [7, 6, 8],
    "Paolo": [5, 7, 6, 8]
}
medie = {nome: media(voti) for nome, voti in studenti.items()}
print(medie)

media_alta = {nome: media for nome, media in medie.items() if media > 6}
print(media_alta)

statistiche = {
    nome: {
        "media": media(voti),
        "voto_max": max(voti),
        "voto_min": min(voti),
    }
    for nome, voti in studenti.items()
}
print(statistiche)


registro = {
    nome: {
        statistica: (
            media(voti) if statistica == "media"
            else max(voti) if statistica == "voto_max"
            else min(voti)

        )
        for statistica in ["media", "voto_max", "voto_min"]
    }
    for nome, voti in studenti.items()
}
print(registro)


