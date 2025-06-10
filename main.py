from pdf_utils import extrair_texto_pdf
from html_utils import ler_htmls
from relatorio import analisar_lotes
from utils import pedir_diretorios

if __name__ == "__main__":
    pasta_html, caminho_pdf, pasta_base = pedir_diretorios()

    print("📄 Lendo PDF e extraindo lotes...")
    texto_pdf, lotes_pdf_lista = extrair_texto_pdf(caminho_pdf)

    print("🌐 Lendo HTMLs e extraindo lotes...")
    lotes_html_lista = ler_htmls(pasta_html)

    print("🔍 Analisando lotes e gerando relatório...")
    analisar_lotes(lotes_pdf_lista, lotes_html_lista, pasta_base)
