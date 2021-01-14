TICKETS_NUMBER = [('A1', 'A1'),]
for pre in range(ord('A'), ord('Z')+1):
    for fix in range(100):
        val = chr(pre)+ "-" + str(fix)
        TICKETS_NUMBER.append((val, val))
TICKETS_NUMBER = tuple(TICKETS_NUMBER)


print(TICKETS_NUMBER)