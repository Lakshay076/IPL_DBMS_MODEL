from flask_mysqldb import MySQL, MySQLdb

mysql = MySQL()
class Admin:
    def __init__(self, admin_id, username, email, image_file, password):
        self.id = admin_id
        self.username = username
        self.email = email
        self.image_file = image_file
        self.password = password
        
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    @classmethod
    def get(cls, admin_id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute("SELECT * FROM ADMIN WHERE Admin_ID = %s", (admin_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return cls(result['Admin_ID'], result['username'], result['email'], result['image_file'], result['password'])
        return None

    
