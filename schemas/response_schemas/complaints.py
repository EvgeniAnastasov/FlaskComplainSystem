from marshmallow import fields

from models import State
from schemas.base import ComplaintBase


class ComplaintResponse(ComplaintBase):
    id = fields.Integer(required=True)
    created_at = fields.DateTime(required=True)
    status = fields.Enum(State, by_value=True)
    user_id = fields.Integer(required=True)
    # Todo: nest user inside schema
