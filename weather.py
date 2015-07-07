import urllib2, re

response = urllib2.urlopen("http://www.nmc.cn/publish/forecast/ACQ/zhongqing.html")
data = response.read()
string = """div class="row wd"> 
       <div class="label h3_wd">
        .*?
       </div> 
       <div>
        .*?
       </div> 
       <div>
        .*? 
       </div> 
       <div>
        .*? 
       </div> 
       <div>
        .*? 
       </div> 
       <div>
        .*? 
       </div> 
       <div>
        .*? 
       </div> 
       <div>
        .*? 
       </div> 
       <div>
        .*? 
       </div> 
      </div> """
pattern = re.compile(string)
items = re.findall(pattern, data)
s = "".join(str(items).split())
s = s[1:len(s)-1]
print s
p = """<div>.*?</div>""" 
pa= re.compile(p)
items = re.findall(pa, s)
for i in items:
      print i
#print s.join(str(items).split())
