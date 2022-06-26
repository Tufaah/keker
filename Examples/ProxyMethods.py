from keker import *
# In this example we will take a look at all Proxy classes/methods


proxy = ['107.173.37.111:3128', '107.174.139.113:3128', '45.199.131.183:3128']
        # Let's say that we have this proxies list


# > (Edit) Class Methods
# Same as edit class methods in Combo edit methods ( swap/shake )
# If you don't know about combo methods go check them first ( ComboMethods.py )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# > Other Methods
# Same as file methods in Combo ( from_file/from_api )
# But we have some other new things in Proxy class!

#Proxy(proxy).auto_update("api url", "minutes in int")
# It will auto update proxy list from an API url in ever number of minutes
# It do run on a separated thread so it doesn't effect any thing

print(Proxy(proxy).random)
# Return a random proxy

auth_proxy = ['107.173.37.111:3128:admin:123',
              '107.174.139.113:3128:dfgd:dgfgdg',
              '45.199.131.183:3128:4hdh:464646']

Proxy(auth_proxy).auth
print(auth_proxy)
# Update the proxy list to be python proxy auth
# Switching from ip:port:user:pass => user:pass:ip:port
# Switching from Normal pattern => Python requests pattern

# Proxy.proxies(proxy type, proxy)
# Explained and used in ( Checker.py ) in line [60]
# Used to send proxy to the requests lib
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #