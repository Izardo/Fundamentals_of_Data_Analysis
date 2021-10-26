# Program to extract CAO 2021 data and convert to CSV format 


import re               # Regular expressions
import requests as rq   # HTTP requests

# Retrieving CAO points from the webserver.
response = rq.get('http://www2.cao.ie/points/l8.php')

# Compiles the regular expression for matching lines so it doesn't recompile repeatedly.
re_course = re.compile(r'([A-Z]{2}[0-9]{3})  (.*)([0-9]{3})(\*?) *')  # 'r' python treats string as raw string and doesnt evaluate back slashes
                                                                    # \ {character} means we want the literal character ie., *
                                                                    # ? means 0 or 1 of 
                                                                    # + means 1 or more of 

# Keeping count of the courses we are processing.
course_count = 0

# Looping through and printing data from response line by line.
for line in response.iter_lines():

    # Matches the string specified in re_course, returning only the courses from the response
    if re_course.fullmatch(line.decode('iso-8859-1')):
        # Adds one to the course count
        course_count += 1
        print(line)
        csv_version = re_course.sub(r'\1,\2,\3,\4', line.decode('iso-8859-1'))
        print(csv_version)
print(f"Line count: {course_count}")


