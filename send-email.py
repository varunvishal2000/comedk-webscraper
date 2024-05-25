import smtplib
import os
from email.message import EmailMessage

EMAIL_ADDRESS = 'varun.vishal.dummy@gmail.com'
EMAIL_PASSWORD = 'khxd cpwu wjdw wfgy'

subject = 'Enquiry for admission in BTech CSE or ECE with gap years and two marksheets'
body = r"""Dear reader,

I am looking for admission in BTech in Computer Science and Engineering(CSE), or BTech in Electronics and Communication Engineering (ECE).  

Regarding the above I have two queries that I am hoping you can help me with,

Query 1 - I did not have Maths in my 12th Boards and have given Maths through NIOS
Query 2 - I have a 6 year gap after my 12th the reason for which is discussed below

1.)
    I have completed my 12th class from CBSE Board in 2018 with subjects Physics, Chemistry, Biology, English and Physical Education.

    So my total marks in 12th are as follows:

        Physics - 87/100
        Chemistry - 84/100
        Biology - 77/100
        English - 73/100
        Physical Education - 94/100

    Now since I didn't do Maths during my 12th, I had given my Maths exam in January 2024 through NIOS
    and I have scored 58 marks in that, the document for each mark statement here is attached down below.

    So the revised total marks in my 12th come out to be:
    
    Physics - 87/100
    Chemistry - 84/100
    Biology - 77/100
    English - 73/100
    Physical Education - 94/100
    Maths(NIOS) - 58/100

    The percentage considering only Physics, Chemistry and Maths (PCM) is - 76.3% and Total cumulative percentage considering all subjects comes to be 78.8%. 

    The problem here is that I now have two marksheets of different boards, one from CBSE which I got in 2018 and one from NIOS which I have now in 2024. Which is what I want to get clarification on, I have contacted NIOS and CBSE and they have said they will not be able to provide a combined marksheet.
    So Kindly let me know what I can do for this situation. 

 
2.)
    I have completed my 12th in 2018 which means I have a total gap of 6 years after my 12th class. 

    There are two reasons for these gap years,

    Me and my family's original ambition was for me to be a doctor so I had given the NEET exam in 2019, 2020 and 2021.
    Financial and Family problems after 2021 due to COVID
    I come from a family where my mother and father are divorced  and my mother is the sole earner for the family. 
    In 2021, during COVID second wave my mother had fallen sick I had to leave everything and care for her. This was at the time of my NEET exam, so I couldn't perform the way I had prepared and ultimately couldn't secure a government seat.

    My mother had thankfully made a full recovery after a few months but was fired from her previous job. Situation at that point was that we didn't have money for even a B.Tech in a private college and I couldn't leave my place as my mother wasn't earning so I couldn't do anything for my higher education.

    Along with this there were also family problems which led to furthur constraints.

    Thankfully since that time, we have become more financially stable and because of that I want to apply here.


If there is any documentation that may be required please let me know, any affit-davit or any such documents.
I am readily available on the mobile number mentioned and also this email address.

I will be obliged for any help.

Best Regards,
Varun Vishal
+91 930 434 5884"""
#Making a Email object
msg = EmailMessage()
#Declaring the particulars needed for email
msg['To'] = 'varunvishal2000@gmail.com'
msg['From'] = EMAIL_ADDRESS
msg['Subject'] = subject
msg.set_content(body)
#Attaching the NIOS mark Statement
with open('Maths Mark Statement - NIOS.pdf', 'rb') as f:
    file_name = f.name
    file_data = f.read()
    file_type = 'pdf'

msg.add_attachment(file_data, maintype='document', subtype=file_type, filename=file_name)

#Attaching the 10th CBSE Marksheet
with open('10th Marksheet.jpg', 'rb') as f:
    file_name = f.name
    file_data = f.read()
    file_type = 'jpg'

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

#Attaching the 12th CBSE Marksheet
with open('Marks Statement-12th.jpg', 'rb') as f:
    file_name = f.name
    file_data = f.read()
    file_type = 'jpg'

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

#Making the smtp object which will send the email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
