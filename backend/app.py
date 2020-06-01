from flask import Flask, jsonify
# from flask_cors import CORS

app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:3000"}})

@app.route('/')
def home():
  message = {}
  message['message'] = 'Hello World from Flask!'
  return jsonify(results=message)

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port="3000")
