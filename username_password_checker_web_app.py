# Question: create a web app that allows users to submit a username and password
# The app checks if the username exists and the password satisfies three
# conditions as in exercise 81

from flask import Flask, render_template_string, request

app = Flask(__name__)

html = """
  		    <div class="form">
              <form action="{{url_for('sent')}}" method="POST">
  			        <input title="Your email address will be safe with us." placeholder="Enter username" type="text" name="username" required> 
  			        <br>
  			        <input title="Your email address will be safe with us." placeholder="Enter password" type="text" name="password" required> 
  			        <br>
                    {{message|safe}}
                <button class="go-button" type="submit"> Submit </button>
  		      </form>
            </div>
"""

@app.route("/")
def index():
    return render_template_string(html)

@app.route("/sent", methods=['GET', 'POST'])
def sent():
    line = None
    if request.method == 'POST':
        while True:

            username = request.form['username']

            with open('usernames.txt', 'r') as file:
                usernames = file.read()
                # usernames = file.readlines()
                # usernames = [u.strip('\n') for u in users]

            if username in usernames:
                print("Username exists!")
                continue

            else:
                print("Username is fine.")
                break

        while True:

            messages = []
            password = request.form['password']

            if not any(ch.isdigit() for ch in password):
                messages.append("Password must contain at least one number!")

            if not any(ch.isupper() for ch in password):
                messages.append("Password must contain at least one uppercase letter!")

            if len(password) < 5:
                messages.append("Password must have at least 5 characters!")

            if len(messages) == 0:
                print("Password is fine.")
                break

            else:
                return render_template_string(html, message = "Please check your password!")

        return render_template_string(html, message = "Success" + "<br>")

if __name__ == "__main__":
    app.run(debug = True)