import docx2txt as doc
import os
import pdfkit
import re

def generateCoverLetter(job_info:dict):
    document = doc.process(os.environ.get('PATH_TO_TEMPLATE_FILE'))
    position_template = re.search('~(.*)~', document).group(1)
    company_template = re.search('!(.*)!', document).group(1)

    document = document.replace(f"~{position_template}~",job_info["position"])\
                                .replace(f"!{company_template}!",job_info["company"])\
                                    .replace("\n","<br>")\
                                        .replace("Hiring Manager",f"Mr. {job_info['lastname']}")

    #config = pdfkit.configuration(wkhtmltopdf=r"wkhtmltopdf\bin\wkhtmltopdf.exe")
    options = {
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': 'UTF-8',
        'dpi': 400

    }
    print("Writing Cover Letter to pdf file")
    pdfkit.from_string(document, f"attachments/Duy Nguyen_{job_info['company']}_CoverLetter.pdf",options=options)
    print("Cover Letter written!")

if __name__ == '__main__':
    job_info = [{"position":"Data Engineer","company":"Google"}]
    generateCoverLetter(job_info)


