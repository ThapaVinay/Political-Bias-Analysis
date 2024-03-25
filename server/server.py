from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/predict_bias', methods=['POST'])
def predict_bias():
    text = str(request.form['text'])

    response = jsonify({
        'bias' : util.get_bias(text)
    })  
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting python Flask server for Home price Prediction...")
    util.load_saved_artifacts()
    app.run()