"""
-OOPS: object oriented prgramming language is programming concept that make our code more cleaner,reusable ,organized format
(architecture)
organizes code around objects and classes.

-4 PILLARS OF OOPS:
1.Encapsulation
2.Abstraction
3.Inheritance
4.Polymorphism

-CLASS (blueprint for creating an object)- A class is a reusable blueprint or template used to create objects. 
It bundles data (variables) and behaviors (functions) together into a single package.

-OBJECT : object is an instance of a class. 
If a class acts as the blueprint, diagram, or template, the object is the actual physical, real-world entity built from that blueprint.

-ENCAPSULATION : (means bundling of data) Encapsulation is the practice of bundling data (attributes) and methods (functions)
together into a single unit (a class) while restricting direct access to some of the object's components.

-ABSTRACTION : (means hiding the complexity of code) Abstraction is the process of hiding complex implementation details and 
showing only the essential features to the user.

-POLIMORPHISM : Same concept diff behaviour

-INHERITANCE : Inherit properties from parent to child

"""

# class name:
#     def greet(self,a,b):
#         print(a+b)
#         print("hello")

    # def bye(self):         # 'self' acts as the catcher
    #     print("bye")    

# i=name()       #i is object
# i.greet(1,1)    #object(here its is-i) itself is passed as the first argument ,i.e. i,1,1
# i.bye()         

#SELF :  represents the specific object (or instance) you are currently creating or working with. 
# It acts as a pointer that tells Python, "Hey, assign this data or run this action for this specific object, not the whole class.

#polimorphism
class numbers :
    def four(self):
        print("4")
    def zero(self):
        print("0")
n=numbers()
n.four()
n.zero()

#inheritance
class fruit:
    def apple(self):
        print("apple")

class vegetable(fruit):
    def cabbage(self):
        print("cabbage")

v=vegetable()
v.apple()
v.cabbage()