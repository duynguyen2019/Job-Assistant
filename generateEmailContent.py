
def generateEmailContent(job_info: dict):
    text = """Hello \n
    Please see the attached file.\n
    Thank you so much for your attention.\n
    Respectfully,\n
    Duy Nguyen
    """
    html = f"""<html><head></head><body><p>Dear Mr. {job_info['lastname']},
                                    <p>Regarding {job_info['position']} at {job_info['company']},
                                       I am very interested in applying.
                                       Please see my resume and cover letter</p>
                                    <p>Thank you so much for your consideration.</p>
                                    <p>Respectfully<br>Duy Nguyen</p></body></html>
                                    """
    return text, html