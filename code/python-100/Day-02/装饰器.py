import functools


def makeBold(func):
    print("正在装饰makebold...")

    def wrapper():
        print('正在执行makebold')
        return "<b>" + func() + "</b>"

    return wrapper


def makeItalic(func):
    print("正在装饰makeItalic")

    def wrapper():
        print('正在执行makeItalic')
        return "<i>" + func() + "</i>"

    return wrapper


@makeBold
@makeItalic
def test():
    print('正在执行test')
    return "Facing the sea"


#
# ret = test()
# print(ret)

# functools.wraps 它也是一个装饰器,它能把原函数的一些属复制到包装函数中, 比如函数名,文档字符串 参数列表等
def make_bold(fn):
    @functools.wraps(fn)
    def wrapper():
        """wrapper function"""
        return "<i>" + fn() + "</i>"

    return wrapper


@make_bold
def say():
    """say something"""
    return "Hello"


print(say.__name__)  # say
print(say.__doc__)  # say something


# 装饰器参数
def make_tag(tag):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return f"<{tag}>{fn(*args, **kwargs)}</{tag}>"

        return wrapper

    return decorator


@make_tag('b')
@make_tag('i')
def say(content):
    return content


print(say('miclon'))

