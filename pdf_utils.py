from PyPDF2 import PdfReader
from utils import extrair_numero_lote_do_conteudo

def extrair_texto_pdf(caminho_pdf):
    reader = PdfReader(caminho_pdf)
    texto_paginas = []
    lotes_pdf_lista = []
    
    for page in reader.pages:
        texto = page.extract_text() or ""
        texto_paginas.append(texto)
        lotes_pdf_lista.extend(extrair_numero_lote_do_conteudo(texto))
    
    return texto_paginas, lotes_pdf_lista
