def run():
  import datetime
  
  message =""
  
  filepath = 'modules/time_log.txt'
  
  f=open(filepath, 'r')
  contents=f.read()
  f.close()
  
  f=open(filepath, 'a')
  
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
  return "<p>"+ message + "</p>"