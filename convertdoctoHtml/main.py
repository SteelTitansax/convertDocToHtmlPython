from docx import Document
from bs4 import BeautifulSoup

def docx_to_html(docx_path, html_path):
    # Abre el archivo DOCX
    doc = Document(docx_path)
    html_content = ""

    # Itera sobre los párrafos y construye el HTML
    for para in doc.paragraphs:
        html_content += f"<p>{para.text}</p>\n"

    # Guarda el contenido HTML en un archivo
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

# Ruta del archivo DOCX de entrada y del archivo HTML de salida
docx_path = 'archivo.docx'
html_path = 'archivo.html'

docx_to_html(docx_path, html_path)
