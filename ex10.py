#-coding:utf8-
print "I am 6\\2\" tall."  #将字符串中的双引号转义
print "I am 6\2\" tall."  #\2被翻译成一个笑脸~~
print 'I am 6\'2 tall.'  #将字符串中的单引号转义

tabby_cat = "\tI'm tabbled in."
persian_cat = "I'm splite\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

###不管是单引号，双引号还是三引号，\都会对后面的字符进行转义，在前面再加一个\可以防止转义