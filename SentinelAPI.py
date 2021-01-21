import requests, sys, webbrowser, bs4, time, ping3, os
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
    tlds=['com','in','net','org','store','co']
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
        url = 'https://www.virustotal.com/vtapi/v2/url/report'
        params = {'apikey': 'insert_your_api_key', 'resource': text}
        response = requests.get(url, params=params)
        x=response.json()
        l=x["positives"]
        if l==0:
            print("Hurray! This website is SAFE to visit")
            stat="safe"
        else:
            print("PROCEED WITH CAUTION,THIS SITE MIGHT BE UNSAFE")
        if stat=='safe':
            url2 = 'https://www.virustotal.com/vtapi/v2/domain/report'
            params_ = {'apikey':'insert_your_api_key','domain':text}
            resp = requests.get(url2, params=params_)
            o=resp.json()
            cat=o['sophos category']
            print()
            print("People browse",text,"for",cat)
            print()
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
