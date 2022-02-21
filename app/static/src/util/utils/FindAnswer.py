class FindAnswer:
    def __init__(self, db):
        self.db = db
# %%
    # 검색 쿼리 생성
    def _make_query(self, ner_tags): #intent_name = kind, ner_tags = rule
        sql = "select * from sym_info_data"
        if ner_tags != None:
            sql = sql + " where b_sym='{}' ".format(ner_tags)

        # elif ner_tags != None:
        #     where = ' where b_sym="%s" ' % ner_tags
        #     if (len(ner_tags) > 0):
        #         where += 'and ('
        #         for ne in ner_tags:
        #             where += " ner like '%{}%' or ".format(ne)
        #         where = where[:-3] + ')'
        #     sql = sql + where

        # 동일한 답변이 2개 이상인 경우, 랜덤으로 선택
        # sql = sql + " order by rand() limit 1"
        return sql

    # 답변 검색
    def search(self, ner_tags):
        global a
        # 의도명, 개체명으로 답변 검색
        a=[]
        sql = self._make_query(ner_tags)
        answers = self.db.select_all(sql)
        for answer in answers:
            a.append(answer['answer1'])
            
# %%
        # 검색되는 답변이 없으면 의도명만 검색
        # if answer is None:
        #     sql = self._make_query(intent_name, None)
        #     answer = self.db.select_all(sql)

        return a
# %%
    # NER 태그를 실제 입력된 단어로 변환
    def tag_to_word(self, ner_predicts):
        global tag_name
        for word, tag in ner_predicts:

            # 변환해야하는 태그가 있는 경우 추가
            if tag == 'B_SYM':
                # answer = answer.replace(tag, word)
                tag_name = word
                break

        # answer = answer.replace('{', '')
        # answer = answer.replace('}', '')
        return word

# %%

# %%


