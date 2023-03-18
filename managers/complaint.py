from db import db
from models import Complaint


class ComplaintManager:
    @staticmethod
    def create_complaint(complaint_data):
        complaint = Complaint(**complaint_data)
        db.session.add(complaint)
        db.session.commit()
