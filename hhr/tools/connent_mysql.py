import pymysql


def select_record():
    db = pymysql.connect(host='106.75.65.223', user='hhr', passwd='hhr2019@hhrchina.com', db='hhrchina_test_2.0', port=4040)
    cursor = db.cursor()

    sql = "select mobilePhone from t_user where userId = '1000033'"

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            first_name = row[0]
            # last_name = row[1]
            # age = row[2]
            # income = row[3]
            # create_time = row[4]
            print(first_name)
    except Exception as e:
        print('查询数据失败 %s' % e)
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    select_record()