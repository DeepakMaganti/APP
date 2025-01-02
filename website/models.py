from . import db
class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20), nullable = False)
    author = db.Column(db.String(50), nullable = False)
    overview = db.Column(db.String(200), nullable = False)
    image = db.Column(db.String(200))
    url = db.Column(db.String(100))