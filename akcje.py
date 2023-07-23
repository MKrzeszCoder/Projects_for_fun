from requests import get


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey='
KEY='*************************'
data = get(url+KEY).json()
data=data.values()
opis=list(data)
maxik=max(len(s) for s in opis[0])
maxik1=max(len(s) for s in opis[0].values())
if maxik1>maxik:
    maxik=maxik1

for elementy in opis[0].keys():
    print(' '+elementy.center(maxik),end=" *** ")
print()
for elementy in opis[0].values():
    print(' '+elementy.center(maxik),end=" *** ")
print()



for elementy in opis[1].keys():
    print(' '+elementy.center(maxik),end=" *** ")
print()
for elementy in opis[1].values():
        for el1,el2 in elementy.items():
            print(' '+str(el1+el2).center(maxik//5),end='')
print()


