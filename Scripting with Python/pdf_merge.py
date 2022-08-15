import sys
import PyPDF2

input_pdfs = sys.argv[1:]


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('merged.pdf')


pdf_merger(input_pdfs)
