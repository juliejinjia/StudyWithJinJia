#-coding:utf-8-

my_name = 'Zed A. shaw'
my_age = 35
my_height = 74
my_weight = 108
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print "Let's talk about %s." %my_name

print "He's %d inches tall." %my_height

print "Actually that's not too heavy."

print "He's got %s eyes and %s hair." %(my_eyes,my_hair)

print "His teeth are usually %s depending on the coffee." %my_teeth

#this line is tricky, try to get it exactly right

print "If I add %d,%d,and %d I get %d." %(my_age,my_height,my_weight,my_age+my_weight+my_height)
print "\n"  ##换行，与上面的区分开来
print "#############################################"
print "test the difference between %s and %r. "  %(my_teeth,my_hair)
print "test the difference between %s and %r. " 
string = "Hello\tWILL\n"

print "%s" %string
print "%r" %string