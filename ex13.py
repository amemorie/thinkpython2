import string

def make_worddictionary(filename, skip):
    fin = open(filename)
    whitepunct = string.punctuation + string.whitespace+'ã'+'©'+'¢'
    dd = {}
    counter = 0
    for line in fin:
        counter += 1
        if counter > skip:
            words = line.strip().split(' ')
            for word in words:
                word = word.lower()
                for f in whitepunct:
                    word = word.replace(f,"")
                if word != '':
                    dd[word] = dd.get(word,0)+1
    return dd


data = [('StendhalFr.txt',43),('StendhalEn.txt',0)]

for ii in range(len(data)):
    dd = make_worddictionary(data[ii][0],data[ii][1])
    print(data[ii][0], len(dd), (sum(dd.values())))
    print(dd)
