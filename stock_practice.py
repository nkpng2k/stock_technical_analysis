fhand = open('tsla_3m_20jun.csv')

count = 0
high_num = 0
low_num = 999999999
index = 0
header_list = []

first_line = fhand.readline() #takes out first line which is all strings

for line in fhand:
    line = line.rstrip() #remove white space
    line = line.strip('"') # get rid of " at beginning and end
    line = line.split('","')
    if float(line[1]) > high_num:
        high_num = float(line[1])
    elif float(line[1]) < low_num:
        low_num = float(line[1])

print '3 Month High: %g' %high_num
print '3 Month Low: %g' %low_num