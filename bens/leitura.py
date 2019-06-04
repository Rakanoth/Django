import datetime, json, codecs

def formatData(data):

    d = datetime.datetime.strptime(data, '%d/%m/%Y')
    d = datetime.date.strftime(d, '%Y-%m-%d')
    return d


f = codecs.open("bem_candidato_2014_BA.txt", "r", "Latin-1")


linha = 1
count = 0
lista_bens = []
while linha != '':
    linha = f.readline()
    linha = linha.replace('"', '')
    if linha != '':
        count = count + 1
        bem = dict()
        bem["model"]= 'bens.bens'
        bem["pk"]= count
        fields = dict()
        be = linha.split(';')
        fields['data_geracao']= formatData(be[0])
        fields['hora_geracao']= be[1],
        fields['ano_eleicao']= int(str(be[2]))
        fields['descricao_eleicao']= be[3]
        fields['sigla_uf']= be[4]
        fields['sequencial_candidato']= int(be[5])
        fields['cd_tipo_bem_candidato']= int(be[6])
        fields['ds_tipo_bem_candidato']= be[7]
        fields['detalhe_bem']= be[8]
        fields['valor_bem']= float(be[9])
        fields['data_ultima_att']= formatData(be[10])
        fields['hora_ultima_att']= be[11]

        bem['fields'] = fields
    lista_bens.append(bem)
print lista_bens[4]
a = json.dumps(lista_bens)

f = open('out.txt', 'w')
f.write(a)
