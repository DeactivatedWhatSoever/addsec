from flask import Blueprint, render_template


report_page = Blueprint('report', __name__, template_folder='../templates')


@report_page.route('/reports/new', methods=['GET'])
def new_report():
    return render_template("new_report.html")


@report_page.route('/reports', methods=['POST'])
def post_report():
    pass

