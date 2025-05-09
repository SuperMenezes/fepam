import re
from pypdf import PdfReader

pdlinesreview = list()
pdftext = ""


#LÊ O ARQUIVO .PDF
reader = PdfReader("relatorio.pdf")

for page in reader.pages:
    text = page.extract_text()
    pdftext = pdftext + text

#SEPARA O TEXTO DO PDF PELAS QUEBRAS DE LINHA
pdflines = pdftext.split('\n')

#LIMPA AS LINHAS DO RODAPÉ E RETIRA LINHAS EM BRANCO
for line in pdflines:
    #LIMPA O TEXTO QUE APARECE CONCATENADO
    line = line.replace("RELATÓRIO DE PESQUISA POR MUNICÍPIO", "")

    #LIMPA ESPAÇOS
    line = line.strip()

    #REMOVE AS LINHAS DO RODAPE E AS LINHAS VAZIAS
    if not (line == "" or "Fundação Estadual de Proteção Ambiental Henrique Luis Roessler/RS" in line or "Av. Borges de Medeiros, 261 - Fone *(51) 3288-9444 - CEP 90020-021 - Porto Alegre - RS - Brasil" in line or "www.fepam.rs.gov.br" in line or "página" in line):
        pdlinesreview.append(line)

#COM AS LINHAS LIMPAS, COMEÇA A GRAVAR O ARQUIVO DE DESTINO
print("INICIA GRAVAÇÃO")
with open('resultado.txt', 'w') as file:
    
    file.write("EMPRESA\tCGC/CPF\tCATEGORIA\tPORTE\tENDEREÇO\tMUNICÍPIO")
    file.write("\n")
    
    registro = 0
    while registro < len(pdlinesreview):
        empresa = pdlinesreview[registro]
        documento = pdlinesreview[registro+1]
        categoria = pdlinesreview[registro+2]
        porte = pdlinesreview[registro+3]
        municipio = pdlinesreview[registro+4]
        endereco = pdlinesreview[registro+5]
        
        #print(registro, "- ", (registro%6))
        #print(pdlinesreview[registro])

        file.write(empresa)
        file.write("\t")
        file.write(documento)
        file.write("\t")
        file.write(categoria)
        file.write("\t")
        file.write(porte)
        file.write("\t")
        file.write(endereco)
        file.write("\t")
        file.write(municipio)
        file.write("\n")
        #print(empresa, documento, categoria, porte, endereco, municipio)

        registro += 6

print("TERMINA GRAVAÇÃO")
