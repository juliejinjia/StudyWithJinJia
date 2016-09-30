#-coding:utf-8-
x = "There are %d types of people." % 10   #可以后面直接加数值
z = "There are %s types of people." % 'ten'  #可以直接跟字符串，字符串一定要加上引号
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who  %s." %(binary,do_not)  #字符串包含字符串

print x
print z
print y

print "I said:%r." %x   
print "I also said:'%s'. " %y   

hilarious = False 
joke_evaluation = "Isn't that joke so funny?!%r"  #字符串包含字符串

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w+e