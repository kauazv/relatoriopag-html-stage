import os
from collections import Counter
from utils import normalizar_lote

def analisar_lotes(lotes_pdf_lista, lotes_html_lista, pasta_base):
    # Conta ocorrências de cada lote
    contador_pdf = Counter(lotes_pdf_lista)
    # Aplica normalização nos lotes
    lotes_pdf_lista = [normalizar_lote(l) for l in lotes_pdf_lista]
    lotes_html_lista = [normalizar_lote(l) for l in lotes_html_lista]

    
    # Lotes únicos
    lotes_unicos_pdf = set(lotes_pdf_lista)
    lotes_unicos_html = set(lotes_html_lista)
    
    # Encontra discrepâncias
    lotes_extras_html = lotes_unicos_html - lotes_unicos_pdf
    lotes_faltando_html = lotes_unicos_pdf - lotes_unicos_html
    
    # Encontra duplicatas apenas no PDF
    duplicatas_pdf = {lote: count for lote, count in contador_pdf.items() if count > 1}
    
    # Salva relatório em arquivo texto
    caminho_relatorio = os.path.join(pasta_base, "relatorio_completo.txt")
    with open(caminho_relatorio, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("📊 RELATÓRIO COMPLETO DE COMPARAÇÃO PDF vs HTML\n")
        f.write("=" * 70 + "\n\n")
        
        # Informações gerais
        f.write("📈 INFORMAÇÕES GERAIS:\n")
        f.write("-" * 30 + "\n")
        f.write(f"📄 Total de lotes no PDF (incluindo duplicatas): {len(lotes_pdf_lista)}\n")
        f.write(f"📄 Total de lotes únicos no PDF: {len(lotes_unicos_pdf)}\n")
        f.write(f"🌐 Total de lotes únicos nos HTMLs: {len(lotes_unicos_html)}\n")
        f.write(f"🌐 Total de arquivos HTML processados: {len(lotes_html_lista)}\n\n")
        
        # Lista todos os lotes do PDF
        f.write("📋 LOTES ENCONTRADOS NO PDF:\n")
        f.write("-" * 30 + "\n")
        if lotes_pdf_lista:
            lotes_pdf_ordenados = sorted(lotes_pdf_lista)
            f.write(f"Lotes: {lotes_pdf_ordenados}\n\n")
        else:
            f.write("Nenhum lote encontrado no PDF.\n\n")
        
        # Adiciona separador
        f.write("-" * 30 + "\n")
        
        # Lista todos os lotes dos HTMLs
        f.write("📋 LOTES ENCONTRADOS NO HTML:\n")
        f.write("-" * 30 + "\n")
        if lotes_html_lista:
            lotes_html_ordenados = sorted(lotes_html_lista)
            f.write(f"Lotes: {lotes_html_ordenados}\n\n")
        else:
            f.write("Nenhum lote encontrado nos HTMLs.\n\n")
        
        # DUPLICATAS APENAS NO PDF
        f.write("🔍 ANÁLISE DE DUPLICATAS NO PDF:\n")
        f.write("-" * 40 + "\n")
        if duplicatas_pdf:
            f.write("❌ LOTES DUPLICADOS ENCONTRADOS NO PDF:\n")
            for lote, count in sorted(duplicatas_pdf.items()):
                f.write(f"   - Lote {lote}: aparece {count} vezes\n")
            f.write("\n")
        else:
            f.write("✅ Nenhuma duplicata encontrada no PDF.\n\n")
        
        # DISCREPÂNCIAS ENTRE PDF E HTML (apenas se houver)
        if lotes_extras_html or lotes_faltando_html:
            f.write("🔍 ANÁLISE DE DISCREPÂNCIAS:\n")
            f.write("-" * 40 + "\n")
            
            if lotes_extras_html:
                f.write("⚠️ LOTES EXTRAS NOS HTMLs (não estão no PDF):\n")
                for lote in sorted(lotes_extras_html):
                    f.write(f"   - Lote {lote}\n")
                f.write("\n")
            
            if lotes_faltando_html:
                f.write("❌ LOTES FALTANDO NOS HTMLs (estão no PDF):\n")
                for lote in sorted(lotes_faltando_html):
                    f.write(f"   - Lote {lote}\n")
                f.write("\n")
        
        f.write("=" * 70 + "\n")
    
    # Relatório simplificado no terminal
    print("\n" + "=" * 60)
    print("📊 RELATÓRIO SALVO COM SUCESSO")
    print("=" * 60)
    print(f"📁 Arquivo: {caminho_relatorio}")
    print(f"📄 Lotes no PDF: {len(lotes_pdf_lista)} (únicos: {len(lotes_unicos_pdf)})")
    print(f"🌐 Lotes nos HTMLs: {len(lotes_html_lista)} (únicos: {len(lotes_unicos_html)})")
    
    if duplicatas_pdf:
        print(f"❌ Duplicatas no PDF: {len(duplicatas_pdf)} lotes")
    
    if lotes_extras_html or lotes_faltando_html:
        print(f"⚠️ Discrepâncias encontradas")
    else:
        print(f"✅ Lotes sincronizados (exceto duplicatas)")
    
    print("\n💡 Abra o arquivo para ver o relatório completo!")
