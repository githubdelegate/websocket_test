
from . import home

@home.route('/')
def index():
    return "home"
    pass