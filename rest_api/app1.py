from flask import Flask, jsonify, request

app = Flask(__name__)

# In-Memory-Datenstruktur
books = [
    {"id": 1, "title": "Der alte Mann und das Meer", "author": "Ernest Hemingway"},
    {"id": 2, "title": "Die Verwandlung", "author": "Franz Kafka"},
]

# Hilfsfunktion zum Finden eines Buchs nach ID
def find_book(book_id):
    return next((book for book in books if book["id"] == book_id), None)

# GET /books – alle Bücher abrufen
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

# GET /books/<book_id> – einzelnes Buch abrufen
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = find_book(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Buch nicht gefunden"}), 404

# POST /books – neues Buch hinzufügen
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({"error": "Felder 'title' und 'author' sind erforderlich"}), 400

    new_id = max([book["id"] for book in books], default=0) + 1
    new_book = {
        "id": new_id,
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

# PUT /books/<book_id> – bestehendes Buch aktualisieren
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = find_book(book_id)
    if not book:
        return jsonify({"error": "Buch nicht gefunden"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Keine Daten gesendet"}), 400

    # Felder aktualisieren (wenn vorhanden)
    book["title"] = data.get("title", book["title"])
    book["author"] = data.get("author", book["author"])
    return jsonify(book), 200

# DELETE /books/<book_id> – Buch löschen
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)
    if not book:
        return jsonify({"error": "Buch nicht gefunden"}), 404

    books.remove(book)
    return jsonify({"message": f"Buch mit ID {book_id} wurde gelöscht"}), 200

# Startpunkt
if __name__ == '__main__':
    app.run(debug=True)
