from flask import Flask, render_template,request
app = Flask(__name__,template_folder="htmlPages")

count=0


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inc')
def inc():
    global count
    count +=1
    return render_template('index.html',count=count) 

@app.route('/dec')
def dec():
    global count
    count -=1
    return render_template('index.html',count=count) 

@app.route('/reset')
def reset():
    global count
    count =0
    return render_template('index.html',count=count) 



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 