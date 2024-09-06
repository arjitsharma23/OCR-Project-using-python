
from pdf2image import convert_from_path
import pytesseract as tsa
import util
from parser_prescription import PresprciptionParser
from parser_patient_details import PatientDetailsParser

pop= r"C:\poppler-24.07.0\Library\bin"
tsa.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract(file_path,file_format):
    pages= convert_from_path(file_path, poppler_path = pop)
    document_text =''

    if len(pages)>0:
        page = pages[0]
        processed_image = util.preprocess_image(page)
        text= tsa.image_to_string(processed_image, lang='eng')
        document_text ='\n'+ text

    if file_format == 'prescription':
        extracted_data = PresprciptionParser(document_text).parse
        
    elif file_format == 'patient_details':
        extracted_data= PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data

if __name__ =='__main__':
    data = extract(r"C:\Users\hp\OneDrive\Documents\backend\resources\patient_details\pd_2.pdf",'patient_details')
    print(data)
