from flask import Blueprint, render_template


query_page = Blueprint('query', __name__, template_folder='../templates')


@query_page.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@query_page.route('/queries/<address>', methods=['GET'])
def query_address(address):
    pass

