from flask import Blueprint, render_template


address_page = Blueprint('address', __name__, template_folder='../templates')


@address_page.route('/', methods=['GET'])
def index():
    return render_template("index.html")

