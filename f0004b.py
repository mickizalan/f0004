név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
év = input('Melyik évben jáurnk? ')
év = int(év)
születési_év = év - kor + 18
print(név, ', kend ', születési_év, '-ban érettségizett.', sep='')
