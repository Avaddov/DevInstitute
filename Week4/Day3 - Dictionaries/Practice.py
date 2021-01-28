#establish dict
a = {"a":1}
#access/add/overwrite data
a["b"]=2
# a["b"]=3
print(a)

#get method prevents crashes on keys that don't exist and give "none" in place
print(a.get("c"))
# print(a["c"]) ((This would crash code))

#remove/delete {key:value}
del a["b"]
print(a)

#nested dictionaries
a["c"] = {"d":4}
print(a["c"]["d"])

#list nested in a dictionary
a["d"] = ["m","v","s","y"]
#access v by indexing and chaining
print(a["d"][1])
