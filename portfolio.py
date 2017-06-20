from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def success():
    return render_template('index.html')


@app.route('/project')
def project():
    return render_template('project.html')



@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')
app.run(debug=True)
