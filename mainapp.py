__author__ = 'nk'
from flask import Flask
import os
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = 'my precious'
app.config['SESSION_TYPE'] = 'filesystem'

# Pull in URL dispatch routes
import urls
#
# if os.getenv('FLASK_CONF') == 'TEST':
#     app.config.from_object('application.settings.Testing')
#
# elif 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Dev'):
#     # Development settings
#     app.config.from_object('settings.Development')
#     # Flask-DebugToolbarx
#     #toolbar = DebugToolbarExtension(app)
#
#     # Google app engine mini profiler
#     # https://github.com/kamens/gae_mini_profiler
#     app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
#
# else:
#     app.config.from_object('settings.Production')

# Enable jinja2 loop controls extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

if __name__ == '__main__':
    app.run(debug=True)
