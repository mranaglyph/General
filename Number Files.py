# Importing the necessary modules.

import os, time

# Creating empty lists (arrays) and variables to be used/filled later.

dir_arr = []
dir_arr_proper = []
dir_arr_proper2 = []
m_times = []
num = []
output_arr = []
x = 0
y = 0

# List files in a given directory, add files to dir_arr list, then print dir_arr.
# Saving path and path2 to separate the path itself from the files in that path.

path = input('\nEnter Location Path of File(s) in Folder : ')
path2 = os.listdir(path)
dir_arr.append(path2)

print('\n{}'.format(dir_arr))

# This process iterates over the generated list just to change it 
# from a multidimensional<?> (appears as : [[item]]) list to a 1D list (array), dir_arr_proper.

for s in path2:
    dir_arr_proper.append(s)

print('\n{}'.format(dir_arr_proper))

# Now that it is a 1D list, path2 (now dir_arr_proper) can be used here to 
# define the proper range. From there, the modified times of the files can be 
# produced in order of thier appearance in the proper list.

for i in range(len(dir_arr_proper)):
    mod = os.path.getmtime(path + '\\' + dir_arr_proper[i])
    m_times.append(mod)
    num.append(str(i))

print('\n{}'.format(m_times))

# Now we have the original list of m_times, and can be sorted 
# (permanent not .sort() or sorted() with m_times2 = m_times).
# Needs a copy sorted so we still have the original 
# Out of Order list as a reference.

m_times2 = m_times.copy()
m_times2 = sorted(m_times2)

print('\n{}'.format(m_times2))

#                       !Important!
# This next while loop is basically the heart of the program, 
# which allows the orginal file list from the path the user input
# to be organized by the file's modified date within the directory.
# It iterates over the m_times2 (x-set) list and compares each item
# in m_times2 to each item in m_times (y-set). Then, 
# if the values are not equal, it checks the next 
# item in y-set. If the values are equal, it adds the file value to 
# a different list (dir_arr_proper2). The file [name] value that it
# adds is referenced from the original dir_arr_proper
# that directly correlates to the m_times value 
# compared on the y-set. It then continues comparisons until both
# x and y sets are exhausted and all file names from z-set (unordered)
# are now in a copy of z-set, ordered. 
#
# Visual Aide Example:
#                       
#                       [x1]\---/[y3] if =, then [z3]\  [z1]
#                       |x2|-\-/-|y5| if =, then |z5|-\ |z2|
#                       |x3|--\--|y1| if =, then |z1|-->|z3| (Copy of z-set, now ordered)
#                       |x4|-/-\-|y2| if =, then |z2|-/ |z4|
#                       [x5]/---\[y4] if =, then [z4]/  [z5]
# 
# TL;DR:
#       Every value in the ordered list is compared to 
#       every value in the unordered list. When a match 
#       is found, it references the orginal file name
#       that corresponds to that position in the m_times list, 
#       and adds that file name to a new list, 
#       now sorted by file modified date.

while (x != len(m_times2)) and (y != len(m_times)):
    if m_times2[x] != m_times[y]:
        y += 1
        continue
    elif m_times2[x] == m_times[y]:
        dir_arr_proper2.append(dir_arr_proper[y])
        x += 1
        y = 0
        continue
    else:
        break
    break

print('\n{}'.format(dir_arr_proper2))

# Rename all files in the dir_arr_proper2 list with the new numerical value, 
# assign extensions, and print a new resulting list for user to see.

print('\n{}'.format(num))

ext = input('\nEnter Extension of All Files in Folder [Examples : .txt, .bat, .png] : ')
for n in range(len(dir_arr_proper2)):
    os.rename(path + '\\' + dir_arr_proper2[n], path + '\\' + num[n] + ext)
    output_arr.append(num[n] + ext)

print('\nFiles Renamed!\n\n{}'.format(output_arr), '\n')
