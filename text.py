# 根据用户提示将用户信息录入到数据库中
import pymysql

def main():
    conn = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = 'zly1995422',
        db = 'address_book',
        charset = 'utf8'
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute('create table address_bk (uid int not null auto_increment,username varchar(10) not null,usertel varchar(11) not null,email varchar(20),primary key(uid));')
            res = True
            while res:
                uname = input('请输入用户姓名')
                utel = input('请输入用户电话号')
                umail = input('请输入用户邮箱')
                cursor.execute('insert into address_bk (username,usertel,email)values (%s,%s,%s)',(uname,utel,umail))
                conn.commit()
                result = int(input('是否结束输入,如果终止录入,请输入1,否则请输入0'))
                if result == 1:
                    res = False
            print('录入成功')
    except:
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()