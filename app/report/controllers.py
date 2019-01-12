from flask import Blueprint, render_template, jsonify
from .models import Report, ReportResult
from app import db
from sqlalchemy import func, text

report_page = Blueprint('report', __name__, template_folder='../templates')

def add_blacklist(tx_from, tx_to, fraud, curious):
	r = Report(
			symbol='ETH',
			tx_from=tx_from,
			tx_to=tx_to,
			quantity=0, 
			description='Blacklist',
			fraud=fraud,
			curious=curious
		)
	db.session.add(r)
	db.session.commit()

def add_report_result(data):
	r = ReportResult(
			tx_to=data[0],
			total_fraud=data[1],
			total_curious=data[2],
		)
	db.session.add(r)
	db.session.commit()

@report_page.route('/reports/new', methods=['GET'])
def new_report():
	# rows = eval(open('/app/src/app/report/blacklist.json', 'r').read())
	# for row in rows:
	# 	add_blacklist('', row, 1, 0)
	# 	for sub in rows[row]:
	# 		add_blacklist(row, sub, 0, 1)

	return render_template("new_report.html")


@report_page.route('/reports', methods=['GET'])
def post_report():
	# sql = text('SELECT tx_to, SUM(fraud), SUM(curious) FROM reports GROUP BY tx_to ORDER BY 1')
	# result = db.engine.execute(sql)
	# for row in result:
	# 	add_report_result(row)

	return jsonify([report_result.serialize() for report_result in ReportResult.query.all()])
