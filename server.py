# -*- coding: iso-8859-15 -*-


from flask import Flask, request
app = Flask(__name__)

from flask import render_template
# este codigo controla los errores de campos ausentes
def process_missingFields(campos, next_page):
    """
    :param campos: Lista de Campos que faltan
    :param next_page: ruta al pulsar botón continuar
    :return: plantilla generada
    """
    return render_template("missingFields.html", inputs=campos, next=next_page)


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/home', methods=['GET'])
def home():
    return app.send_static_file('home.html')


@app.route('/login', methods=['GET'])
def login():
    return app.send_static_file('login.html')


@app.route('/signup', methods=['GET'])
def signup():
    return app.send_static_file('signup.html')


@app.route('/processLogin', methods=['GET', 'POST'])
def processLogin():
       missing = []
       fields = ['email', 'passwd', 'login_submit']
       for field in fields:
              value = request.form.get(field, None)
              if value is None:
                  missing.append(field)
       if missing:
              return process_missingFields(missing, "/login")


       return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<link href="static/css/socialed-style.css" rel="stylesheet" type="text/css"/>' \
           '<title> Home - SocNet </title>' \
           '</head>' \
           '<body> <div id ="container">' \
		   '<a href="/"> SocNet </a> | <a href="home"> Home </a> | <a href="login"> Log In </a> | <a href="signup"> Sign Up </a>' \
           '<h1>Data from Form: Login</h1>' \
	       '<form><label>email: ' + request.form['email'] + \
	       '</label><br><label>passwd: ' + request.form['passwd'] + \
           '</label></form></div></body>' \
           '</html>'


@app.route('/processSignup', methods=['GET', 'POST'])
def processSignup():
       missing = []
       fields = ['nickname', 'email', 'passwd','confirm', 'signup_submit']
       for field in fields:
              value = request.form.get(field, None)
              if value is None:
                     missing.append(field)
       if missing:
              return process_missingFields(missing, "/signup")

       return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<link href="static/css/socialed-style.css" rel="stylesheet" type="text/css"/>' \
           '<title> Inicio - SocialED </title>' \
           '</head>' \
           '<body> <div id ="container">' \
		   '<a href="/"> SocialED </a> | <a href="home"> Home </a> | <a href="login"> Log In </a> | <a href="signup"> Sign Up </a>' \
           '<h1>Data from Form: Sign Up</h1>' \
           '<form><label>Nickame: ' + request.form['nickname'] + \
	       '</label><br><label>email: ' + request.form['email'] + \
	       '</label><br><label>passwd: ' + request.form['passwd'] + \
	       '</label><br><label>confirm: ' + request.form['confirm'] + \
           '</label></form></div></body>' \
           '</html>'


@app.route('/processHome', methods=['GET', 'POST'])
def processHome():
	missing = []
	fields = ['message', 'last', 'post_submit']
	for field in fields:
		value = request.form.get(field, None)
		if value is None:
			missing.append(field)
	if missing:
		return process_missingFields(missing, "/home")

	return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<link href="static/css/socialed-style.css" rel="stylesheet" type="text/css"/>' \
           '<title> Inicio - SocialED </title>' \
           '</head>' \
           '<body> <div id="container">' \
		   '<a href="/"> SocialED </a> | <a href="home"> Home </a> | <a href="login"> Log In </a> | <a href="signup"> Sign Up </a>' \
           '<h1>Hi, How are you?</h1>' \
                	'<form action="processHome" method="post" name="home"> ' \
			'<label for="message">Say something:</label><div class="inputs">' \
			'<input id="message" maxlength="128" name="message" size="80" type="text" required="true" value=""/>' \
			'<input id="last" type="hidden" name="last" required="true" value="' + request.form['last'] + '<br>'+ request.form['message'] + '">' \
	                 '</div>' \
                    	'<div class="inputs">' \
                        '<input id="post_submit" name="post_submit" type="submit" value="Post!"/>' \
           		'<br><br>Previous Posts: <br>' + request.form['last'] + '<br>' +request.form['message'] + \
                	'</form>' \
            		'</div></div>' \
           '</body>' \
           '</html>'


#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, port=55555)
    

