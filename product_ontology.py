from owlready2 import *

def create_product_ontology():

    ontology = get_ontology("http://example.org/company_ontology.owl")

    with ontology:

        class Organization(Thing): 
            pass
        class Department(Organization): 
            pass

        class Person(Thing): 
            pass
        class Manager(Person): 
            pass
        class Employee(Person): 
            pass
        class ProductManager(Employee):
            pass

        class Product(Thing): 
            pass
        class ProductID(Product): 
            pass

        class Service(Thing): 
            pass
        class ServiceID(Service):
            pass

        #Person, Employee 
        class hasName (DataProperty, FunctionalProperty):
            domain = [Person]
            range = [str]
        class hasEmail(DataProperty, FunctionalProperty):
            domain = [Person]
            range = [str]
        class hasAddress(DataProperty, FunctionalProperty):
            domain = [Person]
            range = [str]
        class hasPhone(DataProperty, FunctionalProperty):
            domain = [Person]
            range = [str]
        class isProductExperOf (ObjectProperty):
            domain = [Employee]
            range = [Product]
        class hasTitle (ObjectProperty):
            domain = [Employee]
            range = [ProductManager]

        #Departments
        class hasDeptID (DataProperty, FunctionalProperty):
            domain = [Department]
            range = [int]
        class hasManager(ObjectProperty): 
            domain =[Department]
            range =[Manager]
        class hasEmployee(ObjectProperty): 
            domain =[Department]
            range =[Employee]
        class offersProduct(ObjectProperty):
            domain = [Department]
            range = [ProductID]
        class offersService (ObjectProperty):
            domain =[Department]
            range = [ServiceID]
        
        #Product
        class hasProductID (ObjectProperty):
            domain = [Product]
            range = [ProductID]
        class hasHeight (DataProperty, FunctionalProperty):
            domain = [Product]
            range = [int]
        class hasWidth (DataProperty, FunctionalProperty):
            domain = [Product]
            range = [int]
        class hasDepth(DataProperty, FunctionalProperty):
            domain = [Product]
            range = [int]
        class hasWeight(DataProperty, FunctionalProperty):
            domain = [Product]
            range = [int]
        class hasRelatedProduct(ObjectProperty):
            domain = [Product]
            range = [Product]
            
        #Service 
        class hasServiceID(ObjectProperty):
            domain =[Service]
            range = [ServiceID]
        class hasServiceProduct(ObjectProperty):
            domain =[Service]
            range = [ProductID]

        #Service, Product
        class hasProductManager(ObjectProperty):
            domain =[Product]
            range = [Employee]
        class hasServiceProductManager(ObjectProperty):
            domain = [Service]
            range = [Employee]
        class hasPrice(DataProperty):
            domain = [Service, Product]
            range= [float]


    return ontology
                

