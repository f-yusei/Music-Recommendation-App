from mlask import MLAsk

def Judge_emotion(texts):
    #辞書を指定
    emotion_analyzer = MLAsk('-d /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd')
    #感情分析
    result = emotion_analyzer.analyze(texts[0])
    if result['emotion'] == None:
        print("文を書き直してください")
    else:
        result_final = result['representative']
        #感情を分類
        if result_final[0] == 'iya' or result_final[0] == 'kowa' or result_final[0] == 'aware':
            print(result_final[0])
            return 'ネガティブな落ち着き'
        elif result_final[0] == 'suki' or result_final[0] == 'yasu':
            print(result_final[0])
            return 'ポジティブな落ち着き'
        elif result_final[0] == 'odoroki' or result_final[0] == 'ikari' or result_final[0] == 'haji':
            print(result_final[0])
            return 'ネガティブな激しさ'
        else:
            print(result_final[0])
            return 'ポジティブな激しさ'

if __name__ == '__main__':
    Judge_emotion()
