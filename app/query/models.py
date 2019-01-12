from app import db


class Query(db.Model):
    __tablename__ = 'queries'

    id = db.Column(db.Integer, primary_key=True)
    query_result_id = db.Column(db.Integer)
    symbol = db.Column(db.String(255), nullable=False)
    parent_address = db.Column(db.String(255), nullable=False)
    child_address = db.Column(db.String(255), nullable=False)
    current_score = db.Column(db.Float(), nullable=False)
    depth = db.Column(db.Integer, nullable=False)
    fraud = db.Column(db.Integer, nullable=False)
    curious = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), 
           onupdate=db.func.current_timestamp())

    def __init__(self, symbol, parent_address, child_address, current_score, depth, fraud, curious):
        self.symbol = symbol
        self.parent_address = parent_address
        self.child_address = child_address
        self.current_score = current_score
        self.depth = depth
        self.fraud = fraud
        self.curious = curious

    def __repr__(self):
        return '<Query %r, %r, %r, %r, %r, %r, %r, %r, %r>' % (
                self.id,
                self.symbol,
                self.parent_addres,
                self.child_address,
                self.query_count,
                self.final_score,
                self.depth,
                self.fraud,
                self.curious
        )


class QueryResult(db.Model):
    __tablename__ = 'query_results'

    id = db.Column(db.Integer, primary_key=True)
    avg_score = db.Column(db.Float(), nullable=False)
    total_fraud = db.Column(db.Float(), nullable=False)
    total_curious = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), 
           onupdate=db.func.current_timestamp())

    def __init__(self, avg_score, total_fraud, total_curious):
        self.avg_score = avg_score
        self.total_fraud = total_fraud
        self.total_curious = total_curious

    def __repr__(self):
        return '<QueryResult %r, %r, %r>' % (
                self.id,
                self.avg_score,
                self.total_fraud,
                self.total_curious
        )

