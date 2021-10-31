def run():
  import datetime
  from readabledelta import readabledelta
  
  message =""
  timeformat = "%a %d %m %Y %H:%M:%S"
  
  filepath = 'modules/time_log.txt'
  
  f=open(filepath, 'r')
  contents=f.read()
  f.close()
  
  f=open(filepath, 'a')
  
  #print(contents.splitlines())
  #print(len(contents.splitlines() ) ) 
  if len(contents.splitlines()) == 0:
    f.write("TEST, " + str(datetime.datetime.now().strftime(timeformat)) )
    message = "<h1>New log started!</h1>"
  
  
  else:
    latest = contents.splitlines()[-1]
    if len( latest.split(',') ) == 2:
      f.write(", " + str(datetime.datetime.now().strftime(timeformat)) )
      start = latest.split(',')[1][1:]
      print("test")
      duration = datetime.datetime.now() - datetime.datetime.strptime(start, timeformat)
      message = "<h1>Finished the activity started at " + str(latest.split(",")[1]) + "</h1><h2>Time duration: "+ str(readabledelta(duration)) + "</h2>"
    else:
      f.write("\nTEST, " + str(datetime.datetime.now().strftime(timeformat)) )
      message = "<h1>Started new activity</h1>"
    #print(latest)
    #print(contents.splitlines())
  
  f.close()
  return message
  