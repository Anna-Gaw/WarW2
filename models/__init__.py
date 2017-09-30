from clcrypto import password_hash


class User:
    
    
    __id = None
    email = None
    username = None
    __hashed_password = None
    cnx = None
    
    
    def __init__(self):
        self.__id = -1
        self.email = ""
        self.username = ""
        self.__hashed_password = ""
        

    
    @property   
    def id(self):
        return self.__id
    
    @property
    def hashed_password(self):
        return self.__hashed_password
    
    
    def set_password(self, raw_password, salt):
        self.__hashed_password = password_hash(raw_password, salt)
        
        
    def save(self):
        if self.__id == -1:
            cursor = self.cnx.cursor()
            sql = """insert into `User` (username, email, hashed_password)
            values(%s, %s, %s)"""  
    
            values = (self.username, self.email, self.__hashed_password)
            cursor.execute(sql, values)
            self.cnx.commit()
            self.__id = cursor.lastrowid
            return True
        
        return False    
        
        
    @staticmethod
    def load_user_by_id(cnx, id):
        sql = """select id, username, email, hashed_password 
                    from warsztaty2.user """  
        cursor = cnx.cursor()
        cursor.execute(sql, (id))
        data = cnx.fetchone()
        cursor.close()
        if data is None :
            return None
        else:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]

            return loaded_user

    @staticmethod
    def load_all_users(cnx):
        sql = """select id,username, email, hashed_password
                   from warsztaty2.user"""
        result = []
        cursor = cnx.cursor()
        cursor.execute(sql)
        date = cursor.fetchall()
        if date is None:
            return None
        else:
            for row in date:
                loaded_user = User()
                loaded_user.__id = row[0]
                loaded_user.username = row[1]
                loaded_user.email = row[2]
                loaded_user.__hashed_password = row[3]
                result.append(loaded_user)
            return result
        
       
       
    
    
    
    