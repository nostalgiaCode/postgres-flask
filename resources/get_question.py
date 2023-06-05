import datetime
import json

import requests
from flask import jsonify, request
from flask_restful import Resource, abort

from db import db
from models.questions import QuestionModel


class GetQuestion(Resource):
    def post(self):
        current_time = datetime.datetime.utcnow()

        try:
            questions_num = request.get_json()['questions_num']
        except KeyError:
            return abort(403, message="invalid JSON")
        
        if type(questions_num) is not int:
            return abort(403, message="questions_num is not a real number")
        
        if questions_num <= 0:
            return abort(403, message="questions_num is not a real number")

        for i in range(questions_num):
            while True:
                question_sample = json.loads(requests.get('https://jservice.io/api/random').text)[0]
                if(QuestionModel.get_question(id=question_sample['id']) is not None):
                    continue
                else:
                    new_question=QuestionModel(id=question_sample['id'], question=question_sample['question'], answer=question_sample['answer'])
                    db.session.add(new_question)
                    db.session.commit()
                    break

        return QuestionModel.get_previous_question(current_time)