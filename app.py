from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/valuta", methods=["POST"])
def valuta_auto():
    dati = request.json
    # Per ora restituiamo i dati ricevuti
    return jsonify({
        "stato": "successo",
        "dati_ricevuti": dati,
        "valutazione": "Da implementare"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
