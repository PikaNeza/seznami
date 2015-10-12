nakupovalni_seznam = []
vpr = raw_input("Je treba kaj kupiti? ")
while vpr == "da":
    artikel1 = raw_input("Vnesi artikel: ")
    nakupovalni_seznam.append(artikel1)
    vpr = raw_input("Bi se kaj kupil? ")
else:
    print "To pa ne bo sile!"
print "Nabavi:"
for nakupi in nakupovalni_seznam:
    print nakupi