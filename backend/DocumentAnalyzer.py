import re
import torch
from transformers import BertJapaneseTokenizer, BertModel

class DocumentAnalyzer:
  def __init__(self, model_name='bert-base-japanese-whole-word-masking'):
    self.tokenizer = BertJapaneseTokenizer.from_pretrained(model_name)
    self.model = BertModel.from_pretrained(model_name)
    self.model.eval()
    self.sentence_pattern = re.compile(r'.+?[．|。\s]|.+\Z')
    self.criterion = torch.nn.CosineSimilarity(dim=1)

  def encode(self, sentences):
    indexed_tokens = list(map(lambda s: torch.tensor(self.tokenizer.convert_tokens_to_ids(self.tokenizer.tokenize(s))), sentences))
    tokens_tensor = torch.nn.utils.rnn.pad_sequence(indexed_tokens, batch_first=True)
    with torch.no_grad():
      embeddings, *_ = self.model(tokens_tensor)
    sentence_embeddings = embeddings[:, 0]
    return sentence_embeddings

  def extract_representative_sentence(self, document):
    sentences = self.sentence_pattern.findall(document)
    with torch.no_grad():
      document_embedding = self.encode([document])  # 文書全体のエンベッディング
      sentence_embeddings = self.encode(sentences)  # 文ごとのエンベッディング

      # 最も COS 類似度の高い文を返す
      similarity = self.criterion(document_embedding, sentence_embeddings)
      representatice_sentence_index = similarity.argmax()
    return sentences[representatice_sentence_index]

  def similarity_score(self, sentence_a, document_b):
    sentences_b = self.sentence_pattern.findall(document_b)
    with torch.no_grad():
      sentence_b_embeddings = self.encode(sentences_b)
      sentence_a_embedding = self.encode([sentence_a])

      similarity = self.criterion(sentence_a_embedding, sentence_b_embeddings)
    return similarity, sentences_b

if __name__ == '__main__':
  from pprint import pprint
  analyzer = DocumentAnalyzer()
  document_src = input('Input source text >')
  document_tgt = input('Input target text >')
  print('------ analyzing -----\n')

  representative_sentence_of_src = analyzer.extract_representative_sentence(document_src)
  similarity_score, sentences = analyzer.similarity_score(representative_sentence_of_src, document_tgt)
  print(representative_sentence_of_src)
  pprint(list(zip(similarity_score, sentences)))
