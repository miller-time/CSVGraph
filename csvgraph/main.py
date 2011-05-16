#!/usr/bin/env python

"""
Specify a csv file to graph.
Assuming column 1 is X value, and each column after is a Y value
"""

from argparse import ArgumentParser
from pylab import plot, legend, xlabel, savefig

def main():
    parser = ArgumentParser(description='Plot pairs of columns from a CSV file.')
    parser.add_argument('filename')
    parser.add_argument('--pudb', action='store_true')
    args = parser.parse_args()

    f = open(args.filename)
    csv_file = f.readlines()
    f.close()

    if args.pudb:
        import pudb
        pudb.set_trace()

    csv_file[0] = csv_file[0].replace('\n','').strip('"')
    
    columns = []
    labels = csv_file[0].split(',')
    num_columns = len(labels)
    for i in range(num_columns):
        columns.append([])

    for j,row in enumerate(csv_file):
        row = csv_file[j] = row.replace('\n','')
        cells = row.split(',')
        for i,cell in enumerate(cells):
            cell = cells[i] = cell.strip('"')
            if cell.strip() == "None":
                cell = cells[i] = 0
            try:
                float(cell)
            except ValueError:
                continue
            columns[i].append(cell)

#    for i,column in enumerate(columns):
 #       print i, column, len(column)

    for i in range(1, num_columns):
        if not columns[i]:
            continue
        plot(columns[0], columns[i], label=labels[i].strip('"'))

    legend(loc='best')
    xlabel(labels[0].strip('"'))
    savefig(args.filename.split('.')[0] + '.png')


if __name__=="__main__":
    main()
