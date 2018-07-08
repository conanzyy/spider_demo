#coding:utf-8

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self,new_data):
        if new_data is None:
            return
        self.datas.append(new_data)


    def output_html(self):
        fout = open('output.html','w',encoding='utf-8')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border='1' word-break:break-all cellspacing='0' cellpadding='0' style='table-layout:fixed; width:100%'>")
        fout.write("<tr>")
        fout.write("<th>url</th>")
        fout.write("<th>标题</th>")
        fout.write("<th>摘要</th>")
        fout.write("</tr>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td style='width:30%%; WORD-WRAP: break-word; word-break:break-all'>%s</td>" % data['url'])
            fout.write("<td style='width:10%%; WORD-WRAP: break-word; word-break:break-all'>%s</td>" % data['title'])
            fout.write("<td style='width:70%%; WORD-WRAP: break-word; word-break:break-all'>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()