import os
from utils import extrair_numero_lote_do_nome_arquivo

def ler_htmls(pasta_html):
    lotes_html_lista = []

    for nome_arquivo in os.listdir(pasta_html):
        if nome_arquivo.endswith(".html") and nome_arquivo.lower().startswith("lote"):
            numero_lote = extrair_numero_lote_do_nome_arquivo(nome_arquivo)
            if numero_lote is not None:
                lotes_html_lista.append(numero_lote)
    
    return lotes_html_lista