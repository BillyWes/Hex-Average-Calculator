def TakeInput():
    return(input('Please input your first value'))
    
hex1 = TakeInput()
hex2 = TakeInput()
hex3 = TakeInput()

avHex = ''

for i in range(3)
  o = 2*i
  avHex = avHex + str((int(hex1[o:o+1], 16)) + (int(hex2[o:o+1], 16)) + (int(hex3[o:o+1], 16))/3)

print(avHex)
