import json
import requests
import hashlib

# pegar o arquivo json
resposta = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=[TOKEN]')

# carregar o json em uma variavel
arquivo = resposta.json()

# imprimir todo o json
#print(arquivo)

# tipo da variavel
#print(type(arquivo))

# verificar tokens do json
#print(arquivo.items())

#m nywx mrzirx, xlir aemx yrxmp qer gsqiw evsyrh xs riihmrk alex m lezi mrzirxih. v. fygoqmrwxiv jyppiv
texto_cifrado = arquivo['cifrado']

texto = ''

# voltando 4 casas as letras da frase 
for i in texto_cifrado:
    if ord(i)>=97 and ord(i)<=122:
        texto += chr(ord(i)-4)
    else:
        texto += i

# teste do texto decifrado 
# i just invent, then ]ait until man comes around to needing ]hat i have invented. r. buckminster fuller
#print(texto)

resumo = hashlib.sha1()
resumo.update(texto.encode('utf-8'))

arquivo['decifrado'] = texto
arquivo['resumo_criptografico'] = resumo.hexdigest()

#json modificado
#print(arquivo)

arquivo['file'] = 'answer'

dados = json.dumps(arquivo)

print('json~> ', dados)
print('tipo do arquivo~> ', type(dados), '\n')

'''with open('answer.json', 'w') as saida:
    json.dump(dados, saida)
'''
cabecalho = {'Content-type': 'application/json'}

post = requests.post(url='https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?[TOKEN]', json=dados)
print('resultado da requisição POST~> ', post.status_code)
print('requisição POST~> ', post.json())
