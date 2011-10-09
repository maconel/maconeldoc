#coding: utf8
import sys
import time

def main():
    fromDate = None

    #get from date.
    if len(sys.argv) < 2:
        fromDate = time.time()
    else:
        try:
            fromDate = time.mktime(time.strptime(sys.argv[1], '%Y%m%d'))
        except:
            print 'usage: make_a_week_log.py 20100607'
            return

    #make file.
    for i in range(0, 7):
        date = time.localtime(fromDate + 24 * 60 * 60 * i)
        if date[6] == 5:        #Sat
            continue
        elif date[6] == 6:      #Sun
            continue
        elif date[6] == 4:      #Fri
            file(time.strftime('%Y%m%d.txt', date), 'at')
            file(time.strftime('%Y%m%d_.txt', date), 'at')
            break
        else:                   #Mon - Fri
            file(time.strftime('%Y%m%d.txt', date), 'at')

if __name__ == '__main__':
    main()
