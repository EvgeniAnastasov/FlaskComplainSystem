from db import db
from managers.auth import auth
from models import Complaint


class ComplaintManager:
    @staticmethod
    def create_complaint(complaint_data):
        current_user = auth.current_user()
        complaint_data["user_id"] = current_user.id
        complaint = Complaint(**complaint_data)
        db.session.add(complaint)
        db.session.commit()
        return complaint
