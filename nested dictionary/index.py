#nested dictionary

nt={
    "one":{"name":{"FirstName":"abc","middlename":"xyz"},"address":{"state":"Kashmir","city":"srinagar"}},
    "two":{"name":{"FirstName":"def","middlename":"ghi"},"address":{"state":"kashmir","city":"pulwama"}},
    "three":{"name":{"FirstName":"hello","middlename":"world"},"address":{"state":"Kashmir","city":"kupwara"}},
}

# print(nt["one"])
# print(nt["two"]["address"]["city"])

nt["two"]["address"]["state"]="Jammu"

del nt["three"]["name"]["middlename"]

nt["four"]={"name":{"FirstName":"new","middlename":"name"},"address":{"state":"ladakh","city":"newcity"}}
print(nt)