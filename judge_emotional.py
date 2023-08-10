from transformers import pipeline, AutoModelForSequenceClassification, BertJapaneseTokenizer

# 既存のモデルの呼び出し
model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment') 
tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
nlp = pipeline("sentiment-analysis",model=model,tokenizer=tokenizer)

def judge_emotion(texts): 
    output = nlp(texts)
    #ネガポジのスコアを抽出
    if output[0]['label'] == 'ポジティブ':
        emotional_score = output[0]['score']
        emotional_label = output[0]['label']
    else:
        emotional_score = 1 - output[0]['score']
        emotional_label = output[0]['label']
    return [emotional_label,emotional_score] 
if __name__ == "__main__":
    judge_emotion()




