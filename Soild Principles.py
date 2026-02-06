# SOLID Principles - makes code more maintainable and scalable
'''These enhance loose coupling which is group of classes which are less dependant on each other. Loose coupled classes minimize the changes in the code during updates thus making code more reusable, maintainable, flexible and stable'''
# 1. Single Resonsibility Principle
'''A class should have only one reason to change. Each class should have only one job/purpose and not be filled with excessive functionality which results in High cohesion'''
class Teacher: # class for teachers
    def teach(self):
        print("Teaching classes")
class Principal: # class for principal
    def manage(self):
        print("Managing school")
class Administration: # class for administration
    def manageadmissions(self): # class for
        print("Manages admissions and passed outs")
class Placements: # class for placements
    def manageplacements(self):
        print("Manage conducting placement sessions, exams and interviews")
def main():
    tea=Teacher()
    pri=Principal()
    adm=Administration()
    pla=Placements()
    tea.teach() # each class focuses on its one specific responsinility
    pri.manage()
    adm.manageadmissions()
    pla.manageplacements()
if __name__=="__main__":
    main()
# 2. Open/Closed Principle
'''Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification" which means you should be able to extend a class behavior, without modifying it. Can be achieved using abstract class'''
# Example where we had a class called PaymentProcessor that processes payments for a store using credit cards, we want to extend the functionality by supporting paypal payments as well.
from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def processpayment(self,amount):
        pass
class CreditCardPaymentProcessor(PaymentProcessor):
    def processpayment(self, amount):
        print("processing credit card payment of $",amount)
# Extended Functionality
class PayPalPaymentProcessor(PaymentProcessor):
    def processpayment(self, amount):
        print(f"processing paypal payment of ${amount}")
creditcard=CreditCardPaymentProcessor()
paypal=PayPalPaymentProcessor()
creditcard.processpayment(100)
paypal.processpayment(500)
# 3. Liskov's Substitution Principle
'''Derived or child classes must be substitutable for their base or parent classes. This principle ensures that any class that is the child of a parent class should be usable in place of its parent without any unexpected behaviour.'''
# 3.1 Example violating LSP
from abc import ABC,abstractmethod
# Base class for shape
class Rectangle(ABC):
    def __init__(self,width,height):
        self._width=width
        self._height=height
    @abstractmethod
    def area(self):
        return self._width*self._height
    def get_width(self):
        return self._width
    def get_height(self):
        return self._height
    @abstractmethod
    def set_width(self):
        self._width=width
    @abstractmethod
    def set_height(self):
        self._height=height
# Child/Derived class for Square
class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
    def set_width(self,width):
        self._width=self._height=width
    def set_height(self,height):
        self._height=self._width=height
    def area(self):
        return self._width*self._height
s=Square(5)
s.set_width(10)
print(f"Area is {s.area()}")
'''To see a potential violation of LSP, consider what would happen if you were to use the Square class in a context expecting a Rectangle:
If you substitute a Square where a Rectangle is expected, changing just the width or height would lead to unexpected results because it will change both dimensions.'''
# 3.2 Example not violating LSP
from abc import ABC, abstractmethod
# Base class shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Square(Shape):
    def __init__(self, size):
        self.size = size
    def area(self):
        return self.size * self.size
r = Rectangle(10, 20)
s = Square(10)
print(r.area())
print(s.area())
# 4. Interface Segregation Principle
'''This principle is the first principle that applies to Interfaces instead of classes in SOLID and it is similar to the single responsibility principle. It states that "do not force any client to implement an interface which is irrelevant to them". Here your main goal is to focus on avoiding fat interface and give preference to many small client-specific interfaces. You should prefer many client interfaces rather than one general interface and each interface should have a specific responsibility.'''
# 4.1 Bad Design - Violates ISP
# one big interface forces everyone to do everything
from abc import ABC, abstractmethod
class UserActions(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
    @abstractmethod
    def add_user(self):
        pass
    @abstractmethod
    def delete_user(self):
        pass
class NormalUser(UserActions):
    def login(self):
        print("User logged in")
    def logout(self):
        print("User logged out")
    def add_user(self):
        pass  # ❌ Not needed
    def delete_user(self):
        pass  # ❌ Not needed
# 4.2 Correct Design ISP-Compliant
# Classes should only depend on the methods they actually use.
from abc import ABC, abstractmethod
class UserService(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class AdminService(ABC):
    @abstractmethod
    def add_user(self):
        pass
    @abstractmethod
    def delete_user(self):
        pass
class RegularUser(UserService):
    def login(self):
        print("User logged in")
    def logout(self):
        print("User logged out")
class AdminUser(UserService, AdminService):
    def login(self):
        print("Admin logged in")
    def logout(self):
        print("Admin logged out")
    def add_user(self):
        print("User added")
    def delete_user(self):
        print("User deleted")
user = RegularUser()
user.login()
user.logout()
admin = AdminUser()
admin.login()
admin.add_user()
# 5. Dependancy Inversion Principle
'''The Dependency Inversion Principle (DIP) is a principle in object-oriented design that states that "High-level modules should not depend on low-level modules. Both should depend on abstractions". Additionally, abstractions should not depend on details. Details should depend on abstractions.
In simpler terms, the DIP suggests that classes should rely on abstractions (e.g., interfaces or abstract classes) rather than concrete implementations.
This allows for more flexible and decoupled code, making it easier to change implementations without affecting other parts of the codebase.'''
'''High-level modules should not depend on low-level modules. Both should depend on abstractions (interfaces).
Abstractions should not depend on details. Details should depend on abstractions.
In simple words:
High-level code (business logic) shouldn’t care how the low-level stuff works.
Low-level stuff (like Email, SMS) should follow a contract (interface) so high-level code can just use it.
This makes the system flexible, maintainable, and testable.'''
# Why DIP
# Without DIP
'''High-level code depends on concrete classes.
If we want to change the sending mechanism (email → SMS → push notification), we need to modify high-level code.
Testing becomes hard (we can’t mock services easily).'''
# With DIP
'''High-level code depends only on abstraction.
Low-level modules implement the abstraction.
We can swap services without touching high-level logic.'''
from abc import ABC,abstractmethod
# MessageService is an abstraction/interface.
# It defines a contract: “Any service that sends messages must implement send(message).”
# It does not care how the message is sent (email, SMS, push, etc.).
class MessageService(ABC):
    @abstractmethod
    def send(self, message):
        pass
# EmailService is a low-level module.
# It implements the abstraction MessageService.
# Knows exactly how to send an email.
class EmailService(MessageService):
    def send(self, message):
        print("Sending Email:", message)
# SMSService is another low-level module.
# Also implements MessageService.
# Knows how to send an SMS.
class SMSService(MessageService):
    def send(self, message):
        print("Sending SMS:", message)
# Notification is high-level code (business logic).
# It does not know whether it’s Email or SMS.
# It depends only on the abstraction MessageService.
# The actual service is injected into Notification via constructor.
class Notification:
    def __init__(self, service: MessageService):
        self.service = service  # dependency injected
    # Notification just calls send() on the service.
    # It does not care how sending is done.
    # If tomorrow we add WhatsAppService, no changes are needed in Notification.
    def notify(self, message):
        self.service.send(message)
email_service = EmailService()
notify_email = Notification(email_service)
notify_email.notify("Hello via Email!")
sms_service = SMSService()
notify_sms = Notification(sms_service)
notify_sms.notify("Hello via SMS!")
from abc import ABC, abstractmethod
# OTHER WAY OF WRITING ABOVE EXAMPLE WITH CLEAR STEPS AS COMMENTS
# ------------------------------
# Step 1: Abstraction (interface)
# ------------------------------
class MessageService(ABC):
    @abstractmethod
    def send(self, message):
        pass

# ------------------------------
# Step 2: Low-level implementations
# ------------------------------
class EmailService(MessageService):
    def send(self, message):
        print("Sending Email:", message)

class SMSService(MessageService):
    def send(self, message):
        print("Sending SMS:", message)

# ------------------------------
# Step 3: High-level module
# ------------------------------
class Notification:
    def __init__(self, service: MessageService):
        self.service = service  # dependency injected

    def notify(self, message):
        self.service.send(message)

# ------------------------------
# Step 4: Using the code
# ------------------------------
# Email notification
email_service = EmailService()
notify_email = Notification(email_service)
notify_email.notify("Hello via Email!")

# SMS notification
sms_service = SMSService()
notify_sms = Notification(sms_service)
notify_sms.notify("Hello via SMS!")



