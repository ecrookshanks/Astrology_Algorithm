# This is going to be the first simple test
# for the astrology algorithm.

signs = ('aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces')

baseName = input('Enter the subjects calculated sign: ')
try:
  orig = signs.index(baseName.lower())
except:
  print("The entered value is not found")
  exit()  

spouseIndex = (orig + 6) % 12
spouseWorkIndex = (orig + 6 + 5) % 12
spouseCareerIndex = (orig + 6 + 5 + 4) % 12
kidIndex = (orig + 4) % 12
kidWorkIndex = (orig + 4 + 5) % 12

print('Original subject is: ' + baseName)
print('Which has the following relations:')
print('SPOUSE:           ' + signs[spouseIndex])
print('SPOUSE WORK:      ' + signs[spouseWorkIndex])
print('SPOUSE CAREER:    ' + signs[spouseCareerIndex])
print('KID:              ' + signs[kidIndex])
print('KID WORK:         ' + signs[kidWorkIndex])