from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.complaint import ComplaintManager
from models import RoleType
from schemas.request_schemas.complaints import ComplaintRequestSchema
from schemas.response_schemas.complaints import ComplaintResponse
from utils.decorators import validate_schema, permission_required


class ComplaintsResource(Resource):
    @auth.login_required
    @permission_required(RoleType.complainer)
    @validate_schema(ComplaintRequestSchema)
    def post(self):
        data = request.get_json()
        complaint = ComplaintManager.create_complaint(data)
        return ComplaintResponse().dump(complaint), 201
