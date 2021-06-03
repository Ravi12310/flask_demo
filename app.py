from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
   if (request.method=='POST'):
       operation=request.form['operation']
       num1=int(request.form['num1'])
       num2 = int(request.form['num2'])
   if(operation=='add'):
       r=num1+num2
       result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
   if (operation == 'subtract'):
       r = num1 - num2
       result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
   if (operation == 'multiply'):
       r = num1 * num2
       result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
   if (operation == 'divide'):
       r = num1 / num2
       result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
   return render_template('results.html',result=result)

""""@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)



@app.route('/ravi',methods=['POST'])    ## calling for API from postman/SOAPUI
def math_ravi():
    if (request.method=='POST'):
        num0 = request.json['num0']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = num0+num1+num2
        return jsonify(result)


@app.route('/ravi1',methods=['POST'])    ## calling for API from postman/SOAPUI
def math_ravi1():
    if (request.method=='POST'):
        num0 = request.json['num0']
        num1 = str(request.json['num1'])
        num2 = str(request.json['num2'])
        result = num0+num1+num2
        return jsonify(result)




@app.route('/ravi2',methods=['POST'])   ## calling from API
def math_ravi2():
    if (request.method=='POST'):
        num0 = request.json['num0']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = num0+num1+num2
        return jsonify((result))



@app.route('/ravi3',methods=['POST'])    ## calling from api
def ravi3():
    if (request.method=='POST'):
        num0 = request.json['num0']
        result = num0
        return jsonify(num0 + "kumar" + "royal")



@app.route('/ravi4',methods=['POST'])   ## calling from api
def ravi4():
    if request.method=='POST':
        name = request.json['my name']
        email_id = request.json['my email id']
        phone_number = request.json['my phone_number']
        return jsonify(name  +  email_id  +  str(phone_number))

@app.route('/ravi5',methods=['POST'])   ## calling from postman
def ravi5():
    if request.method=='POST':
        name = request.json['my name']
        email = request.json['my email']
        ph_number = request.json['my ph number']
        return jsonify(name+email+str(ph_number))"""






### To send a data through google
## To add the data in the google url
@app.route('/ravi_function')
def url_test():
    test1 = request.args.get('val1')
    test2 = request.args.get('val2')
    test3 = int(test1) + int(test2)
    return '''<h1> my result is : {}</h1>'''.format(test3)





if __name__ == '__main__':
    app.run()



