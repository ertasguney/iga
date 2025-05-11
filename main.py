from flask import Flask, request, jsonify

app = Flask(__name__)

# Liste des clés valides pour l'exemple
valid_keys = ["RTKMN-IG-Manager-10day", "SomeOtherValidKey"]

@app.route('/check_user', methods=['GET'])
def check_user():
    # Récupérer la clé passée dans l'URL
    key = request.args.get('key')

    # Vérifier si la clé est valide
    if key in valid_keys:
        return jsonify({"status": "valid key"})
    else:
        return jsonify({"status": "invalid key"})

if __name__ == '__main__':
    app.run(debug=True)
