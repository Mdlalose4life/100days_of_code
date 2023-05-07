from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {
        "id": 0,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_year": 1960,
        "genre": "Fiction"
    },
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "published_year": 1949,
        "genre": "Dystopian Fiction"
    },
    {
        "id": 2,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
        "genre": "Fiction"
    },
    {
        "id": 3,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "published_year": 1813,
        "genre": "Romance"
    },
    {
        "id": 4,
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "published_year": 1954,
        "genre": "Fantasy"
    }
]


@app.route('/books', methods=['GET'])
def Getbooks():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            "Nothing Found", 404


@app.route('/insert', methods=['POST'])
def insert_book():
    if request.method == 'POST':
        new_title = request.form['title']
        new_year = request.form['published_year']
        new_genre = request.form['genre'],
        if len(books_list) > 0:
            new_id = books_list[-1]['id'] + 1,
        else:
            new_id = 1,
        new_author = request.form['author']

        new_book = {
            "id": new_id,
            "title": new_title,
            "author": new_author,
            "published_year": new_year,
            "genre": new_genre
        }
        books_list.append(new_book)
        return jsonify(books_list), 201


@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def GetBook(id):
    if request.method == 'GET':
        if len(books_list) > 0:
            for book in books_list:
                if book['id'] == id:
                    return jsonify(book)
                pass
    if request.method == 'PUT':
        if len(books_list) > 0:
            for book in books_list:
                if book['id'] == id:
                    book['title'] = request.form['title']
                    book['author'] = request.form['author']
                    book['published_year'] = request.form['published_year']
                    book['genre'] = request.form['genre']
                    update_book = {
                        "id": book["id"],
                        "title": book["title"],
                        "author": book["author"],
                        "publised_year": book["published_year"]

                    }
                    return jsonify(update_book)

    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)


if __name__ == '__main__':
    app.run(debug=True)
