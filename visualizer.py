import sys
import csv
import time
import numpy as np
import matplotlib.pyplot as plt

def main():
  print 'File: {0}'.format(str(sys.argv[1]))

  with open(sys.argv[1], 'r') as csv_file:
    table = [row for row in csv.reader(csv_file, delimiter = ',', quotechar = '"')]

  header = table[0]
  table = [[time.strptime(row[0], '%Y/%m/%d')] +
    [float(element) for (idx, element) in enumerate(row) if idx >= 1]
    for (idx, row) in enumerate(table) if idx >= 2]

  print 'Header: {0}'.format(header)

  np_table = np.array(table)

  # print np_table.shape
  # print np_table[:, 1]

  plt.plot(np_table[:, 2], np_table[:, 1])

  plt.show()

if __name__ == '__main__':
  main()
