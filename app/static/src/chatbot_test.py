from config.DatabaseConfig import *
from util.utils.Database import Database
from util.utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel
from models.ner.NerModel import NerModel
from util.utils.FindAnswer import FindAnswer



# 전처리 객체 생성
p = Preprocess(word2index_dic = r'C:\Users\kty\prj\WisenutProject3\app\static\train_tools\dict\chatbot_dict.bin',
               userdic = r'C:\Users\kty\prj\WisenutProject3\app\static\src\utils\user_dic1.tsv')

# 질문/답변 학습 디비 연결 객체 생성
db = Database(
    host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
)
db.connect()    # 디비 연결

query = "우리 강아지가 토를 해요"

# 의도 파악
intent = IntentModel(model_name=r'C:\Users\kty\prj\WisenutProject3\app\static\src\models\intent\intent_model.h5', proprocess=p)
predict = intent.predict_class(query)
intent_name = intent.labels[predict]

# 개체명 인식
ner = NerModel(model_name = r'C:\Users\kty\prj\WisenutProject3\app\static\src\models\ner\ner_model_test_fin999.h5', proprocess=p)
predicts = ner.predict(query)
ner_tags = ner.predict_tags(query)

print("질문 : ", query)
print("=" * 100)
print("의도 파악 : ", intent_name)
print("개체명 인식 : ", predicts)
print("답변 검색에 필요한 NER 태그 : ", ner_tags)
print("=" * 100)

# 답변 검색

try:
    f = FindAnswer(db)
    # answer_text, answer_image = f.search(intent_name, ner_tags)
    b_sym = f.tag_to_word(predicts)
    chk = f'말씀하신 증상(부위)이 {b_sym}이신가요?'
    answer1 = f.search(b_sym)
    
except:
    chk = "죄송해요 무슨 말인지 모르겠어요"

print("답변 : ", chk)
print("답변 : ", answer1)


db.close() # 디비 연결 끊음