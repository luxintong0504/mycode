import codecs
def change(f1,e1,f2,e2):
  fp = codecs.open(f1,'r', e1)
  texts = fp.read()
  fp.close()
  a = open(f2,"w")
  a.write(texts)
print(__name__)
if __name__=="__main__":
  change("harry-potter.txt","gb18030","hahaha2.txt","utf-8")
  print("============")