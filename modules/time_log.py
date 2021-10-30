import datetime

f=open('time_log.txt', 'r')
contents=f.read()
f.close()

f=open('time_log.txt', 'a')

if len(contents.splitlines()) < 2:
  if contents == "":
    f.write("TEST, " + str(datetime.datetime.now()) )
  else:
    f.write(", " + str(datetime.datetime.now()) +"\n" )






else:
  latest = contents.splitlines()[-1]
  if len( latest.split(',') ) == 2:
    f.write(", " + str(datetime.datetime.now()) )
  else:
    f.write("\nTEST, " + str(datetime.datetime.now()) )
    
print(latest)
print(contents.splitlines())
f.close()
