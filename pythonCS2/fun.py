def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo('aung',22)
printinfo(name='aung',age=22)
printinfo( age=22, name="aung" )
printinfo( name="aung")