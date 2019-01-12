from app import db


class Query(db.Model):
    __tablename__ = 'queries'

    id = db.Column(db.Integer, primary_key=True)
    query_score_id = db.Column(db.Integer)
    parent_address = db.Column(db.String(255), nullable=False)
    child_address = db.Column(db.String(255), nullable=False)
    query_count = db.Column(db.Integer, nullable=False)
    final_score = db.Column(db.Float(), nullable=False)
    depth = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), 
           onupdate=db.func.current_timestamp())

    def __init__(self, parent_address, child_address, depth):
        self.parent_address = parent_address
        self.child_address = child_address
        self.depth = depth

    def __repr__(self):
        return '<Query %r, %r, %r, %r, %r, %r>' % (
                self.id,
                self.parent_addres,
                self.child_address,
                self.query_count,
                self.final_score,
                self.depth
        )

class QueryScore(db.Model):
    __tablename__ = 'query_scores'

    id = db.Column(db.Integer, primary_key=True)
    base_score = db.Column(db.Float(), nullable=False)
    applied_score = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), 
           onupdate=db.func.current_timestamp())

    def __init__(self, base_score, applied_score):
        self.base_score = base_score
        self.applied_score = applied_score

    def __repr__(self):
        return '<QueryScore %r, %r, %r>' % (
                self.id,
                self.base_score,
                self.applied_score
        )
