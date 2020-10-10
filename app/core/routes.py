from flask import Blueprint, render_template
import json

blueprint = Blueprint('core', __name__, template_folder = 'templates')

@blueprint.route('/')
def render_index() -> object:
    projects = json.load(open('projects.json'))
    contributions = json.load(open('contributions.json'))
    return render_template('index.html', projects = projects['projects'], contributions = contributions['projects'])
