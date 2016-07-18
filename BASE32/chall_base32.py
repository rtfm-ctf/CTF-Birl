import requests,base64,binascii

url = "http://termbin.com/t8ii"
r = requests.get(url, stream=True)
for line in r.iter_lines():
    if 'ase32' != line:
        try:
            base64.b32decode(line)
        except:
            arquivo = open('resultado_bin','a')
            arquivo.write(line.replace("=","")[len(line.replace("=",""))-1:].\
            replace("8","0").replace("9","1").replace('2','0').replace('?','b'))
            arquivo.close()
with open('resultado_bin','r') as result:
    for linha in result:
        n = int(linha, 2)
        print(binascii.unhexlify('%x' % n))
