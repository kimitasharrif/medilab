# import required modules
import pymysql
from flask_restful import*
from flask import*
from functions import*
import pymysql.cursors

# jwt packages
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

# lab sign up resource

class LabSignup(Resource):
    def post(self):
        data = request.json
        lab_name= data["lab_name"]
        email = data["email"]
        phone = data["phone"]
        permit_id = data["permit_id"]
        password =  data["password"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
        cursor = connection.cursor()
        # sql = "insert into Laboratories  (Lab_name, email, phone,permit_id, password) values(%s,%s,%s,%s,%s)"
        # data = (lab_name, email, phone,permit_id, password)
        # try:
        #     cursor.execute(sql,data)
        #     connection.commit()
        #     return jsonify({"message":"Lab registration success"})
        # except:
        #     connection.rollback()
        #     return jsonify({"message":"LAB NOT REGISTERED"})


        # check_password validity

        rensponse = passwordvalidity(password)
        if rensponse:
            if check_phone(phone):
                # phone is corrrect
                sql = "insert into Laboratories  (Lab_name, email, phone,permit_id, password) values(%s,%s,%s,%s,%s)"
                data = (lab_name, email, encrypt(phone),permit_id, hash_password(password))
                try:
                    cursor.execute(sql,data)
                    connection.commit()
                    code = gen_random
                    send_sms(phone,'''Thank you for joining Medilab. Your secret No:{}. Do not share.'''.format(code))
                    return jsonify({"message":"Lab registration success"})
                except:
                    connection.rollback()
                    return jsonify({"message":"LAB NOT REGISTERED"})



            else:
                # phone not in correct format
                return jsonify({"message":"Invalid format enter +254..."})



        else:
            return jsonify({"message":"rensponse"})    

