from app import db


class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    report_result_id = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    tx_from = db.Column(db.String(255), nullable=False)
    tx_to = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Float(), nullable=False)
    description = db.Column(db.Text())
    fraud = db.Column(db.Integer(), nullable=False)
    curious = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), 
        onupdate=db.func.current_timestamp())

   def __init__(self, symbol, tx_from, tx_to, quantity, description, fraud, curious):
        self.symbol = symbol
        self.tx_from = tx_from
        self.tx_to = tx_to
        self.quantity = quantity 
        self.description = description
        self.fraud = fraud
        self.curious = cruious

    def __repr__(self):
        return '<Report %r, %r, %r, %r, %r, %r, %r, %r>' % (
                self.id,
                self.symbol,
                self.tx_from,
                self.tx_to,
                self.quantity,
                self.description,
                self.fraud,
                self.curious
        )


class ReportResult(db.Model):
    __tablename__ = 'report_results'

    id = db.Column(db.Integer, primary_key=True)
    tx_to = db.Column(db.String(255), nullable=False)
    total_fraud = db.Column(db.Integer(), nullable=False)
    total_curious = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), 
        onupdate=db.func.current_timestamp())

   def __init__(self, tx_to, total_fraud, total_curious):
        self.tx_to = tx_to
        self.total_fraud = total_fraud
        self.total_curious = total_cruious

    def __repr__(self):
        return '<ReportResult %r, %r, %r>' % (
                self.tx_to,
                self.total_fraud,
                self.total_curious
        )

