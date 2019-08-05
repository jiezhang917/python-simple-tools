from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook

with open("code.txt", "r", encoding="utf-8") as f:
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    dest_names = soup.select(".unified-postcard__header h3 a")
    domain = 'https://www.booking.com'
    wb = Workbook()
    sheet1 = wb.add_sheet('Homepage Destinations')
    sheet1.write(0, 0, 'Destination Name')
    sheet1.write(0, 1, 'Destination URL')
    with open('links.txt', 'w', encoding='utf-8') as links:
        count = 1
        for dest_name in dest_names:
            chart_name = dest_name.contents[0].replace('\n', '')
            chart_url = (domain + dest_name['href'].replace('\n', ''))
            data = "destination name：" + chart_name + "\n" + "destination url：" + chart_url + "\n"
            # print(data)
            links.writelines(data + '===============' + "\n")
            sheet1.write(count, 0, chart_name)
            sheet1.write(count, 1, chart_url)
            count += 1

    wb.save('booking_urls.xls')
