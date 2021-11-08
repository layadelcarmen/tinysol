# CSV Percentile filter

Returns all records in a CSV file over a percentile value in the specified column.

## Description

Returns all records in a CSV file over a percentile value in the specified column.

## Getting Started

### Dependencies

*  Pandas
*  Pytest

### Installing

* Download the repo



```
cd tinysol

pip install -e .
```


### Executing program

* Run as a python script

* USAGE: csv-processing [inputfile] [column_name] [percentile]


```
csv-processing [inputfile] [column_name] [percentile]
```

### Discussing the solution

The Problem: Given NYC “Yellow Taxi” Trips Data, return all the trips over 0.9 percentile in distance traveled.

The first decision is to inspect the data, how big is, its necesary to persist the data? or in memory processing is enough?  Pandas could solve the problem.

It's necesary to create a data structure with the columns names, and use this as further condition in the data validation process? Json offers the amazing key value characteristic, so a result exposed in this format can be easily to undertand and use for developers.

Data quality: If you want to calculate a percentile, the column should contain numeric values. Percentile function ignores NA values.


#### Define a processing module

Here the decision to go with OO definition or to decide if a functional approach is the simplest way to sove the problem.

A Test Driven Development is the more secure way to test and evolve the solution.


#### Define methods thinking in the future

How modular could be the module to let further processing for different columns and percentile values. Could create a more general function to call different funtions like sum, mean, etc. But here once the trade off with the simplicity, usability and solve the problem.

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

Laya Rabasa 
* [GitHub](https://github.com/layadelcarmen)
* [Linkedin](https://www.linkedin.com/in/layarabasa/)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details