from flask import Flask, render_template, jsonify, abort, request
from flask_restful import Api, Resource, fields, marshal_with, reqparse
from config import DB_URI
from model import db, Book

app = Flask(__name__)
api = Api(app)
app.config.update({
    'SQLALCHEMY_DATABASE_URI': DB_URI,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
})
db.init_app(app) #  初始化数据库连接
app.app_context().push()

db.drop_all() # 删除所有表
db.create_all() # 创建所有表

lunyu = Book(title='lunyu1', author='kongzi', price=18)
lunyu1 = Book(title='lunyu2', author='kongzi', price=18.1)
lunyu2 = Book(title='lunyu3', author='kongzi', price=18.2)
lunyu3 = Book(title='lunyu4', author='kongzi', price=18.3)
lunyu4 = Book(title='lunyu5', author='kongzi', price=18.4)
lunyu5 = Book(title='lunyu6', author='kongzi', price=18.5)
lunyu6 = Book(title='lunyu7', author='kongzi', price=18.6)

db.session.add(lunyu)
db.session.add(lunyu1)
db.session.add(lunyu2)
db.session.add(lunyu3)
db.session.add(lunyu4)
db.session.add(lunyu5)
db.session.add(lunyu6)
db.session.commit()


# # 查询数据库
# users = User.query.all()
# print(type(users))
# for user in users:
#     print(user)

# user = User.query.get(2)
# print(type(user.id), user.email)

# users = User.query.filter_by(username="guest").first()
# print(users)

# #  删除记录
# db.session.delete(guest)
# db.session.commit()

# users = User.query.all()
# print(type(users))
# for user in users:
#     print(user)

class BooksView(Resource):
    resource_fields = {
        'id': fields.Integer,
        'title': fields.String,
        'author': fields.String,
        'price': fields.Float 
    }
    @marshal_with(resource_fields)
    def get(self):
        book = Book.query.all()
        return book
api.add_resource(BooksView, '/bookstore/api/v1/books')

class BookView(Resource):
    resource_fields = {
        'title': fields.String,
        'author': fields.String,
        'price': fields.Float
    }
    @marshal_with(resource_fields)
    def get(self, author):
        # parser = reqparse.RequestParser()
        # parser.add_argument('author', type=str)
        book = Book.query.filter(Book.author.contains(author)).all()
        return book
api.add_resource(BookView, '/bookstore/api/v1/book/<string:author>')

@app.route('/bookstore/api/v1/books/', methods=['POST'])
def create_task():
    if not request.form or not 'title' in request.form:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.form['title'],
        'author': request.form['author'],
        'price': request.form['price'],
    }
    books.append(book)
    return jsonify({'book': book})


@app.route('/bookstore/api/v1/books/<int:id>', methods=['PUT'])
def update_book(id):
    for book in books:
        if book['id'] == id:
            book['title'] = request.form['title']
            book['author'] = request.form['author']
            book['price'] = request.form['price']
        return jsonify({'books': books})
    abort(400)


@app.route('/bookstore/api/v1/books/<int:id>', methods=['DELETE'])
def delete_task(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return jsonify({'result': True})
    abort(404)
    return jsonify({'result': True})


@app.route('/')
def index():
    return render_template('index.html') # 渲染打包好的React App的页面

if __name__ == '__main__':
    app.run(debug=True)