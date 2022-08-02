#Step1-import
from flask import Flask

#Step2-Create the object
app=Flask(__name__)

#Step3-Define the function and bind it with a route
@app.route('/')
def index():
    return "hello to this application"

@app.route('/about')
def about_us():
    return "This is about us page"


@app.route('/user/<user_name>')
def user_profile(user_name):
    return "Welcome {}!".format(user_name)

#Step4-Run the app
if __name__=='__main__':
    app.run()

