import pymysql
#from config.DatabaseConfig import * # DB 접속 정보 불러오기
DB_HOST = "127.0.0.1"
DB_USER = "homestead"
DB_PASSWORD = "secret"
DB_NAME = "homestead"

def DatabaseConfig():
    global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    # 테이블 생성 sql 정의

    ## rule
    # sql = '''
        # CREATE TABLE IF NOT EXISTS `dog_info_data` (
        # `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
        # `kind` VARCHAR(45) NULL,
        # `rule` TEXT NOT NULL,
        # `answer` TEXT NOT NULL,
        # PRIMARY KEY (`id`))ENGINE=InnoDB DEFAULT CHARSET=utf8;
    # '''

    ## ner
    # sql = '''
    #   CREATE TABLE IF NOT EXISTS `sym_info_data` (
    #   `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    #   `intent` VARCHAR(45) NULL,
    #   `ner` VARCHAR(45) NULL,
    #   `chk` VARCHAR(100) NULL,
    #   `b_sym` VARCHAR(45) NULL,
    #   `answer1` TEXT NOT NULL,
    #   `answer2` TEXT NOT NULL,
    #   `answer3` TEXT NOT NULL,
    #   PRIMARY KEY (`id`))
    # ENGINE = InnoDB DEFAULT CHARSET=utf8
    # '''

    # 테이블 생성
    with db.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()

