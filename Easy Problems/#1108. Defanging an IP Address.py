def defangIp(address):
    return address.replace(".", "[.]")

address = "255.100.50.0"
print(defangIp(address))