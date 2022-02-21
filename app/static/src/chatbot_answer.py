import sys
sys.path.append("..")

import logging
import re
import json
from unittest import result
import pandas as pd

#db
from sqlalchemy import create_engine

#INFO : 개발, ERROR : 배포
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s >> %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S')

def btnMatching(pattern, sent):
    p = re.compile(pattern)
    m = p.findall(sent)
    return False if len(m) < 1 else True

def btnGetRule(str, df):
    return df[df['answer1'].apply(btnMatching, args=(str, ))]

def btnData(query):
    with open('/Users/easy/programming/wp-3rd/app/static/json/info.json') as Json: doc = json.loads(Json.read())
    # connect DB
    engine = create_engine(f'mysql://{doc["sqlID"]}:{doc["sqlPW"]}@{doc["sqlHOST"]}/{doc["sqlTABLE"]}', convert_unicode=True)
    conn = engine.connect()

    df = pd.read_sql_table('sym_info_data', conn) 

    df_rows = btnGetRule(query, df)

    qns = df_rows['answer1'].values
    pred = df_rows['answer2'].values
    msg = df_rows['answer3'].values

    if pred == 'None':
      pred = '의심되는 질병이 없습니다.'

    result_answer = '[증상]<br/>' + qns + '<br/><br/>[예상되는 질병]<br/>' + pred + '<br/><br/>[대처방법]<br/>' + msg

    return result_answer