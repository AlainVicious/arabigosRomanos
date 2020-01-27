from numeros.Convert import numerosConvert

convert = numerosConvert()

romanoInput = input('ingresa el numero romano: ').upper()
arabigoInput = int(input('ingresa el numero arabigo: '))

arabigo = convert.romano_a_arabigo(romanoInput)
romano = convert.arabigo_a_romano(arabigoInput)

print('Romano: {0} Arabigo: {1}'.format(romanoInput, arabigo))
print('Arabigo: {0} Romano: {1}'.format(arabigoInput, romano))numeroArabigo