#coding:utf-8
#打印
#定义变量
formatter = "%r %r %r %r"

print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True, False, False, True)
#formatter作为参数传入
print formatter %(formatter, formatter, formatter, formatter)
#参数为string
print formatter %(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)