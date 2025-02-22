import xml.dom.minidom  # Importa o módulo minidom para manipulação de XML
import os  # Importa o módulo os para verificar a existência de arquivos

def format_xml_file(input_file_path, output_file_path):
    """Lê um arquivo XML, formata e salva em um novo arquivo."""
    
    # Verifica se o arquivo de entrada existe
    if not os.path.exists(input_file_path):
        print(f"Arquivo não encontrado: {input_file_path}")
        return

    # Abre o arquivo XML de entrada para leitura
    with open(input_file_path, 'r', encoding='utf-8') as file:
        xml_string = file.read()  # Lê o conteúdo do arquivo XML
    
    # Analisa a string XML e cria um objeto DOM
    dom = xml.dom.minidom.parseString(xml_string)
    
    # Formata o XML com indentação para torná-lo mais legível
    formatted_xml = dom.toprettyxml(indent="  ")

    # Abre (ou cria) o arquivo de saída para escrita
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_xml)  # Escreve o XML formatado no arquivo de saída

    # Imprime uma mensagem indicando que o arquivo foi formatado e salvo
    print(f'O arquivo XML foi formatado e salvo em: {output_file_path}')

# Exemplo de uso
input_file_path = r'C:\Users\sival\OneDrive\Documentos\Python_XMl\NFs finais\DANFENespresso.xml'  # Caminho do arquivo XML de entrada
output_file_path = r'C:\Users\sival\OneDrive\Documentos\Python_XMl\NFs finais\DANFENespresso_formatado.xml'  # Caminho do arquivo XML de saída

# Chama a função para formatar o arquivo XML
format_xml_file(input_file_path, output_file_path)
