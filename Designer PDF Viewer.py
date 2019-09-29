h=[1, 3, 1, 3, 1, 4, 1, 3 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5, 5, 5, 5, 5, 5, 5, 5 ,5 ,5]
def designerPdfViewer(h, word):
    harfler=['a','b',"c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',    't','u','v','w','x','y','z']
    new={}
    empty=[]
    for i in range(26):
        new[harfler[i]]=h[i]
    for i in word:
        if i in new.keys():
            empty.append(new[i])
    return (max(empty)*len(word))