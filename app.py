
from flask import Flask, jsonify, render_template, request,Response
import subprocess




# setting flags to redirect to only login page if admin is not login
accessFlag=0


# Flask APP - this is the flask object
app = Flask(__name__)

# START LOGIN PAGE


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutUs')
def about():
    return render_template('aboutUs.html')


@app.route('/loginPage')
def login():
    return render_template('loginPage.html')




@app.route('/air')
def air():
    # if accessFlag==0:
    #     return render_template("loginPage.html")
    return render_template('air.html')

@app.route('/water')
def water():
    # if accessFlag==0:
    #     return render_template("loginPage.html")
    return render_template('water.html')

@app.route('/deforestation')
def deforestation():
    # if accessFlag==0:
    #     return render_template("loginPage.html")
    return render_template('deforestation.html')



@app.route('/climate')
def climate():
    # global accessFlag
    # if accessFlag==0:
    #     return render_template("loginPage.html")
    
    return render_template('climate.html')



    

# MAIN Function starts here
if __name__ == '__main__':
	# run! Set multiple Threading to TRUE, Host to 0.0.0.0 (to access outside localhost), Port to 8080, and Dubugging to TRUE
	app.run(threaded=True, host='0.0.0.0', port=2020, debug=True)
