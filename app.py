from flask import Flask,render_template,request,url_for,redirect,session
from flask_session import Session
from werkzeug.utils import secure_filename, send_file, send_from_directory
app=Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/",methods=["GET","POST"])
def englishtext():
    if not session.get("name") :
        return redirect('/login')
    else:
        if request.method == "POST":
            data = request.form["query"]
            # print(data)
            print(data)
            return {"response":data}  
        else:
            return render_template('index.html',name='Session: '+session["name"])

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        session["name"]=request.form.get("email")
        email=request.form.get("email")
        password=request.form.get("password")
        return redirect('/')
    return render_template('login.html',data='')

@app.route("/upload",methods=["GET","POST"])
def upload():
    if not session.get("name"):
        return redirect('/login')
    else:
        if request.method == 'POST':
            f = request.files['file']
            f.save(secure_filename(f.filename))
            print(f.filename)
            return render_template('index.html',success=f.filename)
    return render_template('index.html',data='')

if __name__=="__main__":
    app.run(debug=True)