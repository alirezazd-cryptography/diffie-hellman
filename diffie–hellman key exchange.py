print"Enter shared Prime: "
sharedPrime=long(raw_input())
print"Enter shared Base: "
sharedBase=long(raw_input())
print"Shared Prime: ",sharedPrime,"\nShared Base: ",sharedBase
print "Enter person #1 secret number:"
sec1=long(raw_input())
A=(sharedBase ** sec1) % sharedPrime
print "Person #1 to person #2 :",A
print "Enter person #2 secret number:"
sec2=long(raw_input())
B=(sharedBase ** sec2) % sharedPrime
print "Person #2 to Person #1 :",B
print "----------------------------------"
print "Person #1 privately calculated shared secret KEY:",B**sec1%sharedPrime
print "Person #2 privately calculated shared secret KEY:",A**sec2%sharedPrime
print "----------------------------------"
print "Press any key to exit"
raw_input()
exit()
