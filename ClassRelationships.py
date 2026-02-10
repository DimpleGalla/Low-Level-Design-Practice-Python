# 1. ENUMS
'''An enum (short for enumeration) is a special data type that defines a fixed set of named constants. Unlike strings or integers, enums are type-safe, meaning the compiler ensures you can only use values that actually exist in your defined set. They ensure that a variable can only take one out of a predefined set of valid options.'''
'''ENUM ADVANTAGES: Avoid magic values, Improve readability, Enable compiler checks, Support IDE features, Reduce bugs '''
'''ENUM TYPES : Simple Enum, Enum with Properties and Methods'''
# 1.1 Simple Enum
from enum import Enum
class OrderStatus(Enum):
    PLACED="PLACED"
    CONFIRMED="CONFIRMED"
    SHIPPED="SHIPPED"
    DELIVERED="DELIVERED"
    CANCELLED="CANCELLED"
status=OrderStatus.SHIPPED
if status==OrderStatus.SHIPPED:
    print("Your package is on the way")
# 1.2 Enums with Properties and Methods
from enum import Enum
class Coin(Enum):
    PENNY=1
    NICKEL=5
    DIME=10
    QUARTER=25
    def __init__(self,value):
        self.coin_value=value
    def get_value(self):
        return self.coin_value
total= Coin.DIME.get_value()+Coin.QUARTER.get_value()
print(total)
# 2. Class Relationships: Association, Aggregation, Composition, Dependancy, Realization
# 2.1 Association
'''Represents a relationship between 2 independent classes where objects know about each other, their lifecycles are independent and there is no ownership like part-of (like aggregation/composition). Association reflects a "has-a" or "uses-a" relationship. Associated objects are loosely coupled and can exist independently of one another.'''
# 2.1.1 Unidirectional Association
'''One class knows about the other and the other class does not know back'''
# Example - Unidirectional Association
# Order -> Customer where Order knows which customer placed it but the Customer doesn't know about orders
class Customer:
    def __init__(self,name):
        self.name=name
class Order:
    def __init__(self,order_id,customer):
        self.order_id=order_id
        self.customer=customer # unidirectional association
    def show_order(self):
        print(f"Order {self.order_id} placed by {self.customer.name}")
cust=Customer("Dimple")
order=Order(101,cust)
order.show_order()
# 2.1.2 Bidirectional Association
'''Both classes know about each other'''
# Example - Bidirectional Association
# Teacher <-> Student where Teacher knows students and Student knows teacher
class Teacher:
    def __init__(self,name):
        self.name=name
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
class Student:
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher # bidirectional association
        teacher.add_student(self)
teacher=Teacher("David Johnson")
student1=Student("Dimple",teacher)
student2=Student("Sowmya",teacher)
for s in teacher.students:
    print(s.name)
# 2.1.3 One-to-One Association
'''One object ↔ One object'''
# Example - One-to-One Association
# Person ↔ Passport or User ↔ Profile Each person has exactly one passport and vice-versa
class Passport:
    def __init__(self,passport_no):
        self.passport_no=passport_no
class Person:
    def __init__(self,name,passport):
        self.name=name
        self.passport=passport # one-to-one association
passport=Passport("A123456")
person=Person("Dimple",passport)
print(person.passport.passport_no)
# 2.1.4 One-to-Many Association
'''One object ↔ Many objects'''
# Example - One-to-Many Association
# Department -> Employees or Teacher ↔ Students Each Department has many employees but each employee has only one department
class Employee:
    def __init__(self,name):
        self.name=name
class Department:
    def __init__(self,dept_name):
        self.dept_name=dept_name
        self.employees=[]
    def add_employees(self,emp):
        self.employees.append(emp)
dept=Department("Data Science")
emp1=Employee("Alice")
emp2=Employee("Bob")
dept.add_employees(emp1)
dept.add_employees(emp2)
for emp in dept.employees:
    print(emp.name)
# 2.1.4 Many-to-Many Association
'''Many objects ↔ Many objects'''
# Example - Many-to-Many Association
# Student -> Course or Doctor ↔ Patient. A student can take many courses and a course can have many students
class Course:
    def __init__(self,name):
        self.name=name
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
class Student:
    def __init__(self,name):
        self.name=name
        self.courses=[]
    def enroll(self,course):
        self.courses.append(course)
        course.add_student(self)
math=Course("Math")
python=Course("Python")
alice=Student("Alice")
bob=Student("Bob")
alice.enroll(math)
bob.enroll(python)
bob.enroll(math)
for i in bob.courses:
    print(i.name)
# 2.2 Aggregation
'''Aggregation represents a “has-a” relationship with weak ownership. One class(whole) contains another class(part). Contained object can exist independently. If the container is destroyed, the contained object does NOT die
'''
'''Key characteristics:
1. The whole and the part are logically connected.
2. The part can exist independently of the whole.
3. The whole does not own the part.
4. The part can be shared among multiple wholes.
5.  Both the whole and the part can be created and destroyed independently
'''
# All aggregations are associations, but not all associations are aggregations
# 2.2.1 Example 1: Employee can exist without Department - Employees are created outside the department
class Employee:
    def __init__(self,name):
        self.name=name
class Department:
    def __init__(self,dept_name,employees):
        self.dept_name=dept_name
        self.employees=employees # aggregation
    def show_employees(self):
        for emp in self.employees:
            print(emp.name)
emp1=Employee("Laura")
emp2=Employee("Joshua")
dept=Department("Software Development",[emp1,emp2])
dept.show_employees()
# 2.2.2 Example 2: Books can move to another library or exist alone.
class Book:
    def __init__(self,title):
        self.title=title
class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
book1=Book("Clean code")
book2=Book("Design patterns")
library=Library("City library")
library.add_book(book1)
library.add_book(book2)
# 2.2.3 Example 3: Company and Employee (shared object) , shared object is classic aggregation signal
class Employee:
    def __init__(self,name):
        self.name=name
class Company:
    def __init__(self,name):
        self.name=name
        self.employees=[]
    def hire(self,employee):
        self.employees.append(employee)
emp=Employee("Dimple")
company1=Company("Zoox")
company2=Company("BNSF")
company1.hire(emp)
company2.hire(emp)
# 2.2.4 Why Aggregation matters in OOPS
'''
1. Better Design & Loose Coupling: Objects are not tightly bound and are easier to maintain and extend
2. Real World Modeling: Reflects how things actually behave instead of assuming incorrect ownerships
3. Memory & Lifecycle Safety: Prevents accidental deletion of shared objects
4. Promotes Resuablity: Part components are independent and can be reused across multiple whole objects
5. Improves Flexibility: The relationship is loose which reduces coupling between classes. You can modify one class without affecting the other.
'''
# 2.3 Composition
'''Composition represents a “has-a” relationship with strong ownership. One class owns another class. Child object cannot exist independently. If parent is destroyed, child is destroyed too. Parent controls the lifecycle of child. Composition is a special type of association that signifies strong ownership between objects. The “whole” class is fully responsible for creating, managing, and destroying the “part” objects. In fact, the parts cannot exist without the whole'''
'''Key characteristics:
1. Represents a strong “has-a” relationship.
2. The whole owns the part and controls its lifecycle.
3. When the whole is destroyed, the parts are also destroyed.
4. The parts are not shared with any other object.
5. The part has no independent meaning or identity outside the whole.
'''
# 2.3.1 Example 1: Car & Engine, Engine should not exist without Car - Engine is created inside Car
class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine=Engine() # composition
    def drive(self):
        self.engine.start()
        print("Car is moving")
car=Car()
car.drive()
# 2.3.2 Example 2: House & Rooms, Rooms cannot exist without the House.
class Room:
    def __init__(self,name):
        self.name=name
class House:
    def __init__(self):
        self.rooms=[Room("Bedroom"),Room("Kitchen"),Room("Bathroom")]
house=House()
for room in house.rooms:
    print(room.name)
# 2.3.3 Example 3: Order & OrderItems, OrderItem has no meaning without Order.
class OrderItem:
    def __init__(self,product,price):
        self.product=product
        self.price=price
class Order:
    def __init__(self):
        self.items=[]
    def add_item(self,product,price):
        self.items.append(OrderItem(product,price)) # composition
    def total_price(self):
        return sum(item.price for item in self.items)
order=Order()
order.add_item("Laptop",1000)
order.add_item("Monitor",500)
print(order.total_price())
# 2.3.4 Design rule - Prefer composition over inheritance
'''
1. Inheritance creates tight coupling, child depends heavily on parent's implementation, small change in parent can break many children. With composition changes are localized, not global.
2. Inheritance forces unwanted behaviour, child classes inherit everything, even things they shouldn't.
### USE INHERITANCE ONLY IF : Child is-a parent, Behaviour is always valid, Relationship will never change
### USE COMPOSITION : Child uses behaviour, Behaviour can change, you want flexibility
'''
# 2.3.5 Why Composition matters in OOPS
'''
1. Correct Lifecycle Management - prevents invalid states like a room without a house
2. Strong Encapsulation - parent fully controls child and child implementation can change safely
3. Prevents accidental sharing bugs - child objects are not reused incorrectly and no hidden 
'''
# 2.3.6 When composition should be used
'''
1. Child cannot exist alone
2. Child is a part of parent
3. Child must NOT be shared
4. Parent controls creation & destruction
'''
# 2.4 Dependency 
'''A Dependency exists when one class relies on another to fulfill a responsibility.
This typically happens when:
1. A class accepts another class as a method parameter.
2. A class instantiates or uses another class inside a method.
3. A class returns an object of another class from a method.
'''
'''Key characteristics:
1. Short-lived: The relationship exists only during method execution.
2. No ownership: The dependent class does not store the other as a field.
3. "Uses-a" relationship: The class uses another to accomplish a task, but does not retain it.
4. Weakest relationship in OOP.
'''
# 2.4.1 Example 1 - Report depends on Printer, but does not store it.
class Printer:
    def print_doc(self,text):
        print(text)
class Report:
    def generate(self,printer): # dependancy
        printer.print_doc("Annual Report")
printer=Printer()
report=Report()
report.generate(printer)
# 2.4.2 Why Dependency matters in OOPS
'''
1. Reveals Coupling : Shows how tightly classes are connected, promotes loose coupling.
2. Improves Testability : Lets you replace real dependancies with fake ones (Testing an app with fake db instead of touching real db)
3. Reusability : same class works with different implementations
'''
# 2.4.3 Dependency Injection
'''Providing a class with its dependencies from the outside instead of creating them inside. Don’t create what you depend on, Receive it. Without DI - tight coupling, with DI - loose coupling, flexible design'''
# 2.4.3. a. Example 1 - Bad Design without Dependency Injection
class EmailService:
    def send(self,msg):
        print("Sending email:",msg)
class Notification:
    def __init__(self):
        self.email=EmailService() # hard-coded dependency
    def notify(self):
        self.email.send("Hello")
# Cannot replace EmailService, Hard to test, violates Single Responsibility Principle
#Example 1 - Good Design with Dependency Injection
class Notification:
    def __init__(self, service):
        self.service = service  # injected dependency
    def notify(self):
        self.service.send("Hello")
email = EmailService()
notification = Notification(email)
notification.notify()
# 2.4.3.1 Dependency Injection Types - Constructor Injection (Most common), Method Injection, Property Injection
# Constructor Injection - As constructor parameters
class Service:
    def execute(self):
        print("Service executed")
class Client:
    def __init__(self, service):
        self.service = service
# Method Injection - As method parameters
class Client:
    def process(self, service):
        service.execute()
# Property Injection - As Class Fields/Instance variables
class Client:
    def __init__(self):
        self.service = None
    def set_service(self, service):
        self.service = service
# 2.4.4 When to use Dependency and DI
'''
Use dependency when:
1. Class needs external behavior
2. Relationship is short-lived
3. No ownership required
'''
'''
Use dependency injection when:
1. You want flexibility
2. You want easy testing
3. You expect changes in implementation
'''
# 2.5 Dependency 
'''Realization is a relationship between a class and an interface (or abstract class). The interface defines a contract (methods without implementation). The class realizes (implements) that contract. In Python, we usually do this using abstract base classes (ABC)'''
'''Real-World Example- Interface: Payment, Classes: CreditCardPayment, PayPalPayment.Both must implement pay(amount) method — that is realization.'''
# 2.5.1 Example
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass  # just a contract, no implementation
class CreditCardPayment(Payment):
    def pay(self, amount): # Realize the interface in concrete classes
        print(f"Paid {amount} using Credit Card")
class PayPalPayment(Payment):
    def pay(self, amount): # Realize the interface in concrete classes
        print(f"Paid {amount} using PayPal")
def process_payment(payment_method, amount): # use the concrete classes
    payment_method.pay(amount)  # depends on interface
credit = CreditCardPayment()
paypal = PayPalPayment()
process_payment(credit, 100)
process_payment(paypal, 200)
# process_payment depends only on Payment (the interface), not the concrete classes
# Both CreditCardPayment and PayPalPayment realize the Payment interface
# You can add another payment method (like UPIPayment) without changing process_payment
# 2.5.2 When to use inheritance and realization
'''Inheritance models identity
"A Dog IS an Animal."

The child inherits everything from the parent, including state (fields) and behavior (methods). You use it when there's a true taxonomic relationship.

Use Inheritance when:
There's a true "is-a" relationship (Dog is an Animal)
You want to share implementation code across related classes
Child classes are specializations of the parent
State (fields) needs to be inherited
Realization models capability
"A Bird CAN fly, and so can an Airplane."

The implementing classes share what they can do, not what they are. A Bird and an Airplane have nothing else in common.

Use Realization (Interfaces) when:
Unrelated classes share a capability (Flyable, Serializable, Comparable)
Multiple inheritance of behavior is needed
You want maximum flexibility and loose coupling
The contract matters more than shared implementation'''