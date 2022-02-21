import csv
from konlpy.tag import Komoran
from random import  *
food_file = 'b_sg.csv'
sent_file = 'new_corpus.csv'
komoran = Komoran(userdic='../../utils/user_dic.tsv')
file = open("05sg_ner.txt", 'w', encoding='utf-8-sig')
with open(food_file, mode='r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        with open(sent_file, mode="r", encoding="utf-8") as qf:
            qreader = csv.reader(qf)
            for qi, qrow in enumerate(qreader):
                sentence = []
                word = row[0].split(':')
                sentence.append(tuple(word))
                q = qrow[0]
                q = q.replace('\ufeff', '')
                pos = komoran.pos(q)
                for p in pos:
                    x = (p[0], 'O', p[1])
                    sentence.append(x)
                # 파일 저장
                raw_q = ";"
                res_q = '$'
                line = ""
                for i, s in enumerate(sentence):
                    raw_q += "{} ".format(s[0])
                    res_q += "{} ".format(s[0])

                    if s[1] == 'B_SG':
                        line += "{}\t{}\t{}\t{}\n".format(i + 1, s[0], 'NNG', s[1])
                    else:
                        line += "{}\t{}\t{}\t{}\n".format(i + 1, s[0], s[2], s[1])
                print(raw_q)
                print(res_q)
                print(line)
                file.write(raw_q + "\n")
                file.write(res_q + "\n")
                file.write(line + "\n")
file.close()