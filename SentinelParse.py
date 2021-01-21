import requests, sys, webbrowser, bs4, time, ping3
print()
def main():
    print()
    burl=input("Enter site name, type exit to quit: ")
    if burl=="exit":
        quit()
    else:
        pass
    print()
    text=''
    tlds=['com','in','net','org','store']
    for l in tlds:
        if l in burl:
            m=burl.split(str(l))
            k=m[0]
            if 'https' in k:
                beautify=k.lstrip('https://')
                text=beautify+l
            elif 'http' in k:
                beautify=k.lstrip('http://')
                text=beautify+l
            else:
                text=k+l
            break
    from ping3 import ping, verbose_ping
    a=ping(text) 
    if a!=False:
        print("ANALYZING WEBSITE...")
        print()
        stat=''
        url= 'https://safeweb.norton.com/report/show?url='+text
        request_result=requests.get(url)
        soup=bs4.BeautifulSoup(request_result.text,"html.parser")
        c=soup.find('div', class_="span8").text
        index=c.find('SAFE')
        if index==-1:
            print('PROCEED WITH CAUTION,THIS SITE MIGHT BE UNSAFE')
        else:
            print('Hurray! This website is SAFE to visit')
            stat='safe'
        url2= 'https://www.fortiguard.com/webfilter?q='+text+'&version=8'
        request_res=requests.get(url2)
        soup2=bs4.BeautifulSoup(request_res.text,"html.parser")
        l=soup2.find("meta",{"name":"description","property":"description"})['content']
        u=l.split(':')
        print()
        print("People browse",text,"for",u[1])
        print()
        time.sleep(1)
        if stat=='safe':
            open=input("Would you like to open the website directly(y or n)?")
            if open=='y' or open=='Y':
                webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(burl)
                main()
            else:
                main()
        else:
            main()
    else:
        print("Please enter a valid site")
        main()
main()
