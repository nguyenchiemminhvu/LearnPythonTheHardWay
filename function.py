# God is with us

#----------------------------------------------------
# functions

def say_hello():
    print "Hello!";
    print "I'm with God!";

# like argv
def say_name(*args):
    arg1, arg2 = args;
    print arg1;
    print arg2;

def say_name_again(arg1, arg2):
    print arg1;
    print arg2;


#------------------------------------------------------
# main program

say_hello();
print "";
say_name("nguyen", "vu");
print "";
say_name_again("nguyen", "vu");
