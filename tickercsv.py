from csv import writer
import lists

tickername = 'FB'
timeframe = '15min'

list_data = ['Date','Open','High','Low','Close','Volume']

lists.lists_stocks(tickername,timeframe)
csvname = tickername + '_' + timeframe + '.csv'

with open('Tickers\\' + csvname, 'w', newline='') as f_object:
    # Pass the CSV  file object to the writer() function
    writer_object = writer(f_object)
    writer_object.writerow(list_data)

    for x in range(len(lists.date)):
        f_object.write(lists.date[-(1+x)])
        f_object.write(',')
        f_object.write(str(lists.open[-(1+x)]))
        f_object.write(',')
        f_object.write(str(lists.high[-(1+x)]))
        f_object.write(',')
        f_object.write(str(lists.low[-(1+x)]))
        f_object.write(',')
        f_object.write(str(lists.close[-(1+x)]))
        f_object.write(',')
        f_object.write(str(lists.volume[-(1+x)]))
        f_object.write("\n")

lines_seen = set() # holds lines already seen

with open('Tickers\\' + csvname, "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i not in lines_seen:
            f.write(i)
            lines_seen.add(i)
    f.truncate()

with open('Tickers\\' + csvname, "r") as txt_file:
  new_data = list(set(txt_file))

f_object.close()