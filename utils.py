import re
import os

def pedir_diretorios():
    pasta_html = input("Digite o caminho da pasta com os HTMLs: ").strip()
    pasta_pdf = input("Digite o caminho da pasta com o 'MERGED PDF.pdf': ").strip()
    caminho_pdf = os.path.join(pasta_pdf, "MERGED PDF.pdf")
    
    if not os.path.isfile(caminho_pdf):
        print(f"❌ Arquivo 'MERGED PDF.pdf' não encontrado em: {pasta_pdf}")
        exit(1)
    
    return pasta_html, caminho_pdf, pasta_pdf

def extrair_numero_lote_do_nome_arquivo(nome_arquivo):
    padrao = r'lote(\d{5})@2025'
    match = re.search(padrao, nome_arquivo, re.IGNORECASE)
    return int(match.group(1)) if match else None

def extrair_numero_lote_do_conteudo(texto):
    padrao = r'lote\s*:?\s*(\d+)'
    return [int(m) for m in re.findall(padrao, texto, re.IGNORECASE)]