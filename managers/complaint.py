from werkzeug.exceptions import BadRequest

from db import db
from managers.auth import auth
from models import Complaint, RoleType, State


class ComplaintManager:
    @staticmethod
    def create_complaint(complaint_data):
        current_user = auth.current_user()
        complaint_data["user_id"] = current_user.id
        complaint = Complaint(**complaint_data)
        db.session.add(complaint)
        db.session.commit()
        return complaint

    @staticmethod
    def get_complains():
        current_user = auth.current_user()
        role = current_user.role
        complaints = role_mapper[role]()
        return complaints

    @staticmethod
    def _get_complainer_complaints():
        current_user = auth.current_user()

        return Complaint.query.filter_by(user_id=current_user.id).all()

    @staticmethod
    def _get_approver_complaints():
        return Complaint.query.filter_by(status=State.pending).all()

    @staticmethod
    def _get_admin_complaints():
        return Complaint.query.filter_by().all()

    @staticmethod
    def approve_complaint(complaint_id):
        ComplaintManager._validate_status(complaint_id)
        Complaint.query.filter_by(id=complaint_id).update({"status": State.approved})
        db.session.commit()

    @staticmethod
    def reject_complaint(complaint_id):
        ComplaintManager._validate_status(complaint_id)
        Complaint.query.filter_by(id=complaint_id).update({"status": State.rejected})
        db.session.commit()

    @staticmethod
    def _validate_status(complaint_id):
        complaint = Complaint.query.filter_by(id=complaint_id).first()
        if not complaint:
            raise BadRequest("No such a complaint")
        if complaint.status != State.pending:
            raise BadRequest("Complaint already processed")


role_mapper = {
    RoleType.complainer: ComplaintManager._get_complainer_complaints,
    RoleType.approver: ComplaintManager._get_approver_complaints,
    RoleType.admin: ComplaintManager._get_admin_complaints,
}
