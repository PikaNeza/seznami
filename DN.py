nakupovalni_seznam = []
vpr = raw_input("Je treba kaj kupiti? ")
while vpr == "da":
    artikel1 = raw_input("Vnesi artikel: ")
    if artikel1 == "ne":
        break
    nakupovalni_seznam.append(artikel1) # vpr = raw_input("Bi se kaj kupil? ")
print "Nabavi:"
for nakupi in nakupovalni_seznam:
    print nakupi