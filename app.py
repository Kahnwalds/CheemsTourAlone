from flask import Flask, jsonify, request
from entities.Trip import Trip

app = Flask(__name__)

# ──────────────────────────────────────────────
# Health check
# ──────────────────────────────────────────────
@app.route('/', methods=['GET'])
def index():
    return jsonify({"success": True, "message": "CheemsTourAlone API running"}), 200


# ──────────────────────────────────────────────
# GET /trips  →  obtener todos los trips
# ──────────────────────────────────────────────
@app.route('/trips', methods=['GET'])
def get_trips():
    try:
        trips = Trip.get_all()
        if trips is None:
            return jsonify({"success": False, "message": "Error retrieving trips"}), 500
        return jsonify(trips), 200
    except Exception as ex:
        print(f"[ERROR] GET /trips: {ex}")
        return jsonify({"success": False, "message": str(ex)}), 500


# ──────────────────────────────────────────────
# POST /trip  →  crear un nuevo trip
# ──────────────────────────────────────────────
@app.route('/trip', methods=['POST'])
def save_trip():
    try:
        data = request.json
        trip = Trip(
            name=data['name'],
            city=data['city'],
            latitude=data['latitude'],
            longitude=data['longitude']
        )
        new_id = trip.save()
        success = new_id is not None
        return jsonify({"success": success, "id": new_id}), 200 if success else 500
    except Exception as ex:
        print(f"[ERROR] POST /trip: {ex}")
        return jsonify({"success": False, "message": str(ex)}), 500


# ──────────────────────────────────────────────
# PUT /trip/<id>  →  actualizar un trip existente
# ──────────────────────────────────────────────
@app.route('/trip/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    try:
        data = request.json
        trip = Trip(
            name=data['name'],
            city=data['city'],
            latitude=data['latitude'],
            longitude=data['longitude']
        )
        updated = trip.update(trip_id)
        return jsonify({"success": updated}), 200 if updated else 500
    except Exception as ex:
        print(f"[ERROR] PUT /trip/{trip_id}: {ex}")
        return jsonify({"success": False, "message": str(ex)}), 500


# ──────────────────────────────────────────────
# DELETE /trip/<id>  →  eliminar un trip
# ──────────────────────────────────────────────
@app.route('/trip/<int:trip_id>', methods=['DELETE'])
def delete_trip(trip_id):
    try:
        deleted = Trip.delete(trip_id)
        return jsonify({"success": deleted}), 200 if deleted else 500
    except Exception as ex:
        print(f"[ERROR] DELETE /trip/{trip_id}: {ex}")
        return jsonify({"success": False, "message": str(ex)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
