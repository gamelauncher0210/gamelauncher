import urllib,urllib.request
web = input("input URL:")
response = urllib.request.urlopen(web)
html = response.read()
print(html)
fileout = open("html.txt","w")
fileout.write(str(html))
fileout.close()
