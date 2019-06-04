import datetime, json, codecs

def formatData(data):

    d = datetime.datetime.strptime(data, '%d/%m/%Y')
    d = datetime.date.strftime(d, '%Y-%m-%d')
    return d


f = codecs.open("consulta_cand_2014_BA.txt", "r", "Latin-1")
# f = open('consulta_cand_2014_BA.txt')


linha = 1
count = 0
lista_candidatos = []
while linha != '':
    linha = f.readline()
    linha = linha.replace('"', '')
    if linha != '':
        count = count + 1
        candidato = dict()
        candidato["model"]= 'deputados.deputados'
        candidato["pk"]= count
        fields = dict()
        cand = linha.split(';')
        fields['data_geracao']= formatData(cand[0])
        fields['hora_geracao']= cand[1],
        fields['ano_eleicao']= int(str(cand[2]))
        fields['num_turno']= int(cand[3])
        fields['descricao_eleicao']= cand[4]
        fields['sigla_uf']= cand[5]
        fields['sigla_ue']= cand[6]
        fields['descricao_ue']= cand[7]
        fields['codigo_cargo']= int(cand[8])
        fields['descricao_cargo']= cand[9]
        fields['nome_candidato']= cand[10]
        fields['sequencial_candidato']= int(cand[11])
        fields['numero_candidato']= int(cand[12])
        fields['cpf_candidato']= int(cand[13])
        fields['nome_urna_candidato']= cand[14]
        fields['cod_situacao_candidatura']= int(cand[15])
        fields['des_situacao_candidatura']= cand[16]
        fields['numero_partido']= int(cand[17])
        fields['sigla_partido']= cand[18]
        fields['nome_partido']= cand[19]
        fields['codigo_legenda']= int(cand[20])
        fields['sigla_legenda']= cand[21]
        fields['composicao_legenda']= cand[22]
        fields['nome_legenda']= cand[23]
        fields['codigo_ocupacao']= int(cand[24])
        fields['descricao_ocupacao']= cand[25]
        fields['data_nascimento']= formatData(cand[26])
        fields['num_titulo_eleitoral_fields']= int(cand[27])
        fields['idade_data_eleicao']= int(cand[28])
        fields['codigo_sexo']= int(cand[29])
        fields['descricao_sexo']= cand[30]
        fields['cod_grau_instrucao']= cand[31]
        fields['descricao_grau_instrucao']= cand[32]
        fields['codigo_estado_civil']= int(cand[33])
        fields['descricao_estado_civil']= cand[34]
        fields['codigo_cor_raca']= int(cand[35])
        fields['descricao_cor_raca']= cand[36]
        fields['codigo_nacionalidade']= int(cand[37])
        fields['descricao_nacionalidade']= cand[38]
        fields['sigla_uf_nascimento']= cand[39]
        fields['codigo_minicipio_nascimento']= int(cand[40])
        fields['nome_municipio_nascimento']= cand[41]
        fields['despesa_max_campanha']= cand[42]
        fields['cod_sit_tot_turno']= int(cand[43])
        fields['desc_sit_tot_turno']= cand[44]
        fields['nm_email']= cand[45]

        candidato['fields'] = fields
    lista_candidatos.append(candidato)
print lista_candidatos[4]
a = json.dumps(lista_candidatos)

f = open('out.txt', 'w')
f.write(a)
