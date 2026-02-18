dict={
    "name":"sowjanya",
    "ages":{
    "age1":21,
    "age2":23
}
}
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict["name"])
print(dict.update({"name":"raj"}))
print(dict)
print(dict.get("name"))
print(dict["ages"]["age2"])
print(dict["ages"].get("age2"))

#using loops-----

for key in dict:
    print(key)
for value in dict.values():
    print(value)    
for key,value in dict.items():
    print(key,":",value)   
