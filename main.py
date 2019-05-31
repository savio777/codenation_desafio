import json
import requests
import hashlib

token = 'MEU TOKEN'

# pegar o arquivo json
resposta = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + token)

resposta.encoding = 'utf-8'

# carregar o json em uma variavel
arquivo = resposta.json()

# imprimir todo o json
print(arquivo)

# tipo da variavel
#print(type(arquivo))

# verificar tokens do json
#print(arquivo.items())

# guardar texto cifrado
#m nywx mrzirx, xlir aemx yrxmp qer gsqiw evsyrh xs riihmrk alex m lezi mrzirxih. v. fygoqmrwxiv jyppiv
texto_cifrado = arquivo['cifrado']

# inicializar variavel
texto = ''

# voltando as letras da frase 4 casas para descriptografar  
for i in texto_cifrado:
    if ord(i)>=98 and ord(i)<=122:
        texto += chr(ord(i)-4)
    # como o que vem depois de 97 (a) são caracteres especiais, e o desafio só aceita mudar letras pode concluir que a letra
    # criptografada é o w
    elif ord(i)==97:
        texto += 'w'
    else:
        texto += i

# criar texto criptografado
resumo = hashlib.sha1()
resumo.update(texto.encode('utf-8'))

# guardar texto decifrado e resumo criptografado
arquivo['decifrado'] = texto
arquivo['resumo_criptografico'] = resumo.hexdigest()

# criar arquivo
with open('answer.json', 'w') as f:
    json.dump(arquivo, f, ensure_ascii=False)

# variavel q lê o arquivo
arquivo_enviar = {'answer': open('answer.json', 'rb')}

# enviar a resposta
post = requests.post(url='https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + token, files=arquivo_enviar)

# log da requisição
print('resultado da requisição POST~> ', post.status_code)
print('requisição POST~> ', post.json(), '\n')
