import sys
import argparse
import csv
import operator


def main():
    parser = argparse.ArgumentParser(description='Sort a CSV file.')
    parser.add_argument('-c', '--column', help='Column to sort by')
    parser.add_argument('-f', '--file', help='Input file to sort')
    parser.add_argument('-o', '--output', help='Output file')

    args = vars(parser.parse_args())

    if args['file'] is None:
        input_file = 'input.csv'
    else:
        input_file = args['file']

    if args['output'] is None:
        output_file = 'output.csv'
    else:
        output_file = args['output']

    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        headers = next(reader)
        data = [line for line in reader]

    if args['column'] is None:
        column = get_column(headers)
    else:
        column = args['column']

    validate_column(headers, column)

    sorted_data = sort_csv(headers, data, column)

    write_output(headers, sorted_data, output_file)


def get_column(headers):
    """
    Get the column that the user wants to use for sorting.  This function
    should only be called if the user did not specify a column argument.  If
    no column is specified, the first column in the file will be used.
    """

    column = input("What column do you want to sort by?  (Press Enter for default, %s) " % headers[0])

    if column == '':
        column = headers[0]

    return column


def validate_column(headers, column):
    """
    Validate that the column you're sorting by actually exists in the file,
    whether it was specified by user input in the get_column() function, or
    by the -c argument.
    """

    if column not in headers:
        print("That column is not in the file.  Exiting.")
        sys.exit(0)
    return


def sort_csv(headers, data, column):
    """
    Takes the headers (first line) of the CSV file, the file's data (the other
    lines after the first line), and the column the user wants to sort on, and
    sorts the data in the file.  Returns the sorted file.
    """

    index = headers.index(column)

    sorted_data = []

    sorted_data = sorted(data, key=lambda x: x[index])

    return sorted_data


def write_output(headers, sorted_data, output_file):
    """
    Write the sorted data to the output file
    """

    with open(output_file, 'w', newline='') as csvfile:
        csvfile = csv.writer(csvfile, delimiter='\t')
        csvfile.writerow(headers)
        csvfile.writerows(sorted_data)


if __name__ == '__main__':
    main()
