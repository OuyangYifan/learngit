from datetime import datetime
from datetime import date
import threading
import itertools
import time
import  sys
def date_calc():
   frm_date = date(2019,01,05)
   fin_date = date(2019,12,26)
   now_date = date.today()
   Span_date = date.today() - frm_date
   Days_span = Span_date.days + 1
   COUNT_9s = "Accord to Chinese Lunar Calendar, it's in #{0} NINEs,{1} days."
   print(COUNT_9s.format(int(Days_span/9 + 1),(Days_span)))
   
   Span_date = date.today() - fin_date
   Days_span = Span_date.days + 1
   print("%d days passed since purchase of the financial product"%(Days_span))

   job = threading.Event()
   fun = threading.Thread(target=have_fun,
                               args=('have fun~~~thinking!', job))
   print('fun object:', fun)  
   fun.start()  
   result = slow_function()  
   job.set()  
   fun.join() 
   return result

def slow_function():  
    # pretend waiting a long time for I/O
    time.sleep(3)  
    return 23   

def have_fun(msg,job_done):
        '''msg = have fun~~~thinking!'''
        write,flush = sys.stdout.write,sys.stdout.flush
        
        for char in  itertools.cycle('|/-\\$'):
                #print(char)
                status = char +' ' + msg
                write(status)
                flush()
                write('\x08' * (len(status) ))  #move the cursor back with backspace characters (\x08).
                #flush()
                if job_done.wait(.1):
                        #flush()
                        break
        #flush()
        write(' '*len(status) + '\x08'*len(status))

def main():
    result = date_calc()  
    print('Answer:', result)

if __name__ == '__main__':
    main()

