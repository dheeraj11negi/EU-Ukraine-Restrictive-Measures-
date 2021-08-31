import json
import requests
from scrapinghelp import htmlhelper
import hashlib

class ExtractData:
    def crawling(list,convertmonthdate,convert_date):
        newlist=[]
        for ele in list:
            d = {

                "Title": "",
                "Source": "https://www.consilium.europa.eu/en/policies/sanctions/ukraine-crisis/history-ukraine-crisis/",
                "publishedAt": "",
                "URL": "",
                "query": "",
                "uid": "",
                "Content": ""
            }

            try:
                getnewurl=ele['geturl']
                if getnewurl!="":
                    res=requests.get(getnewurl)
                    print(res)
                    if res.status_code==200:
                        source=htmlhelper.returnformatedhtml(res.text)
                        getdate=htmlhelper.returnvalue(source,"<div class=\"col-md-9 council-left-content-basic council-main-title\">","</ul>")

                        if getdate!="":
                            getansdate=htmlhelper.collecturl(getdate,"<li>","</li>")
                            if len(getansdate)==3:
                                try:
                                    getorigdate=getansdate[1].split(" ")
                                    getyear=getorigdate[len(getorigdate)-1]
                                    getmonth=getorigdate[len(getorigdate)-2]
                                    getdate=getorigdate[len(getorigdate)-3]

                                    if getmonth in convertmonthdate:
                                        getmonth=convertmonthdate[getmonth]

                                    if getdate in convert_date:
                                        getdate=convert_date[getdate]


                                    getfulldate=getyear+"-"+getmonth+"-"+getdate
                                    if getfulldate!='':
                                        d['publishedAt']=getfulldate
                                except:
                                    pass

                            else:
                                print("jg")








            except:
                pass

            try:
                gettitle=ele['gettitle']
                if gettitle!="":
                    d['Title']=gettitle

            except:
                pass

            try:
                getcontent=ele['getcontent']
                if getcontent!="":
                    d['Content']=getcontent
            except:
                pass

            try:
                d["URL"]=ele['geturl']
            except:
                pass

            try:
                d["uid"] = hashlib.sha256(((d["Source"] + d["Title"]).lower()).encode()).hexdigest()
            except:
                pass

            try:
                newlist.append(d)
            except:
                pass

        try:
                with open('EU_pressrelease_list.json', 'w', encoding="utf-8") as file:
                    json.dump(newlist, file, ensure_ascii=False, indent=4)

        except:
            pass






