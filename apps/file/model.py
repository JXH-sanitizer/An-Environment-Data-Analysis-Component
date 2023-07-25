from exts import db

class File(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String(20),nullable = False,unique = True)
    password = db.Column(db.String(50),nullable = False)
    phone = db.Column(db.String(11),unique = True,nullable = False)
    isdelete = db.Column(db.Boolean,default = False)

    def __init__(self):
      return self.username