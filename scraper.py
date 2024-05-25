import bs4, requests, re

url = "https://www.comedk.org/college-acharya-institute-of-technology"

page = requests.get(url)

soup = bs4.BeautifulSoup(page.text, 'html.parser')

pat = r""
#Extracted the h1 from the class given
col_name = soup.select(".inner-e1-sec1 h1")[0].text
#
col_city = soup.select(".inner-e1-sec1 h6")[0].text
#
col_contact_info_text = soup.select("#contact-college p")

temp = ""

for items in col_contact_info_text:
    temp = temp + items.text

#print(temp)

#col_head_name = soup.select("#contact-college p")[0].text

#col_ph_no = soup.select("#contact-college p")[1].text

#col_email_id =soup.select("#contact-college p")[2].text

name_pattern = re.compile(r"(Dr|Prof|Mr|Mrs)\.?(\s*\w*)*")

a = "varunvishal2000@gmail.co.in-net a.smld;alsmd hello@abc.in"

email_pattern = re.compile(r"[\s:]?(\w*[.-_]?)*@(\w*[.-]+\w*)*")

emails = []

ph_pattern = re.compile(r"[+]?\d+[-\s]?\d+")

for x in email_pattern.finditer(temp):
    emails.append(x.group())

print(emails)