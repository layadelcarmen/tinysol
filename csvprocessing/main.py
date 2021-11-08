import sys, getopt

from .csvprocessing import load_csv_data, calculate_percentile_for_column, get_records_above, check_data_type


def _print_help():
    _help = '''
    USAGE: script.py <inputfile> <column_name> <percentile>

    Example: 
    
    file: 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-03.csv

    column: trip_distance

    percentile: 0.9

    '''
    print(_help)


def pipeline_percentile(file, column, percentile):
    data = load_csv_data(file)
    if check_data_type(data, column, ["float64"]):
        val_percentile = calculate_percentile_for_column(data, column, percentile)
        print(get_records_above(data, column, val_percentile))
    else:
        print("Could not calculate the percentile in a non-numeric column.")


def main():

    argv = sys.argv
    try:
        opts, args = getopt.getopt(argv,"h")
    except getopt.GetoptError:
        _print_help()
        sys.exit(2)
   
    if len(args) == 2 and args[1] == 'h':
        _print_help()
        sys.exit()
    elif len(args) == 4:       
        file = args[1] 
        column =  args[2]
        percentile = float(args[3])
    else:
        _print_help()
        sys.exit()

    pipeline_percentile(file, column, percentile)


if __name__ == '__main__':
    main()