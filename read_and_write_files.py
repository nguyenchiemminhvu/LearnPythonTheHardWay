# God is with us

from sys import argv;

script, file_name = argv;

print "clean content in file: ", file_name;

file = open(file_name, 'w');
file.truncate();

print "done";
print "";
print "write something to file";

line = raw_input("> ");

file.write(line);
file.write("\n");

file.close();
