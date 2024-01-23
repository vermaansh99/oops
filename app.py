class Person:
    #name
    #age
    #gender
    #static variables
    default_role = "user"
    def __init__(self,name,age,gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self._salary = 10000

    def _sayHello(self):
        print("Hello From Person")





    def speak(self):
        print("My salary is ",self._salary)
        print(f"My Name is {self.name}, I am {self.age} years")


class Admin(Person):
    def __init__(self, name, age, gender,salary) -> None:
        self.salary =salary
        super().__init__(name, age, gender)

    # def showSalary(self):
    #     print("My salary is ",super()._salary)

    
    def fire(self):
        print("I can fire")

class Manager(Admin,Person):

    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender,salary=1000)

    def hire(self):
        print("I can hire")

    





person1 = Person("Sumit",27,"Male") #object creation
person2 = Person("Ansh",22,"Male")
person3 = Person("Saif",30,"Male")

# print(person1.__salary)
admin = Admin("Rahul",25,"Male",20000000)

person1.speak()
person2.speak()


admin.speak()
admin.fire()
admin._sayHello()
manager = Manager("Sammy",27,"Male")

manager.fire()
manager.speak()
manager.hire()
print(manager.default_role)
manager._sayHello()

from flask import Flask,render_template,request,jsonify
from auth.auth import Auth


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create")
def create():
    return render_template("signup.html")

@app.route("/save",methods=["POST"])
def save():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        auth = Auth(email,password,"mongodb://127.0.0.1:27017")
        created = auth.createAccount()
        print("Created ",created)
        if not created:
            return {"error":"Username or Email already exists"}
        
    return "User Created Successfully"


@app.route("/authenticate",methods=["POST"])
def authenticate():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        auth = Auth(email,password,"mongodb://127.0.0.1:27017")
        token = auth.login()
        if token ==-1:
            return {"error":"Username or Email already exists"}
        elif not token:
            return {"error":"Invalid Username/Password"}
        else:
            return {"access_token":token}
        
@app.route("/me",methods=["GET"])
def me():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error":"Unauthorized","message":"Token Required"})
    auth = Auth()
    email = auth.verifyUser(token)

    return {"message":"Access Granted","email":email}

app.run(debug=True)



    
    










