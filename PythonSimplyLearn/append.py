appendMe ='even more text'
saveFile = open('Example2File.txt','a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()