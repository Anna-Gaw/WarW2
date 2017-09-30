from models import User
from clcrypto import generate_salt
from MySQLdb import connect




def conn():
    cnx = connect(user="root", password="coderslab", 
                  host="localhost", database = "warsztaty2")
    return cnx
    
cnx = conn()
if __name__ == "__main__":
    u = User()
    u.cnx = cnx
    u.username = "Alicja"
    u.email = "ala.ala@o.pl"
    u.set_password ("cmoz333s", generate_salt())
    print(u.id, u.email, u.username, u.hashed_password)
    u.save()
    print(u.id, u.email, u.username, u.hashed_password)
    cnx.close()
    print(u.id, u.email, u.username, u.hashed_password)
    u.load_user_by_id("1")
    
    
    