inp = input('Write a number from 1-9:')

if int(inp) < 4:
    print('Low heat')
elif int(inp) < 7:
    print('Medium heat')
elif int(inp) < 9:
    print('High heat')
else :
    print('What kind of stove do you have')

print('All done!')