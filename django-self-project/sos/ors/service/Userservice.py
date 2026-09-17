from django.db import connection


class UserService:

    def next_pk(self):
        pk = 0
        cursor = connection.cursor()
        sql = "select max(id) from sos_user"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.close()
        return pk + 1

    def add(self, data):
        id = UserService.next_pk(self)
        firstname = data['firstname']
        lastname = data['lastname']
        loginid = data['loginid']
        password = data['password']
        dob = data['dob']
        address = data['address']

        cursor = connection.cursor()
        sql = "insert into sos_user values(%s, %s, %s, %s, %s, %s, %s)"
        data = (id, firstname, lastname, loginid, password, dob, address)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data['id']
        firstname = data['firstname']
        lastname = data['lastname']
        loginid = data['loginid']
        password = data['password']
        dob = data['dob']
        address = data['address']

        cursor = connection.cursor()
        sql = "update sos_user set firstname = %s, lastname = %s,loginid = %s, password = %s, dob = %s, address = %s where id = %s"
        data = (firstname, lastname, loginid, password, dob, address, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')

    def delete(self, id):
        cursor = connection.cursor()
        sql = "delete from sos_user where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def get(self, id):
        cursor = connection.cursor()
        sql = "select * from sos_user where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "firstname", "lastname", "loginid", "password", "dob", "address")
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def find_by_login(self, loginid):
        cursor = connection.cursor()
        sql = "select * from sos_user where login_id = %s"
        data = (loginid,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "firstname", "lastname", "loginid", "password", "dob", "address")
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def authenticate(self, loginid, password):
        cursor = connection.cursor()
        sql = "select * from sos_user where loginid = %s and password = %s"
        data = (loginid, password)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "firstname", "lastname", "loginid", "password", "dob", "address")
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def search(self, params):
        firstname = params.get('firstname', '')
        dob = params.get('dob', 0)
        page_no = params.get('page_no', 0)
        page_size = params.get('page_size', 0)
        cursor = connection.cursor()
        sql = "select * from sos_user where 1=1"
        if firstname != '':
            sql += " and firstname like '" + firstname + "%%'"
        if dob != 0:
            sql += " and dob = " + str(dob)
        if (page_size > 0):
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "firstname", "lastname", "loginid", "password", "dob", "address")
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res