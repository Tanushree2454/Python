#write-just write anything already written to that file will be gone overwritten (example a picture)
#  read
#  append- is just gonna add to what ever was previously there in that file 
writeMe = 'Example text'
saveFile = open('exampleWrite.txt','w')
saveFile.write(writeMe)
saveFile.close()