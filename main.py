from flask import jsonify, request

from pyms.flask.app import Microservice

from csvprocessing import load_csv_data, calculate_percentile_for_column, get_records_above

ms = Microservice() 
app = ms.create_app() 


@app.route("/") 
def example():
    return jsonify({"main": "Hello, Yellow taxi"})


# file_example = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-03.csv'

@app.route("/percentile") 
def pipeline_percentile():
    file = request.args.get('file')
    column = request.args.get('column')
    percentil = float(request.args.get('age'))
    data = load_csv_data(file)
    val_percentile = calculate_percentile_for_column(data, column, percentil)
    return get_records_above(data, column, val_percentile)


if __name__ == '__main__':
    app.run()