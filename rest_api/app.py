from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'Brave New World', 'author': 'Aldous Huxley'}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    return jsonify({'book': book})

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify({'book': new_book}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        data = request.get_json()
        book.update(data)
        return jsonify({'book': book})
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)