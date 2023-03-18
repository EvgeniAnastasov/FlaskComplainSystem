from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.complaint import ComplaintManager
from schemas.request_schemas.complaints import ComplaintRequestSchema
from utils.decorators import validate_schema


class ComplaintsResource(Resource):
    @auth.login_required
    @validate_schema(ComplaintRequestSchema)
    def post(self):
        data = request.get_json()
        ComplaintManager.create_complaint(data)
