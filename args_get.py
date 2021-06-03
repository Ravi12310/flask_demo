### To send a data through google


from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route('/ravi_function1')
def url_test1():
    test1 = request.args.get('val1')
    test2 = request.args.get('val2')
    test3 = test1+test2
    return '''<h1> my result is : {}</h1>'''.format(test3)


if __name__ == '__main__':
    app.run()