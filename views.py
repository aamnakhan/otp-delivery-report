from otpApp import app
from flask import request, redirect, url_for, render_template, Response
import datetime
from models import OtpDelivery, db
from sqlalchemy import desc



@app.route('/post/', methods= ['POST'])
def otpResponse():
    sms_id = request.args.get('externalId')
    status = request.args.get('status')
    cause = request.args.get('cause')
    user_phone_number_wcountrycode = request.args.get('phoneNo')
    user_phone_number = user_phone_number_wcountrycode[2:12]
    group_name = request.args.get('grpName')
    error_code = request.args.get('errCode')
    delivery_timestamp_ms = request.args.get('deliveredTS') #captures TS in milliseconds
    delivery_timestamp = getDateTime(delivery_timestamp_ms)
    dump = OtpDelivery(datetime.datetime.utcnow(), sms_id, status, cause, user_phone_number_wcountrycode, user_phone_number, group_name, error_code, delivery_timestamp)
    db.session.add(dump)
    db.session.commit()
    return 'OK'

def getDateTime(longDate): #converts long number to timestamp
     myNumber = float(longDate)/1000 #dividing by 1000 to convert to seconds from milliseconds
     return str(datetime.datetime.fromtimestamp(myNumber).strftime('%Y-%m-%d %H:%M:%S'))


@app.route('/dashboard', methods=['GET'])
def showDashboard():
    results = OtpDelivery.query.with_entities(OtpDelivery.user_phone_number,OtpDelivery.delivery_timestamp,OtpDelivery.status,OtpDelivery.cause,OtpDelivery.error_code).order_by(desc(OtpDelivery.delivery_timestamp))
    return render_template('tables.html',results=results)


@app.route('/search', methods=['GET'])
def getSearchQuery():
    phone = request.args.get('phoneNo')
    return showSearchResults(phone)

def showSearchResults(phone):
    results = OtpDelivery.query.with_entities(OtpDelivery.user_phone_number,OtpDelivery.delivery_timestamp,OtpDelivery.status,OtpDelivery.cause,OtpDelivery.error_code).order_by(desc(OtpDelivery.delivery_timestamp)).filter(OtpDelivery.user_phone_number == phone)
    return render_template('tables.html',results=results)
