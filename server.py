from flask import Flask, request, jsonify, render_template
import model # Import your Python function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/submit', methods=['POST'])
def submit():
    # get array if disease
    diseases = request.form.getlist('disease')
    # get array of diet
    diets = request.form.getlist('diet')
    # get array of nutrients
    vitmains = request.form.getlist('vitamin')
    res = model.process(diseases,diets,vitmains)
    print(res)
    return {
        'result': res
    }

if __name__ == "__main__":
    app.run(debug=True)