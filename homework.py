import pymysql
import time

class AddressBook(object):
    def __init__(self,host,port,user,passwd,db,charset):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset

    def create(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.db,
            charset=self.charset
        )
        with conn.cursor() as cursor:
            cursor.execute('create table tb_address (uid int not null auto_increment,username varchar(10) not null,usertel varchar(11) not null,primary key(uid));')
    # 增
    def add(self):
        name = input('请输入要增加的姓名')
        tel = input('请输入要该用户的电话号码')
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.db,
            charset=self.charset
        )
        with conn.cursor() as cursour:
            cursour.execute( 'insert into tb_address (username,usertel) values (%s,%s)',(name,tel))
            conn.commit()
            print('增加联系人成功')
    #删
    def dele(self):
        name = input('请输入要删除的姓名')
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.db,
            charset=self.charset
        )
        with conn.cursor() as cursour:
            cursour.execute("delete from tb_address where username='%s' " %name)
            conn.commit()
            print('删除联系人成功')

    def updata(self):
        res = int(input('修改姓名输入1,修改电话号码输入2'))
        if res == 1:
            oname = input('请输入原来的姓名')
            nname = input('请输入修改后的姓名')
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                charset=self.charset
            )
            with conn.cursor() as cursour:
                cursour.execute("update tb_address set username='%s' where username='%s'; " % (nname,oname))
                conn.commit()
                print('修改联系人成功')
        if res == 2:
            name = input('请输入姓名')
            tel = input('请输入修改后的电话号码')
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                charset=self.charset
            )
            with conn.cursor() as cursour:
                cursour.execute("update tb_address set usertel='%s' where username='%s'; " % (tel,name))
                conn.commit()
                print('修改联系人成功')

    def find(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.db,
            charset=self.charset
        )
        with conn.cursor() as cursor:
            name = input('请输入您要查询的姓名')
            cursor.execute("select username,usertel from tb_address where username='%s'" %(name))
            result = cursor.fetchone()
            nname=result[0]
            tel=result[1]
            print('姓名:%s  电话:%s' %(nname,tel))

    #显示全部
    def show(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.db,
            charset=self.charset
        )
        with conn.cursor() as cursor:
            cursor.execute('select * from tb_address')
            res = cursor.fetchone()
            while res:
                nname = res[1]
                tel = res[2]
                print('姓名:%s  电话:%s' % (nname, tel))
                res = cursor.fetchone()

def main():
    zhulinyi = AddressBook('localhost',3306, 'root','zly1995422','address_book','utf8')
    zhulinyi.create()
    print('*********************************************')
    print('*                                           *')
    print('*                                           *')
    print('*                                           *')
    print('*         欢迎来电黑鬼哥哥的iphone          *')
    print('*                                           *')
    print('*                                           *')
    print('*                                           *')
    print('*********************************************')
    result = True
    while result:
        print('请选择将要进行的操作')
        print('1:增加联系人')
        print('2:删除联系人')
        print('3:修改联系人')
        print('4:查看联系人')
        print('5:查看所有联系人')
        print('6:退出')
        num = int(input('您要进行的操作是:'))
        if num == 1:
            zhulinyi.add()
        elif num == 2:
            zhulinyi.dele()
        elif num == 3:
            zhulinyi.updata()
        elif num == 4:
            zhulinyi.find()
        elif num == 5:
            zhulinyi.show()
        elif num == 6:
            result = False
        time.sleep(2)

if __name__ == '__main__':
    main()