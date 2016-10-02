#-coding:utf8-
print "How old are you?"

age = input()
#输入3+2，输出5
print "How tall are you?"

height = raw_input()
#输入6'2",输出'6\'2"'，其中输入的单引号前面有一个转义字符，防止与前面的单引号混淆
print "How much you weight?"

weight = raw_input()

print "So ,you are %d old, %r tall and %r heavy." %(age,height,weight)

#根据网上的了解，raw_input返回的是字符串类型，string类型；input返回的是数值类型。
#input会计算字符串中的表达式，raw_input不会
#