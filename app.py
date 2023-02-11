from flask import Flask,request,render_template

app=Flask(__name__)


@app.route("/")
def hello_world():
    
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return "The name is Bond Mr.Bond"
@app.route('/demo',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        num3 = int(request.form['num3'])
        num4 = int(request.form['num4'])
        num1name = int(request.form['num4'])
        result = {"sum":0,"total":0,"item1":num1,"item2":num2,"item3":num3,"item4":num4,'dis':0}
        result["sum"] = num1 + num2 + num3 + num4
        if(result["sum"] > 2000):
            result["total"] = (result["sum"]  - result["sum"]*(20.0/100.0))
            result['dis'] = 20
        elif(result["sum"] > 1000 and result["sum"] < 2000):
            result["total"] = (result["sum"]  - result["sum"]*(15.0/100.0))
            result['dis'] = 15
        else:
            result["total"] = (result["sum"]  - result["sum"]*(10.0/100.0))
            result['dis'] = 10
        return render_template('results.html',result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)




