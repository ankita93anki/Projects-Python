import csv 

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('students.csv', 'r')  as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

with open('new_students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','Age','Grade'])
    writer.writerow(['Alice', 20,'A'])
    writer.writerow(['Bob', 21, 'B'])

with open('new_students.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name','Math','Science','English'])
    writer.writeheader()
    writer.writerow({'Name':'Daisy', 'Math':88, 'Science':92,'English':85})


#Student Report Generator
import csv

#Step 1: Read Student data and calculate averages
def process_student_data(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            student_reports = []
            for row in reader:
                name = row['Name']
                math = int(row['Math'])
                science = int(row['Science'])
                english = int(row['English'])
                average = round((math+science+english) / 3, 2)
                status = "Pass" if average >= 60 else "Fail"

                student_reports.append({
                    'Name': name,
                    'Math': math,
                    'Science': science,
                    'English': english,
                    'Average': average,
                    'Status': status
                })

        #Step 2: Write processed data to a new CSV file
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['Name','Math','Science','English','Average','Status']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_reports)
        print(f"Processed data has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file} not found")
    except KeyError:
        print("Error: Invalid column names in the input file")
    except Exception as e:
        print(f"An error occurred: {e}")

#Main Program
input_file = 'students.csv'
output_file = 'student_report.csv'
process_student_data(input_file, output_file)

