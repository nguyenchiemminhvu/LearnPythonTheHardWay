# God is with us

def read_file(f):
    print f.read();

def rewind(f):
    f.seek(0);

def print_a_line(f):
    print f.readline();

#---------------------------------------------------------

file = open("text.txt", "w");
file.write("""
    Nguyen Chiem Minh Vu
    12/04/2017
    Da Nang city
    Trung Lap Church
    JOY
""");
file.close();

file = open("text.txt", "r");
read_file(file);
rewind(file);
print "";
print_a_line(file);
file.close();
