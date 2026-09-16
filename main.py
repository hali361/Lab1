# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException


def compute_BMI(height: float, weight: float) -> float:
    """
    compute body-mass-index:  weight / (mass**2)
    :param height: height in meters
    :param weight: weight in kg
    :return: BMI in kg/m**2
    """
    return round(weight / (height ** 2), 2)

def parse_row(row: str) -> list:
    """
    Accepts a single row (string) read from the data file.
    Splits it into a list of individual values, cast to numeric datatypes where appropriate.
    :param row: the string row read from the file
    :return: the parsed row, as a list
    """
    values = row.split(",")

    # check for missing values in a row
    if len(values) != 5:
        raise TextFormatException("incorrect number of values in the row")

    # check for empty values in a row
    if "" in values:
        raise MissingValueException(f"missing {values.index('')} in the row")

    values[0] = int(values[0])
    values[3] = float(values[3])
    values[4] = float(values[4])

    # outlier check for height in meters (should be less than 3 meters)
    if values[4] > 3:
        raise MeasurementUnitException("height isn't in meters")

    return values

def main():
    
    # your code here
    with open("data.csv", "r") as data_file, open("bmi.csv", "w") as output_file:
        output_file.write("Exam ID,BMI\n")

        #read header line to avoid errors when parsing the data
        data_file.readline()

        for row in data_file:
            try:
                parsed_row = parse_row(row)
                bmi = compute_BMI(parsed_row[4], parsed_row[3])
                output_file.write(f"{parsed_row[0]},{bmi}\n")

            except MissingValueException:
                exam_id = row.split(",")[0]
                print(f"Exam ID {exam_id}: missing value")

            except MeasurementUnitException:
                exam_id = row.split(",")[0]
                print(f"Exam ID {exam_id}: height isn't in meters")

            except TextFormatException:
                exam_id = row.split(",")[0]
                print(f"Exam ID {exam_id}: incorrect name format")

main()