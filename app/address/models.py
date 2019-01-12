from app import db


class Address(db.Model):
    __tablename__ = 'addresses'

   id = db.Column(db.Integer, primary_key=True)
   address = db.Column(db.String(255), nullable=False)
   reported_count = db.Column(db.Integer(), nullable=False)
   score = db.Column(db.Float(), nullable=False)
   status = db.Column(db.Integer(), nullable=False)
   created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
   updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), 
           onupdate=db.func.current_timestamp())

   def __init__(self, address, reported_count, score, status):
        self.address = address
        self.reported_count = reported_count
        self.score = score
        self.status = status

    def __repr__(self):
        return '<Address %r, %r, %r, %r, %r>' % (
                self.id,
                self.address,
                self.reported_count,
                self.score,
                self.status
        )

