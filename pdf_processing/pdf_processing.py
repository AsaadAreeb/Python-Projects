# Instead of making a .py file, I ran these commands directly on terminal.

# Extracting Text from PDFs
# >>> import PyPDF2
# >>> pdfFileObj = open('paper.pdf', 'rb')
# >>> pdfReader = PyPDF2.PdfReader(pdfFileObj)
# >>> len(pdfReader.pages)
# 16
# >>> pageObj = pdfReader.pages[0]
# >>> pageObj.extract_text()
# >>> pdfFileObj.close()

#############  Decrypting PDFs  #############
# >>> import PyPDF2
# >>> pdfReader = PyPDF2.PdfReader(open('encrypted.pdf', 'rb'))
# >>> pdfReader.is_encrypted
# True
# >>> pdfReader.pages[0]
    # raise FileNotDecryptedError("File has not been decrypted")

# >>> import PyPDF2
# >>> pdfReader = PyPDF2.PdfReader(open('encrypted.pdf', 'rb'))
# >>> pdfReader.is_encrypted
# True
# >>> pdfReader.decrypt("rosebud")
# <PasswordType.OWNER_PASSWORD: 2>
# >>> pageObj = pdfReader.pages[0]