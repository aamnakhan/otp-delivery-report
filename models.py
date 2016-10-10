from otpApp import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgres import UUID
import uuid
import psycopg2
import datetime


db = SQLAlchemy(app)

class OtpDelivery(db.Model):
    __tablename__ = 'otp_realtime_delivery'
    id = db.Column(UUID, primary_key=True, default=lambda: uuid.uuid4().hex)
    created_at = db.Column(db.DateTime, nullable=False)
    sms_id = db.Column(db.String(50))
    status = db.Column(db.String(50))
    cause = db.Column(db.String(50))
    user_phone_number_wcountrycode = db.Column(db.String(50))
    user_phone_number = db.Column(db.String(50))
    group_name = db.Column(db.String(50))
    error_code = db.Column(db.String(50))
    delivery_timestamp = db.Column(db.DateTime)
    def __init__(self, created_at, sms_id, status, cause, user_phone_number_wcountrycode, user_phone_number, group_name, error_code, delivery_timestamp):
        self.created_at = created_at
        self.sms_id = sms_id
        self.status = status
        self.cause = cause
        self.user_phone_number_wcountrycode = user_phone_number_wcountrycode
        self.user_phone_number = user_phone_number
        self.group_name = group_name
        self.error_code = error_code
        self.delivery_timestamp = delivery_timestamp

db.create_all()
db.session.commit()
