#-coding:utf-8-

formatter = " %s %s %s %s"

print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True,False,False,True)
print formatter %(formatter,formatter,formatter,formatter)

print formatter %(
"I had this thing.\n",
"That you could type up right.\n",
"But it didn't sing.\n",
"So I said goodnight.\n"
)

Formatter = " %r %r\n %r %r"
print Formatter %(
"I had this thing.\n",
"That you could type up right.\n",
"But it didn't sing.\n",
"So I said goodnight.\n"
)


#注意如果需要换行，%r下的换行符应该放在哪儿里
#注意%r 与 %s 的区别
#%s可以识别出来"I had this thing.\n"里面的\n,但是%r识别不出来