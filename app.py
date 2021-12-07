from flask import Flask,render_template,request,url_for

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def englishtext():
    if request.method == "POST":
        data = request.form["query"]
        # print(data)
        print(data)
        return {"response":data}
    else:
        return render_template('index.html',data='')

if __name__=="__main__":
    app.run(debug=True)