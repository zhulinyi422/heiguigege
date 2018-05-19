import pymysql

def main():


        table = 'student'
        sql = 'insert into %s' % (table)
        print(sql +'(username,usertel) values (%s,%s)')
if __name__ == '__main__':
    main()
# table = 'student'
# sql = 'insert into %s' %(table)
#  cursour.execute( sql +'(username,usertel) values (%s,%s)',(name,tel))