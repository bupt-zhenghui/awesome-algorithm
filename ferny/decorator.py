def decorator_function(original_function):
    def wrapper_function():
        print("装饰器函数开始")
        original_function()
        print("装饰器函数截止")
    return wrapper_function
# 注意装饰器函数要返回一个函数

# def original_function():
#     print("hello world")
#
# decorated_function = decorator_function(original_function)
# decorated_function()

# 或使用@语法糖
@decorator_function
def original_function():
    print("hello world")

original_function()