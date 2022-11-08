def timeConversion(origstr):
    meridian = origstr[-2:]
    if meridian == "PM" and origstr[:2] != "12":
        origstr = str(12 + int(origstr[:2])) + origstr[2:]
    if meridian == "AM" and origstr[:2] == "12":
        origstr = "00" + origstr[2:]
    return origstr[:-2]


print(timeConversion("12:00:00AM"))