
This project generates email addresses for students based on their names and separates them by gender. It also handles special characters in names and calculates similarity between male and female names.

**Getting Started**

### Prerequisites

* Python 3.8 or later
* pandas library
* tensorflow_hub library

### Installation

1. Clone the repository: `git clone https://github.com/your-username/student-email-generator.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the project: `python main.py`

### Input Files

* `Test Files.xlsx`: An Excel file containing student names in the format "Last Name, First Name".

### Output Files

* `students_with_emails.csv`: A CSV file containing student data with generated email addresses.
* `students_with_emails.tsv`: A TSV file containing student data with generated email addresses.

### Configuration Options

* `--input-file`: Specify the input file path (default: `Test Files.xlsx`).
* `--output-dir`: Specify the output directory (default: current working directory).



### Email Generation

The project generates email addresses in the format "firstname.lastname@domain.com".

### Gender Separation

The project separates students by gender into two lists: males and females.

### Special Character Handling

The project handles special characters in names by replacing them with underscores.

### Similarity Calculation

The project calculates similarity between male and female names using a custom algorithm.


### Libraries and Dependencies

* pandas 1.3.5
* tensorflow_hub 0.12.0

### Code Structure

The project consists of the following files:

* `main.py`: The main script that runs the project.
* `functions.py`: A module containing helper functions for email generation, gender separation, and similarity calculation.

### Contributor Guidelines

* Fork the repository and create a new branch for your changes.
* Submit a pull request with a detailed description of your changes.

### Issue Tracking

Report issues or bugs on the project's GitHub issues page.

**License and Copyright**
----------------------

### License

This project is released under the MIT License.

### Copyright

Copyright 2024 Grace,Kendi,Crystal,Trevor and Alex . All rights reserved.





