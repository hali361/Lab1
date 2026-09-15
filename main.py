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
    return weight / (height ** 2)

def parse_row(row: str) -> list:
    """
    Accepts a single row (string) read from the data file.
    Splits it into a list of individual values, cast to numeric datatypes where appropriate.
    :param row: the string row read from the file
    :return: the parsed row, as a list
    """
    values = row.split(",")

    if len(values) != 5:
        raise TextFormatException("incorrect value of numbers")

    if "" in values:
        raise MissingValueException("missing value")

    values[0] = int(values[0])
    values[3] = float(values[3])
    values[4] = float(values[4])

    if values[4] > 3:
        raise MeasurementUnitException("height isn't in meters")

    return values

def main():
    
    # your code here
    with open("data.csv", "r") as data_file, open("bmi.csv", "w") as output_file:
        output_file.write("Exam ID,BMI\n")

        data_file.readline()

        for row in data_file:
            try:
                parsed_row = parse_row(row)
                bmi = compute_BMI(parsed_row[4], parsed_row[3])
                print(bmi)

            except MissingValueException:
                exam_id = row.split(",")[0]
                print(f"Exam ID {exam_id}: missing value")

            except MeasurementUnitException:
                exam_id = row.split(",")[0]
                print(f"Exam ID {exam_id}: height isn't in meters")

            except TextFormatException:
                exam_id = row.split(",")[0]
                print(f"Exam ID {exam_id}: incorrect text format")

main()