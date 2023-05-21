
"""
1. objetivo
2. url base
3. endpoints
    localhot/meds (get)
    localhost/meds (post)
    localhost/meds (delete)
    localhost/meds/id (get)
    localhost/meds/id (put)

4. recursos
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

meds = [{
    "id": 1,
    "identificacao": [{"medicamento": "Acetilcisteína",
                      "classe": "mucolítico e expectorante",
                       "apresentacao": "Amp. 3 mL (100 mg/mL)",
                       "reconstituicao": "Já vem em solução"}],
    "vias de admistração": [{
        "inalatória": "sim",
        "itramuscular": "não",
        "endovenosa_ou_direto": "prevenção nefropatia porcontraste: 5 – 10 min",
        "infusao": "intoxicação por paracetamol Dose 1: 1 hora Dose 2: 4 horas Dose 3: 16 horas"
    }]

}]
