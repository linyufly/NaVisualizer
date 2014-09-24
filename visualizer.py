import sys
import csv
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import MonthLocator, DayLocator

def main():
  print 'File: {0}'.format(str(sys.argv[1]))

  with open(sys.argv[1], 'r') as csv_file:
    table = [row for row in csv.reader(csv_file, delimiter = ',', quotechar = '"')]

  header = table[0]
  table = [[datetime.strptime(row[0], '%Y/%m/%d')] +
    [float(element) for (idx, element) in enumerate(row) if idx >= 1]
    for (idx, row) in enumerate(table) if idx >= 2]

  print 'Header: {0}'.format(header)

  np_table = np.array(table)

  date_list = np_table[:, 0]
  close_list = np_table[:, 1]
  open_list = np_table[:, 3]
  high_list = np_table[:, 4]
  low_list = np_table[:, 5]

  fig, close_plot = plt.subplots()

  close_plot.plot(date_list, low_list, 'b', date_list, high_list, 'r')

  close_plot.set_ylim(0)

  # format the ticks
  close_plot.xaxis.set_major_locator(MonthLocator())
  close_plot.xaxis.set_major_formatter(DateFormatter('%Y-%m'))
  close_plot.xaxis.set_minor_locator(DayLocator())

  # format the coordinate message box
  def PriceFormatter(x): return '$%.2f' % x
  close_plot.format_xdata = DateFormatter('%Y-%m-%d')
  close_plot.format_ydata = PriceFormatter
  close_plot.grid(True)

  # for x-axis
  fig.autofmt_xdate()

  plt.show()

if __name__ == '__main__':
  main()
