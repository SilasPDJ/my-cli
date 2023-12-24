from PyPDF2 import PdfMerger
import os
# pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf'][:2]
# pdfs = ['pt0.pdf', 'pt1.pdf', 'pt2.pdf', 'pt3.pdf']


def generate_pdf_merge(path: os.PathLike, destiny: os.PathLike = None, files_are_reversed=False):
    """Merge PDF files in a specified directory.

    This function merges PDF files located in the given directory into a single PDF file.

    Args:
        path (os.PathLike): The path to the directory containing the PDF files.
        destiny (os.PathLike, optional): The destination directory for the merged PDF file.
            If not provided, the merged PDF will be saved in the same directory as the source PDFs.
        files_are_reversed (bool, optional): If True, the PDF files will be merged in reverse order.
            Defaults to False.

    Example:
        generate_pdf_merge('/path/to/pdf/files', destiny='/path/to/output', files_are_reversed=True)
    """
    print("testew")
    files = [os.path.join(path, file)
             for file in os.listdir(path) if file.endswith('pdf')]

    files.sort(reverse=files_are_reversed)

    merger = PdfMerger()
    # pdfs = [for pdf in pdfs]
    pdfs = files

    for pdf in pdfs:
        merger.append(pdf)
    if destiny is None:
        merger.write(os.path.join(path, "TUTTI.pdf"))
    else:
        merger.write(os.path.join(destiny, "TUTTI.pdf"))

    merger.close()
