from flask import Flask, render_template,request,redirect,url_for

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/gallary')
def gallary():
    return render_template('gallary.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/SignUp',methods=['POST','GET'])
def SignUp():
    if request.method =='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        photo = request.form['photo']
        print([fname,lname,email,username,password,photo])
        return render_template('gallary.html')
    return render_template('gallary.html')
if __name__ == "__main__":
    app.run(debug=True)
    
