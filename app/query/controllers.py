from flask import Blueprint, render_template, jsonify
from .models import Query, QueryResult
from app.report.models import Report, ReportResult
from app import db
from random import randint

import math as m


query_page = Blueprint('query', __name__, template_folder='../templates')


def get_score(address):
	if len(address) != 42:
                print('what',len(address))
                return 'Address not formal.'
	report_result = ReportResult.query.filter_by(tx_to=address).first()
	if not report_result:
		return 'Address is safe!'
	if report_result.total_fraud == 1:
		return '100 점'
		
	bCuriousNum = report_result.total_curious
	bFraudNum = report_result.total_fraud
	# bCuriousScore # 구해야 함
	# bFraudScore # 구해야 함

	## base score의 curious 구하기
	### 정규화를 위한 avg(궁금)의 y값 구하기
	### 이 y값으로 나눠주면 정규화 할 수 있음

	a = 0.2
	b = 0
	c = 2
	d = 100
	g = 50
	x = 1.2569

	y1 = g/(1+d*m.exp(-a*x)) + m.log(c*x, 10) + b

	if bCuriousNum == 0:
		bCuriousScore = 0
	elif bCuriousNum >= x:
		bCuriousScore = 100
	else:    
		y2 = g/(1+d*m.exp(-a*bCuriousNum)) + m.log(c*bCuriousNum, 10) + b
		bCuriousScore = (y2/y1)*100
	## base score의 fraud 구하기
	bFraudScore = bFraudNum * randint(1, 100)
	## base score 구하기
	bScore = (bCuriousScore + bFraudScore)/2
	# depth score 구하기
	dCuriousNum = 0
	dFraudNum = 0
        
	reports = Report.query.filter_by(tx_to=address).all()
	if reports:
		for report in reports:
			dCuriousNum += report.curious #주소값에따라 다름
			dFraudNum += report.fraud #주소값에따라 다름

	# dCuriousScore # 구해야 함
	# dFraudScore # 구해야 함
	## depth score의 curious 구하기
	### 정규화를 위한 avg(궁금)의 y값 구하기
	### 이 y값으로 나눠주면 정규화 할 수 있음
	a = 0.2
	b = 0
	c = 2
	d = 100
	g = 50
	x = 1.2569

	y1 = g/(1+d*m.exp(-a*x)) + m.log(c*x, 10) + b
	if dCuriousNum == 0:
		dCuriousScore = 0
	elif dCuriousNum >= x:
		dCuriousScore = 100
	else:    
		y2 = g/(1+d*m.exp(-a*dCuriousNum)) + m.log(c*dCuriousNum, 10) + b
		dCuriousScore = (y2/y1)*100

	## depth score의 fraud 구하기
	dFraudScore = dFraudNum * 100
	## depth score 구하기
	dScore = (dCuriousScore + dFraudScore)/2
	# 최종 스코어 구하기
	resultScore = (bScore+ dScore)/2
	return f'{int(resultScore):d} 점'


@query_page.route('/', methods=['GET'])
def index():
	return render_template("index.html")


@query_page.route('/queries/<address>', methods=['GET'])
def query_address(address):
        """
        Example: curl localhost:8080/queries/1234
        """
        return get_score(address)

