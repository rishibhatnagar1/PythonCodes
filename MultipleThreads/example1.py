import thread
import time

def print_time(threadName,delay):
	count = 0
	while (count < 100):
		time.sleep(delay)
		count +=1
		print "%s: %s" % ( threadName, time.ctime(time.time()) )
try:
	#thread.start_new_thread ( function, args[, kwargs] )
	thread.start_new_thread(print_time,("Thread-1",15))
	thread.start_new_thread(print_time,("Thread-2",3))
except:
	print "Thread not initiated "
while 1:
	pass
