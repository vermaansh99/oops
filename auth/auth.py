from db.db import Database
import bcrypt
import jwt
import datetime
from jwt.exceptions import InvalidTokenError
AUTH_SECRET = '#HAS#SECRET'

class Auth(Database):
    def __init__(self,email="",password="",connection_string="") -> None:
        self.email = email
        self.password = password
        super().__init__(connection_string)

    def createAccount(self):
        client = self.GetClient()
        db = client["profile-service"]
        collection = db["users"]

        # first check existing

        isExist = collection.find_one({"email":self.email})
        if isExist:
            return None

        salt = bcrypt.gensalt()
        password =  bcrypt.hashpw(self.password.encode('utf-8'), salt)
        return collection.insert_one({"email":self.email,"password":password})
    
    def login(self):
        client = self.GetClient()
        db = client["profile-service"]
        collection = db["users"]
        
        #check existence
        User = collection.find_one({"email":self.email})
        if not User:
            return -1
        
        #now verify password

        user_password = User["password"]
        incoming_password = self.password.encode('utf-8')

        verified = bcrypt.checkpw(incoming_password,user_password)
        if not verified:
            return 0
        payload = {
        'user_id': self.email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=600),
        'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, AUTH_SECRET, algorithm='HS256')
        return token
    
    
    def verifyUser(self,token):
        try:

            decoded_token = jwt.decode(token, AUTH_SECRET, algorithms=["HS256"])
            email = decoded_token['user_id']
            return email
        except jwt.ExpiredSignatureError:
        # Handle expired token, e.g., by returning an appropriate message
            return "Token expired. Please log in again."
        except InvalidTokenError:
        # Handle invalid token, e.g., by returning an appropriate message
            return "Invalid token. Please try again."
        

