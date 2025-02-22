#xmltodict -> converte xml em dicionario python
import xmltodict

#abrir arquivo em formato binário
with open('NFs Finais/DANFEBrota.xml', 'rb') as arquivo:
  #tranforma em dicionario
  documento = xmltodict.parse(arquivo)
# print(documento)


dic_notafiscal = documento['nfeProc']['NFe']['infNFe']

#valor-total, produtos/seviços (valores),  cnpj_vendeu, cpf/cnpj_comprou, nome_comprou

valor_total = dic_notafiscal['total']['ICMSTot']['vNF']

cnpj_vendeu = dic_notafiscal['emit']['CNPJ']

nome_vendeu = dic_notafiscal['emit']['xNome']

cpf_comprou = dic_notafiscal['dest']['CPF']

nome_comprou = dic_notafiscal['dest']['xNome']


produtos = dic_notafiscal['det']
lista_produtos = []

for produto in produtos:
  valor_produto = produto['prod']['vProd']
  nome_produto = produto['prod']['xProd']
  lista_produtos.append((nome_produto ,valor_produto))
  # print(valor_produto, nome_produto)
 





#resposta em dicionario
resposta = {
  'valor total': valor_total,
  'cnpj_vendeu': cnpj_vendeu,
  'nome_vendeu': nome_vendeu,
  'cpf_comprou': cpf_comprou,
  'nome_comprou': nome_comprou,
  'lista_produtos': lista_produtos
}

print(resposta)
