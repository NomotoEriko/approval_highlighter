# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from DocumentAnalyzer import DocumentAnalyzer
# from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
analyzer = DocumentAnalyzer()
# cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:3000"}})

@app.route('/', methods=['GET'])
def analyze():
  document_src = request.args['src']
  document_tgt = request.args['tgt']
  representative_sentence_of_src = analyzer.extract_representative_sentence(document_src)
  similarity_score, sentences = analyzer.similarity_score(representative_sentence_of_src, document_tgt)
  results = {
    'representative_sentence': representative_sentence_of_src,
    'tgt_sentences': sentences,
    'scores': similarity_score.tolist()
  }
  return jsonify(results)

if __name__ == '__main__':
  app.run(debug=False, host="0.0.0.0", port="3000")
