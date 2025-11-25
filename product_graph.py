
import pandas as pd 
from owlready2 import *
import xml.etree.ElementTree as ET
from product_ontology import create_product_ontology

onto = create_product_ontology()
df = pd.read_excel('products.xlsx')
df2 = pd.read_csv('services.csv')
orgmap_path  = "/Users/abhivyakti/Desktop/Learning Code/Eccenca Project /data/orgmap.xml"

def clean_price(val):
    val =  val.strip("EUR").replace(',','.')
    return val 

#ORGMAP.XML
def orgmap():

    tree = ET.parse(orgmap_path)
    root = tree.getroot()

    for dept in root.findall("dept"):
        
        dept_name = dept.get("name")
        dept_id = dept.get("id")
        dept_instance = onto.Department(dept_name)
        dept_instance.hasDeptID = dept_id

        manager = dept.find("manager")
        if manager is not None:
            m_name = manager.findtext("name")
            m_email = manager.findtext("email")
            m_add = manager.findtext("address")
            m_phone = manager.findtext("phone")
                    
            manager_instance = onto.Manager(m_name)
            manager_instance.hasEmail = m_email
            manager_instance.hasAddress = m_add
            manager_instance.hasPhone =m_phone
            dept_instance.hasManager.append(manager_instance)
            #dept_instance.offersProduct.append()

        # employees
        for emp in dept.findall("employees/employee"):
            e_name = emp.findtext("name")
            e_email = emp.findtext("email")
            e_add = emp.findtext("address")
            e_phone = emp.findtext("phone")
            #TODO: products = emp.findtext("productExpert")

            employee_instance = onto.Employee(e_name)
            employee_instance.hasName = e_name 
            employee_instance.hasEmail = e_email
            employee_instance.hasAddress = e_add
            employee_instance.hasPhone = e_phone
            dept_instance.hasEmployee.append(employee_instance)
            #print(f"  Employee: {e_name}, {e_email}, ProductExpert in: {products}")

            
        """products
        for prod in dept.findall("products/product"):
            #print(f"  Product ID: {prod.get('id')}")
            dep_prod.append(prod.get('id'))
        """
        

        """# services
        for srv in dept.findall("services/service"):
            #print(f"  Service ID: {srv.get('id')}")
            dep_serv.append(srv.get('id'))
        print(dep_prod)
        #print(dep_serv)
        print("-" * 50)
 """
    onto.save(file = "graph2.owl", format="rdfxml")
        

#PRODUCTS.XLSX
def products():

    for index, row in df.iterrows():
        
        product_name = row['ProductName']
        product_id = row['ProductID']
        product_manager_email = row['ProductManager']
        height = int(row['Height'])
        width = int(row['Width'])
        depth = int(row['Depth'])
        weight = int(row['Weigth'])
        price = row['Price']
        price =  clean_price(price)
        price = float(price)
        #print (f"for product = {product_name}, price = {price}, hwdw =  {height}, {width}, {depth}, {weight}")
        
        
        #print(f"Product ID: {product_id}, Name: {product_name}, Expert: {product_manager_email}")

        product_instance = onto.Product(product_name)     
        product_id_instance = onto.ProductID(product_id)   
        product_instance.hasProductID.append(product_id_instance)
        product_id_instance.hasPrice.append(price)
        product_id_instance.hasHeight = height
        product_id_instance.hasWidth = width
        product_id_instance.hasDepth = depth
        product_id_instance.hasWeight = weight

        product_manager = onto.search(hasEmail = product_manager_email) #.search will give a list 

        if product_manager:
            product_manager = product_manager[0]
            #print (f"product = {product_name} , product manager ontology reference : {product_manager}")
            product_instance.hasProductManager.append(product_manager)
            

    onto.save(file = "graph2.owl", format="rdfxml")


#SERVICES.CSV 
def services():

    for index, row in df2.iterrows():

        ser_id = row['ServiceID']
        ser_name = row['ServiceName']
        ser_prod_man_email = row['ProductManager']
        ser_price =  row['Price']
        ser_price = clean_price(ser_price)
        ser_product = row['Products']
        products_list = [p.strip() for p in ser_product.split(',')]

        ser_ins = onto.Service(ser_name)
        ser_id_ins = onto.ServiceID(ser_id)
        ser_ins.hasServiceID.append(ser_id_ins) 
        ser_ins.hasPrice.append(ser_price)
        
        

        for product_id in products_list:
            #searching for a specific individual using search_one 
            product_id_search = onto.search_one(iri = f"*{product_id}")
            if product_id_search:
                ser_ins.hasServiceProduct.append(product_id_search)

        manager = onto.search(hasEmail = ser_prod_man_email)
        if manager:
            manager = manager[0]
            ser_ins.hasServiceProductManager.append(manager)

            

        onto.save(file = "graph2.owl", format="rdfxml")
        products_list = []
        #print ("___________________________")

def random ():

    tree = ET.parse(orgmap_path)
    root = tree.getroot()

    for dept in root.findall("dept"):

        dept_name = dept.get("name")
        dep_ins_search = onto.search_one(iri = f"*{dept_name}")

        for prod in dept.findall("products/product"):

            prod_id_search = prod.get('id')
            #print(f"  Product ID: {prod.get('id')}")
            prod_search = onto.search_one(iri = f"*{prod_id_search}")
            #print (f"department : {dep_ins_search}, product : {prod_search}")
            dep_ins_search.offersProduct.append(prod_search)

        for service in dept.findall("services/service"):

            serv_id_search = service.get('id')
            #print(f"  Service ID: {serv_id_search}")
            serv_search = onto.search_one(iri = f"*{serv_id_search}")
            dep_ins_search.offersService.append(serv_search)


    onto.save(file = "graph2.owl", format="rdfxml")
                


        
        
        



orgmap()
products()
services()
random()