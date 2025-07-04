from flask import Blueprint, render_template, request, redirect, url_for
from .models import Event
from . import db 

# Homepage blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')