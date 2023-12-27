from flask import Flask, request, render_template
import gmail1
from gmail1 import my_function

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/call_python_function', methods=['POST','GET'])
def call_python_function():

    email1 = request.form['email1']
    # print(email1)
    email2 = request.form['email2']
    # print("hi")
    # Call the Python function from the 'gmail.py' file
    paragraph_text = gmail1.my_function(email1, email2)
  
    # Render the result directly in the HTML template
    return render_template('index.html',paragraph_text=paragraph_text)
if __name__ == '__main__':
    app.run(debug=True,port=5500)

