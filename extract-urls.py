import bs4, requests, re, pandas as pd

url = "https://www.comedk.org/be-colleges"

col_dict = {"Name": [], "Place":[], "Phone Numbers":[], "Emails":[]}

page = requests.get(url)

soup = bs4.BeautifulSoup(page.text, "html.parser")

table_rows = soup.select("div table tbody tr")

n = len(table_rows)

for i in range(1, n):
    
    col_url = f"https://www.comedk.org/{table_rows[i].select("a")[0].get("href")}"

    col_page = requests.get(col_url)

    col_soup = soup = bs4.BeautifulSoup(col_page.text, 'html.parser')

    col_name = soup.select(".inner-e1-sec1 h1")[0].text
    col_city = soup.select(".inner-e1-sec1 h6")[0].text

    col_contact_info_text = soup.select("#contact-college p")

    temp = ""

    for items in col_contact_info_text:
        temp = temp + items.text
    
    #name_pattern = re.compile(r"(Dr|Prof|Mr|Mrs)\.?(\s*\w*)*")
    email_pattern = re.compile(r"[:\s](\w+[.-_]?\w+)(\w+[.-_]?\w+)(\w+[.-_]?\w+)@(\w+[.-_]?\w+)+")
    ph_pattern = re.compile(r"[+]?\d+[-\s]?\d+")

    emails = []

    for x in email_pattern.finditer(temp):
        emails.append(x.group())

    ph_nums = []

    for x in ph_pattern.finditer(temp):
        ph_nums.append(x.group())
    
    col_dict["Name"].append(col_name)
    col_dict["Place"].append(col_city)
    col_dict["Phone Numbers"].append(ph_nums)
    col_dict["Emails"].append(emails)

    df = pd.DataFrame(col_dict)

print(df)