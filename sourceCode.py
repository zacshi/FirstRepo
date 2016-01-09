#print 96well plate labels
for Let in range(65, 73): # Step through charactor number 65 to 72 in ASCII
    for num in range(1, 13):
        print chr(Let) + str(num),# teh comma seems to be giving a space instead of new line
    print 
