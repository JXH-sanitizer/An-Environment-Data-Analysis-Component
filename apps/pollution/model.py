from exts import db

class Pollution(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    CAS = db.Column(db.String(20),nullable=False)
    pollutionname = db.Column(db.String(30),nullable=False)
    location = db.Column(db.String(200),nullable=False)
    unit = db.Column(db.String(15),nullable=False)
    conc = db.Column(db.String(20),nullable=False)
    isdelete = db.Column(db.Boolean,default=False)

    def __str__(self):
        return self.pollutionname