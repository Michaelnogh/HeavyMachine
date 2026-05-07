from flask import Flask, jsonify, request
from flask_cors import CORS
from machines_data import MACHINES

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Build sorted category list from the data once at startup
CATEGORIES = sorted({m["category"] for m in MACHINES})


@app.get("/api/machines")
def get_machines():
    """
    Returns all machines.
    Optional query params:
      ?category=Bulldozer   – filter by category (case-insensitive)
      ?search=cat           – search by name or manufacturer (case-insensitive)
    Both params can be combined.
    """
    category = request.args.get("category", "").strip()
    search   = request.args.get("search", "").strip().lower()

    result = MACHINES

    if category:
        result = [m for m in result if m["category"].lower() == category.lower()]

    if search:
        result = [
            m for m in result
            if search in m["name"].lower() or search in m["manufacturer"].lower()
        ]

    return jsonify(result)


@app.get("/api/categories")
def get_categories():
    """Returns a sorted list of all machine categories."""
    return jsonify(CATEGORIES)


@app.get("/api/machines/<int:machine_id>")
def get_machine(machine_id):
    """Returns a single machine by its id."""
    for m in MACHINES:
        if m["id"] == machine_id:
            return jsonify(m)
    return jsonify({"error": "Machine not found"}), 404


if __name__ == "__main__":
    app.run(port=8000, debug=True)
