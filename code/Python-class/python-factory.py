# -*- coding:utf-8 -*-
# 工厂模式属于创建模式列表类别。它提供了创建对象的最佳方法。 在工厂模式中，创建对象时不会将逻辑公开给客户端，并使用通用接口引用新创建的对象。工厂模式使用工厂方法在Python中实现。 当用户调用一个方法时，传入一个字符串，并通过工厂方法实现创建一个新对象，并将此对象作为返回值。 工厂方法中使用的对象类型由通过方法传递的字符串确定。在下面的例子中，每个方法都包含对象作为参数，这是通过工厂方法实现的。
class Button(object):
    html = ''
    def get_html(self):
        return self.html

class Image(Button):
    html = '<img></img>'

class Input(Button):
    html = '<input />'

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():
    def created_button(self,typ):
        targetclass= typ.capitalize()
        return globals()[targetclass]()

button_obj = ButtonFactory()

button = ['image','input','flash']

for b in button:
    print(button_obj.created_button(b).get_html())