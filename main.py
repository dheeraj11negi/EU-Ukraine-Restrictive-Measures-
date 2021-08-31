import requests
from scrapinghelp import htmlhelper
from Extract_Data import ExtractData
if __name__=="__main__":
    url="https://www.consilium.europa.eu/en/policies/sanctions/ukraine-crisis/history-ukraine-crisis/"
    res=requests.get(url)
    print(res)
    source=htmlhelper.returnformatedhtml(res.text)
    getatr=htmlhelper.collecturl(source,"</h3>","</ul>")

    list=[]
    for ele in getatr:
        arrdict = {
            "geturl": "https://www.consilium.europa.eu",
            "getdate": "",
            "gettitle": "",
            "getcontent": ""
        }
        if "<li><a href=\"/en/policies/sanctions/ukraine-crisis/\"" in ele:
            continue
        else:
            try:
                url=htmlhelper.returnvalue(ele,"<a href=\"","/\"")
                if url!="":
                    arrdict['geturl']=arrdict['geturl']+url
            except:
                pass

            try:
                gettitle=htmlhelper.returnvalue(ele,"title=\"","\">")
                if gettitle!="":
                    arrdict['gettitle']=gettitle

            except:
                pass

            try:
                list.append(arrdict)
            except:
                pass

            try:
                mystring=""
                contentarr=htmlhelper.collecturl(ele,"<p>","</p>")
                if len(contentarr)>1:

                    for go in contentarr:
                        mystring=mystring+go.replace("<strong>","").replace("</strong>","")

                    arrdict['getcontent']=mystring
                    mystring=""


                    pass
                else:
                    mystring=mystring+contentarr[0].replace("<strong>","").replace("</strong>","")
                    if mystring!="":
                        arrdict['getcontent']=mystring
                        mystring=""

            except:
                pass

    convertmonthdate = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }

    convert_date = {
        "1": "01",
        "2": "02",
        "3": "03",
        "4": "04",
        "5": "05",
        '6': "06",
        "7": "07",
        "8": "08",
        "9": "09"
    }




    ExtractData.crawling(list,convertmonthdate,convert_date)














