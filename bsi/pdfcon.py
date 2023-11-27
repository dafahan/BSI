import pdfkit

pdf_path = 'file.pdf'
html_path = 'my_html_file.html'
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
pdfkit.from_file(pdf_path, html_path, configuration=config)
