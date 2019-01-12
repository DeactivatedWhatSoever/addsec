from app import db


class Report(db.Model):
    __tablename__ = 'reports'

   id = db.Column(db.Integer, primary_key=True)
   symbol = db.Column(db.String(10), nullable=False)
   tx_hash = db.Column(db.String(255), nullable=False)
   tx_at = db.Column(db.DateTime(), nullable=False)
   tx_from = db.Column(db.String(255), nullable=False)
   tx_to = db.Column(db.String(255), nullable=False)
   quantity = db.Column(db.String(255), nullable=False)
   description = db.Column(db.Text())
   created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
   updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), 
           onupdate=db.func.current_timestamp())

   def __init__(self, symbol, tx_hash, tx_at, tx_from, tx_to, quantity, description):
        self.symbol = symbol
        self.tx_hash = tx_hash
        self.tx_at = tx_at
        self.tx_from = tx_from
        self.tx_to = tx_to
        self.quantity = quantity 
        self.description = description

    def __repr__(self):
        return '<Report %s, >' % (
                self.id,
                self.symbol,
                self.tx_hash,
                self.tx_at,
                self.tx_from,
                self.tx_to,
                self.quantity,
                self.description
        )

