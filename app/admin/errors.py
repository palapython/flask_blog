from flask import render_template
from . import admin

@admin.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@admin.app_errorhandler(500)
def internet_server_error(error):
    return render_template('500.html'), 500