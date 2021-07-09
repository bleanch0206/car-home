from flask import Flask,render_template,url_for,redirect,request

app = Flask(__name__)

@app.route("/" ,methods=['POST','GET'])

def index():
    if request.method == 'POST':
        if request.values['send'] == '送出':
            return render_template('carhome.html', name=request.values['user'])
    return render_template('carhome.html',name="")

@app.route("/tow")
def test():
    return redirect(url_for('index'))


if __name__ == "__main__":
	app.run(debug=True)