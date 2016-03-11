from main import app
import views

__author__ = 'GANGESHWAR'

# Home page
app.add_url_rule('/', 'index', view_func=views.index)

# Home page
app.add_url_rule('/home','home', view_func=views.home)

#login url
app.add_url_rule('/login', view_func=views.login, methods=['POST'])

#logout url
app.add_url_rule('/logout',view_func=views.logout)

#users link
app.add_url_rule('/users',view_func=views.users,methods=['GET'])

#signup link
app.add_url_rule('/signup',view_func=views.signup,methods=['GET', 'POST'])

#upload
app.add_url_rule('/upload',view_func=views.upload1)

#submit link
app.add_url_rule('/submit',view_func=views.submit, methods=['GET', 'POST'])

#img
app.add_url_rule('/view/<bkey>',view_func=views.img, methods=['GET', 'POST'])

app.add_url_rule('/planmytravel',view_func=views.planmytravel, methods=['POST', 'GET'])

app.add_url_rule('/profile', view_func=views.profile,methods=['GET', 'POST'])

app.add_url_rule('/plantrip', view_func=views.plantrip,methods=['GET', 'POST'])