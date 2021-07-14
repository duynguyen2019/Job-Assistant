
import os
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Setup the basics here
def send_mail(sender: str, recipient: str, subject: str, attachment_list: list, body_text: str, body_html: str):
    SENDER = sender
    RECIPIENT = recipient
    SUBJECT = subject
    # The full path to the file that will be attached to the email.
    att_list = attachment_list
    BODY_TEXT = body_text
    BODY_HTML = body_html

    # The character encoding for the email.
    CHARSET = "utf-8"

    # Create a new SES resource and specify a region.
    access_key  = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    client = boto3.client('ses',region_name ='us-east-2',
                        aws_access_key_id= access_key,
                        aws_secret_access_key= secret_access_key
                        )

    # Create an instance of multipart/mixed parent container.
    msg = MIMEMultipart('mixed')

    # Add subject, from and to lines.
    msg['Subject'] = SUBJECT 
    msg['From'] = SENDER 
    msg['To'] = RECIPIENT

    # Create a multipart/alternative child container.
    msg_body = MIMEMultipart('alternative')
    msg.attach(msg_body)

    # Encode the text and HTML content and set the character encoding. This step is
    # necessary if you're sending a message with characters outside the ASCII range.
    textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
    htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)

    # Add the text and HTML parts to the child container.
    msg_body.attach(textpart)
    msg_body.attach(htmlpart)

    # Define the attachment part and encode it using MIMEApplication.
    for attachment in att_list:
        att = MIMEApplication(open(attachment, 'rb').read())
        att.add_header('Content-Disposition','attachment', filename=os.path.basename(attachment))
        msg.attach(att)

    # Add the attachment to the parent container.

    #print(msg)
    try:
        #Provide the contents of the email.
        response = client.send_raw_email(
            Source=SENDER,
            Destinations=[
                RECIPIENT
            ],
            RawMessage={
                'Data':msg.as_string(),
            }
        )

    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
if __name__ =="__main__":
    # The email body for recipients with non-HTML email clients.
    text = """Hello \n
    
    Please see the attached file for a list of customers to contact.\n
    Thank you so much for your attention.\n
    Respectfully,\n
    Duy Nguyen
    
    """
    job_title ="Data Analyst"
    # The HTML body of the email.
    html = f"""\
    <html>
    <head></head>
    <body>
    <p>Dear Recruiter regarding {job_title},

    <p>Please see my resume and cover letter</p>

    <p>Thank you so much for your consideration.</p>

    <p>Respectfully<br>
    Duy Nguyen</p>

    </body>
    </html>
    """
    sender = "duynguyen1993@csu.fullerton.edu"
    recipient = "duynguyenms2021@gmail.com"
    subject = "TEST"
    attachment_list = ["documents/DN_Resume.pdf"]

    send_mail(sender, recipient, subject, attachment_list, text, html)