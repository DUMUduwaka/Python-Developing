from re import template
import PyPDF2

template = PyPDF2.PdfFileReader(open('merged.pdf', 'rb'))
