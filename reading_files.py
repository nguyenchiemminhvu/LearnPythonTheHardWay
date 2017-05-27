# God is with us

from sys import argv;

script, file_name = argv;

file = open(file_name);

print "File name: ", file_name;
print "__Content__";
print file.read();
