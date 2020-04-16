def lerArquivoCsv():
    return open(
        'F:\\FACULDADES - LOGATTI\\ANALISE E PROJETOS AVANÇADOS DE '
        'SOFTWARE\\Engenharia\\Aula4\\school-report\\1617FedSchoolCodeList.csv',
        'r').readlines()


def abrirArquivoTxt(nome_arquivo):
    return open(
        'F:\\FACULDADES - LOGATTI\\ANALISE E PROJETOS AVANÇADOS DE '
        'SOFTWARE\\Engenharia\\Aula4\\school-report\\' + nome_arquivo + '.txt',
        'w')


## Criar uma extração apenas com as seguintes colunas: ID, SchoolCode e SchoolName.
arquivo = lerArquivoCsv()
resultado = []

for row in arquivo:
    colunas = row.split(';')
    resultado.append(colunas[0] + ';' + colunas[1] + ';' + colunas[2] + '\n')

arquivo = abrirArquivoTxt('condicao1')
arquivo.writelines(resultado)
arquivo.close()

## Criar um extração retornar todas as colunas e aplicar o filtro para City = "CLEVELAND"
arquivo = lerArquivoCsv()
resultado = []

try:
    for row in arquivo:
        colunas = row.split(';')
        if 'CLEVELAND' == colunas[4]:
            resultado.append(row)
            print(row)
except:
    print('Filtro não encontrado.')

arquivo = abrirArquivoTxt('condicao2')
arquivo.writelines(resultado)
arquivo.close()

## Criar um extração retornar todas as colunas e aplicar o filtro para SchoolName iniciando com a letra "A"
arquivo = lerArquivoCsv()
resultado = []

try:
    for row in arquivo:
        colunas = row.split(';')
        if 'A' in colunas[2][0]:
            resultado.append(row)
            print(row)
except:
    print('Filtro não encontrado.')

arquivo = abrirArquivoTxt('condicao3')
arquivo.writelines(resultado)
arquivo.close()

## Criar um extração retornar todas as colunas e aplicar o filtro para StateCode igual a "PR"
arquivo = lerArquivoCsv()
resultado = []

try:
    for row in arquivo:
        colunas = row.split(';')
        if 'PR' == colunas[5]:
            resultado.append(row)
        print(row)
except:
    print('Filtro não encontrado.')

arquivo = abrirArquivoTxt('condicao4')
arquivo.writelines(resultado)
arquivo.close()

## Criar um extração retornar SchoolName, City e StateCode, aplicar o filtro para ZipCode igual a "44106"

arquivo = lerArquivoCsv()
resultado = []

try:
    for row in arquivo:
        colunas = row.split(';')
        if '44106' == colunas[6]:
            resultado.append(colunas[2] + ';' + colunas[4] + ';' + colunas[5] + '\n')
except:
    print('Filtro não encontrado.')

arquivo = abrirArquivoTxt('condicao5')
arquivo.writelines(resultado)
arquivo.close()

## Gerar um consolidado demonstrando a quantidade de escolas, fazer um agrupamento pela "City" ( cidade x - n escolas, cocidade y - z eslas)
arquivo = lerArquivoCsv()
resultado = []
lista = []


def verificarExistencia(cidadeVerificada):
    for index in range(len(lista)):
        if lista[index]['cidade'] == cidadeVerificada:
            lista[index]['quantidade'] += 1
            return True
    return False


for i in range(len(arquivo)):
    cidade = arquivo[i].split(';')[4]
    if not verificarExistencia(cidade):
        lista.append({
            'cidade': cidade,
            'quantidade': 1
        })

lista.sort(key=lambda x: x['cidade'])

for item in lista:
    print(item)

arquivo = abrirArquivoTxt('condicao6')
arquivo.writelines(resultado)
arquivo.close()
