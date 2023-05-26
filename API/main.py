from flask import Flask, jsonify

app = Flask(__name__)

meds = [
    {
        "id": 1,
        "identificacao": [
            {
                "medicamento": "Acetilcisteína",
                "classe": "mucolítico e expectorante",
                "apresentacao": "Amp. 3 mL (100 mg/mL)",
                "reconstituicao": "Já vem em solução",
            }
        ],
        "vias de admistração": [
            {
                "inalatória": "sim",
                "itramuscular": "não",
                "endovenosa_ou_direto": "prevenção nefropatia porcontraste: 5 – 10 min",
                "infusao": "intoxicação por paracetamol Dose 1: 1 hora Dose 2: 4 horas Dose 3: 16 horas",
            }
        ],
        "soluções p/ diluição": [
            {"SF": "Volume de soro igual ao volume do medicamento", "Dose": "1 hora"}
        ],
    }
]


@app.route("/meds", methods=["GET"])
def get_meds():
    return jsonify(meds)


@app.route("/meds/<int:med_id>", methods=["GET"])
def get_med(med_id):
    for med in meds:
        if med["id"] == med_id:
            return jsonify(med)
    return jsonify({"error": "Medication not found"})


if __name__ == "__main__":
    app.run()
