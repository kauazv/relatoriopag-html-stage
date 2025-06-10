import re
import os

def normalizar_lote(lote: str) -> str:
    lote = lote.lower()
    lote = re.sub(r'lote\s*', '', lote)
    lote = re.sub(r'@.*$', '', lote)
    lote = lote.replace(',', '.').replace('-', '.')
    partes = lote.strip().split('.')
    partes = [str(int(p)) for p in partes if p.strip().isdigit()]
    return '.'.join(partes)


def pedir_diretorios():
    pasta_html = input("Digite o caminho da pasta com os HTMLs: ").strip()
    pasta_pdf = input("Digite o caminho da pasta com o 'MERGED PDF.pdf': ").strip()
    caminho_pdf = os.path.join(pasta_pdf, "MERGED PDF.pdf")
    
    if not os.path.isfile(caminho_pdf):
        print(f"❌ Arquivo 'MERGED PDF.pdf' não encontrado em: {pasta_pdf}")
        exit(1)
    
    return pasta_html, caminho_pdf, pasta_pdf

def extrair_numero_lote_do_nome_arquivo(nome_arquivo):
    padrao = r'lote\s*([0-9]+(?:[.,-][0-9]+)*)@2025'
    match = re.search(padrao, nome_arquivo, re.IGNORECASE)
    return match.group(1) if match else None

def extrair_numero_lote_do_conteudo(texto):
    padrao = r'lote\s*:?\s*(\d+(?:[.,-]\d+)*)'  
    return [m for m in re.findall(padrao, texto, re.IGNORECASE)]
