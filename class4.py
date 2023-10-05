"""
#dictionary data type
emp={
    "name":"qwerty",
    "age":45,
    "eid":124,
    "skills":["ML","PYTHON","HTML"]
    }

print(emp)
print(type(emp))
print(emp["name"])
print(emp["eid"])
print(emp["skills"][1])
print(emp["skills"][::2])
"""
"""
emp={
    "name":"qwerty",
    "age":45,
    "eid":124,
    "skills":["ML","PYTHON","HTML"]
    }

#get method
print(emp.get("age"))

print(emp.get("skills")[1:2:])
print(emp.get("skills")[1])
print(emp.get("name"))
print(emp.get("state"))
print(emp.get("address"),"not found")
"""
"""
emp={
    "name":"qwerty",
    "age":45,
    "eid":124,
    "skills":["ML","PYTHON","HTML"]
    }
#accessing the values
print("start")
print(emp["name"])

print(emp)
print("done")
print(emp["state"])
"""
"""
emp={
    "name":"qwerty",
    "age":45,
    "eid":124,
    "skills":["ML","PYTHON","HTML"]
    }
#changing the values
print("before:")
print(emp)
emp["name"]="abcd"
emp["phone"]=1456
emp["address"]="Agra"
emp["eid"]=1022
emp["age"]=25
print("after:")
print(emp)
"""
"""
emp={
    "name":"qwerty",
    "age":45,
    "eid":124,
    "skills":["ML","PYTHON","HTML"]
    }
print("-----Before--------")
print(emp)
emp.update({
    "name": "zuno",
    "state": "new_delhi",
    "country":"India",
    "address": "Agra",
    "age":30
    })
print("-------After--------")
print(emp)
"""
"""
emp={
    "name":["qwerty"],
    "age":[45],
    "eid":124,
    "skills":["ML","PYTHON","HTML"],
    "address":[]
    }
#append function
print("-----Before--------")
print(emp)
emp["skills"].append("ds")
emp["name"].append("Guru")
emp.get("address").append("Mumbai")
emp["age"].append(30)
print("-------After--------")
print(emp)
"""
"""
emp={
    "name":["qwerty"],
    "age":[45],
    "eid":124,
    "skills":["ML","PYTHON","HTML"],
    "address":[]
    }
print("-----Before--------")
print(emp)
emp["skills"].extend(["ds","Java","Css","Js"])
emp["name"].extend(["Guru","Nanak","Aditi","Amiy"])
emp.get("address").extend(["Mumbai","Sagar","New_Delhi","Agra"])
emp["age"].extend([30,35,20,45])
print("-------After--------")
print(emp)
"""
"""
emp={
    "name":"qwerty",
    "age":45,
    "eid":124,
    "skills":["ML","PYTHON","HTML"],
    "address": "mumbai"
    }
print(emp)
emp.popitem()
print(emp)
emp.clear()
print(emp)
print("done")
"""
"""
print(emp)
print("done")
#emp.pop("name")
#emp.pop("skills")[1]
#del emp["skills"][1]
#del emp["skills"][::2]
del emp["skills"]
print(emp)
del emp
print(emp)
#emp.get("skills".append("java"))
"""
# keys,Values & items
emp={
    "name":"qwerty",
    "age":45,
    "eid":124,
    "skills":["ML","PYTHON","HTML"],
    "address": "mumbai"
    }
print(emp)
print(emp.keys())
print(emp.values())
print(emp.items())
print(emp)
print("Finally Done")

"""
#nested dictionary
company={
    "emp1":{
        "name":"abc",
        "age": 24,
        "eid":112
        },
    
    "emp2":{
         "name":"xyz",
        "age":25,
        "eid":126
         }
    }
print(company)
print(type(company))
print(company["emp1"]["name"])
print(company.get("emp2"))
"""
"""
a1={
    "name":"aaa",
    "eid":111
    }
a2={
    "name":"bbb",
    "eid":222
    }
print(a1)
print(a2)
a={
    1:a1,
    2:a2
    }
print(a.get(2)["eid"])
"""
"""
#constructor
a=dict(name="abc",age=24)
print(a)
print(type(a))
"""
