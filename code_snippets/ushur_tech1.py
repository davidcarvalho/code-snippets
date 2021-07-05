input1 = '11:32:47PM'
input2 = '12:06:60AM'
input3 = '1234567890'


def validate_time(time_string):
    # check for length
    if len(time_string) == 10 and len(time_string.split(':')) == 3:
        # split and validate
        hour = int(time_string[0:2])
        min = int(time_string[3:5])
        sec = int(time_string[6:8])
        am_pm = time_string[8:]
        if (0 < hour <= 12) and (0 < min <= 59) and (0 < sec <= 59) and (am_pm == 'AM' or am_pm == 'PM'):
            return True
        else:
            return False
    else:
        return False


print(validate_time(input3))
