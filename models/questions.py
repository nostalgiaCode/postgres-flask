import datetime

from db import db


class QuestionModel(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    question = db.Column(db.String(300))
    answer = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(timezone=True), default = None)

    def __init__(self, id, question, answer):
        self.id = id
        self.question = question
        self.answer = answer
        self.created_at = datetime.datetime.utcnow()

    def get_question(id):
        if id is not None:
            return QuestionModel.query.filter_by(id=id).first()
        
    def get_previous_question(time):
        sample = QuestionModel.query.\
            filter(QuestionModel.created_at < time).\
                order_by(QuestionModel.created_at.desc()).first()
        if sample is None:
            return None
        else:
            return sample.question