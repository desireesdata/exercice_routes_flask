from flask import Flask
from flask import render_template
from .config import Config

app = Flask(__name__,
            template_folder='templates',
            static_folder='statics')
app.config.from_object(Config)

from .routes import generales