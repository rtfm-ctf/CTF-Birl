#!/usr/bin/python

with open("ASCII-ART.htm","r") as file:
    for line in file:
        target = open('resultado', 'a')
        target.write(line.replace("\n","").strip())
        with open('resultado','r') as file2:
            for line in file:
                print line.decode("base64").replace('`','').replace('@','').replace('/','')

#Passar resultado do script no site https://sange.fi/esoteric/brainfuck/impl/interp/i.html e pegar o resultado ;)
