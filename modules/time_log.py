import datetime

message =""

f=open('time_log.txt', 'r')
contents=f.read()
f.close()

f=open('time_log.txt', 'a')

print(contents.splitlines())
print(len(contents.splitlines() ) ) 
if len(contents.splitlines()) == 0:
  f.write("TEST, " + str(datetime.datetime.now()) )
  Message = "New log started!"






else:
  latest = contents.splitlines()[-1]
  if len( latest.split(',') ) == 2:
    f.write(", " + str(datetime.datetime.now()) )
    message = "Finished the activity started at " + str(latest.split(",")[1])
  else:
    f.write("\nTEST, " + str(datetime.datetime.now()) )
    message = "Started new activity"
  print(latest)
  print(contents.splitlines())

f.close()
print(message)