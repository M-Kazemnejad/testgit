spainDict = iranDict = portugal = morocco = {'wins': 0 , 'loses': 0 , 'draws': 0 , 'goale_zade' : 0 , 'gole_khorde': 0 }
iran_spain = input()
iran_portugal = input()
iran_morocco = input()
spain_portugal = input()
spain_morocco = input()
portugal_morroco = input()

iran_spain = iran_spain.split('-')
iran_gols1 = int(iran_spain[0])
spain_gols1 = int(iran_spain[1])
print(iran_gols1)
print(type(iran_gols1))
if iran_gols1 > spain_gols1:
    iranDict['wins'] += 1 
    iranDict['goale_zade'] = iran_gols1
    spainDict['loses'] += 1
    spainDict['gole_khorde'] = iran_gols1
elif iran_gols1 < spain_gols1:
    iranDict['loses'] += 1
    iranDict['gole_khorde'] += 1
    spainDict['wins'] +

