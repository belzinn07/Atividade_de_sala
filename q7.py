d= float(input('Digite a distância da viagem em km: '))
if d <= 200:

    print('vc pagará {}'.format(d*0.50))
else:

    print('Como a distãncia é maior que 200km vc pagará {}'.format(d*0.45))  
      