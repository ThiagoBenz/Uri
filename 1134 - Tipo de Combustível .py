resp = 5
gasolina = 0
alcool = 0
diesel = 0
while resp != 4:
    resp = int(input())

    if resp == 1:
        alcool += 1
    elif resp == 2:
        gasolina += 1
    elif resp == 3:
        diesel += 1
    elif resp == 4:
        print ("MUITO OBRIGADO")
        print ("Alcool:",alcool)
        print ("Gasolina:",gasolina)
        print ("Diesel:",diesel)
        break
        
   
    

