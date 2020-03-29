# -*- coding: utf-8 -*-
import os
from covid19uncle import GlobalCovid19, ThaiCovid19
from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

# สร้างตัวแปรเก็บผลลัพท์จากฟังชั่น
thai = ThaiCovid19()
#print('อัพเดต:', thai)
print('อัพเดต:', thai['อัพเดต'])
print('ผู้ป่วยสะสม:', thai['ผู้ป่วยสะสม'])
print('ผู้ป่วยรายใหม่:', thai['ผู้ป่วยรายใหม่'])
print('ผู้ป่วยรุนแรง:', thai['ผู้ป่วยรุนแรง'])
print('ผู้ป่วยเสียชีวิต', thai['ผู้ป่วยเสียชีวิต'])
print('======')


@app.route('/')
def hello():
    return "Hello, Universe!"

@app.route('/thai')
def thai_covid():
    return jsonify({"thai": thai}), 200


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()


# data = GlobalCovid19()
# print(data['italy'])
# print('total: ',data['italy']['total'])
# print('new_cases',data['italy']['new_cases'])
# print('total_deaths', data['italy']['total_deaths'])
