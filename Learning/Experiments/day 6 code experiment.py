contents =["Rich man of babylon","The key tools of investment","The good,the bad, the ugly"]

filenames = ["doc.txt","report.txt","presentation.txt"]

for content,filename in zip(contents,filenames):
    file = open(f"../files/{filename}","w")
    file.writelines(content)