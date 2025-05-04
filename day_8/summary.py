import re

def readData(fromfile1):
    data = ""
    # Reading
    f = open(file= fromfile1, mode= "r")
    try:
        data=f.read()
    except Exception:
        print("Error while reading file")
    else:
        print(f"Data Read --> \n{data}")
    finally:
        f.close()
        return data
        # pass
strdata=readData("abc.txt")
# print(len(re.findall("[a-z]",strdata)))
# smallcount=len(re.findall("[a-z]",strdata))
print((re.findall("[A-Z]",strdata)))
wordcounts= len(strdata)
print(f"wordCounts {wordcounts}")
uppcount=len(re.findall("[A-Z]",strdata))
print(uppcount)
vocount=len(re.findall("[a,e,i,o,u]",strdata.lower()))
print(vocount)
consocount=len(re.findall("[b-df-hj-np-tv-z]",strdata.lower()))
print(consocount)
spacecount=len(re.findall("[\s]",strdata.lower()))
print(f"space cout {spacecount}")
nelinecount=len(re.findall("[\n]",strdata.lower()))
print(f"nextline cout {nelinecount}")
specharcount=len(re.findall("[,._$@]",strdata.lower()))
print(f"spechar cout {specharcount}")

