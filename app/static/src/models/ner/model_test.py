from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing
import numpy as np
from konlpy.tag import Komoran
import pickle
import jpype


class Preprocess:
    def __init__(self, word2index_dic='', userdic=None):
        # 단어 인덱스 사전 불러오기
        if(word2index_dic != ''):
            f = open(word2index_dic, "rb")
            self.word_index = pickle.load(f)
            f.close()
        else:
            self.word_index = None

        # 형태소 분석기 초기화
        self.komoran = Komoran(userdic=userdic)

        # 제외할 품사
        # 참조 : https://docs.komoran.kr/firststep/postypes.html
        # 관계언 제거, 기호 제거
        # 어미 제거
        # 접미사 제거
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ',
            'JX', 'JC',
            'SF', 'SP', 'SS', 'SE', 'SO',
            'EP', 'EF', 'EC', 'ETN', 'ETM',
            'XSN', 'XSV', 'XSA'
        ]

    # 형태소 분석기 POS 태거
    def pos(self, sentence):
        jpype.attachThreadToJVM()
        return self.komoran.pos(sentence)

    # 불용어 제거 후, 필요한 품사 정보만 가져오기
    def get_keywords(self, pos, without_tag=False):
        f = lambda x: x in self.exclusion_tags
        word_list = []
        for p in pos:
            if f(p[1]) is False:
                word_list.append(p if without_tag is False else p[0])
        return word_list

    # 키워드를 단어 인덱스 시퀀스로 변환
    def get_wordidx_sequence(self, keywords):
        if self.word_index is None:
            return []

        w2i = []
        for word in keywords:
            try:
                w2i.append(self.word_index[word])
            except KeyError:
                # 해당 단어가 사전에 없는 경우, OOV 처리
                w2i.append(self.word_index['OOV'])
        return w2i



p = Preprocess(word2index_dic='D:/chatbot-master/train_tools/dict/chatbot_dict.bin',
               userdic='D:/chatbot-master/utils/user_dic1.tsv')


new_sentence = '몸속에 벌레가 잔뜩 보여'
pos = p.pos(new_sentence)
print(pos)
keywords = p.get_keywords(pos, without_tag=True)
new_seq = p.get_wordidx_sequence(keywords)

max_len = 40
new_padded_seqs = preprocessing.sequence.pad_sequences([new_seq], padding="post", value=0, maxlen=max_len)
print("새로운 유형의 시퀀스 : ", new_seq)
print("새로운 유형의 시퀀스 : ", new_padded_seqs)

# NER 예측
model = load_model('fin.h5')
p = model.predict(np.array([new_padded_seqs[0]]))
p = np.argmax(p, axis=-1) # 예측된 NER 인덱스 값 추출

print("{:10} {:5}".format("단어", "예측된 NER"))
print("-" * 50)
# index_to_ner = {1: 'O', 2: 'B_DT', 3: 'B_FOOD', 4: 'I', 5: 'B_OG', 6: 'B_PS', 7: 'B_LC', 8: 'NNP', 9: 'B_TI', 0: 'PAD'}
index_to_ner = {1: 'O', 2: 'B_DIS', 3: 'B_SYM', 4: 'B_SPE', 5: 'B_PART', 6: 'B_SG', 0: 'PAD'}#fin
# index_to_ner = {1: 'O', 2: 'B_DIS', 3: 'B_SPE', 4: 'B_SYM', 5: 'B_PART', 6: 'B_SG', 0: 'PAD'}
for w, pred in zip(keywords, p[0]):
    print("{:10} {:5}".format(w, index_to_ner[pred]))


# 새로운 유형의 시퀀스 :  [39, 214, 117, 194, 404, 3, 2, 9]
# 새로운 유형의 시퀀스 :  [[ 39 214 117 194 404   3   2   9   0   0   0   0   0   0   0   0   0   0
#     0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
#     0   0   0   0]]