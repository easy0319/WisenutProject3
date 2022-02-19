import sys
sys.path.append("..")

import logging
import re
from unittest import result
import numpy as np
import pandas as pd

#INFO : 개발, ERROR : 배포
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s >> %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S')

def matching(pattern, sent):
    p = re.compile(pattern)
    m = p.findall(sent)
    return False if len(m) < 1 else True

def getRule(str, df):
    return df[df['규칙'].apply(matching, args=(str, ))]


def ruleData(query):
    df = pd.read_csv('/Users/easy/programming/wp-3rd/app/static/csv/rule_spe.csv') 
    qus = query.replace(' ', '')
    df_rows = getRule(qus, df)

    name = ''.join(df_rows['규칙'].values).split('|')[0]
    type = df_rows['종류'].values
    msg = df_rows['답변'].values

    if '종료' in type:
        # logging.info(msg[0])
        return msg[0]

    if '품종' in type:
        if '병' in qus:
            qus = name + '질병'
            df_rows = getRule(qus, df)
            msg = df_rows['답변'].values
            # logging.info('[잘 걸리는 질병] : ' + msg[0])
            return msg[0]
        elif '케어' in qus or '키우' in qus or '관리' in qus:
            qus = name + '케어방법'
            df_rows = getRule(qus, df)
            msg = df_rows['답변'].values
            # logging.info('[키우는법] : ' + msg[0])
            return msg[0]
        elif '성격' in qus:
            qus = name + '성격'
            df_rows = getRule(qus, df)
            msg = df_rows['답변'].values
            # logging.info('[성격] : ' + msg[0])
            return msg[0]
        elif '특징' in qus:
            qus = name + '특징'
            df_rows = getRule(qus, df)
            msg = df_rows['답변'].values
            # logging.info('[특징] : ' + msg[0])
            return msg[0]
        else:
            msg = msg[0].split('@')
            msg = ['[' + name + ' ' + i for i in msg]
            # [logging.info('['+name + ' ' + i) for i in msg]
            return '<br/><br/>'.join(msg)
    elif '질병' in type:
        if '증상' in qus:
            qus = name + '증상'
            df_rows = getRule(qus, df)
            msg = df_rows['답변'].values
            # logging.info('[증상] : ' + msg[0])
            return msg[0]
        elif '이유' in qus or '원인' in qus:
            # logging.info(name)
            qus = name + '이유'
            df_rows = getRule(qus, df)
            msg = df_rows['답변'].values
            # logging.info('[원인] : ' + msg[0])
            return msg[0]
        elif '케어' in qus or '관리' in qus:
            qus = name + '케어방법'
            df_rows = getRule(qus, df)
            msg = df_rows['답변'].values
            # logging.info('[케어방법] : ' + msg[0])
            return msg[0]
        else:
            msg = msg[0].split('@')
            msg = ['[' + name + ' ' + i for i in msg]
            # [logging.info('['+name + ' ' + i) for i in msg]
            return '<br/><br/>'.join(msg)
    elif '수술' in type:
        # logging.info('['+name+'] : ' + msg[0])
        return msg[0]
    else:
        # logging.info('죄송합니다. 무슨 말인지 모르겠습니다.')
        return '죄송합니다. 무슨 말인지 모르겠습니다.'