from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.rl_config import defaultPageSize

import config


PAGE_WIDTH = defaultPageSize[0]
PAGE_HEIGHT = defaultPageSize[1]

def create_cert(name):
    """
    Функция для добавления текста на PDF файл.

    1. Создаем canvas и рисуем наш текст
    """
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))
    can.setFont("DejaVuSerif", 30)

    text = name
    text_width = pdfmetrics.stringWidth(text, "DejaVuSerif", 30)
    y = 310
    x = ((PAGE_WIDTH - text_width) / 2) + 120

    can.drawString(x, y, text)
    can.save()
    packet.seek(0)

    new_pdf = PdfFileReader(packet)  # получаем свою PDF с помощью canvas из Reportlab
    existing_pdf = PdfFileReader(open(config.TEMPLATE_PDF, "rb"))  # берем шаблон PDF

    """
    2. Создаем новый PDF-файл с помощью PyPDF2
    """
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)  # страница шаблона
    page.mergePage(new_pdf.getPage(0))  # мержим с нашей страницей
    output.addPage(page)

    """
    3. Save and enjoy!
    """
    outputStream = open(config.OUTPUT_PDF, "wb")
    output.write(outputStream)
    outputStream.close()
    return True


if __name__ == '__main__':
    create_cert("Иванову Петрову Сидоровичу")
