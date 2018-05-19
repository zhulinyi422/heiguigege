# 将txt文本中的信息录入到数据库中
import pymysql

def main():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='zly1995422',
        db='address_book',
        charset='utf8'
    )
    try:
            path = 'user_mes.txt'

            for tline in open(path,'rb'):
                line = tline.decode('utf-8')
                list1 = line.split(' ')
                # print(list1[0])
                # print(list1[1])
                # print(list1[2].rsplit('/r'))
                uname = list1[0]
                utel = list1[1]
                umail = list1[2]
                with conn.cursor() as cursor:
                    cursor.execute('create table if not exists address_bk (uid int not null auto_increment,username varchar(10) not null,usertel varchar(11) not null,email varchar(20),primary key(uid));')
                    cursor.execute('insert into address_bk (username,usertel,email)values (%s,%s,%s)',
                                       (uname, utel, umail))
                    conn.commit()

            print('录入成功')


    # except:
    #     conn.rollback()
    finally:
        conn.close()





if __name__ == '__main__':
    main()




