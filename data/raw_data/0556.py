"""
Задача №4

Доработаем класс Архив из задачи 2.

Добавьте методы представления экземпляра для программиста
и для пользователя.
"""


# 01:06:40


class Archive:
    """
    При первом запуске создаёт экземпляр класса, при повторном - добавляет
    в архив прежние данные.
    """
    instance = None
    counts = []
    texts = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            # cls.instance.counts = []
            # cls.instance.texts = []
        else:
            cls.instance.counts.append(cls.instance.count)
            cls.instance.texts.append(cls.instance.text)
        return cls.instance

    def __init__(self, count, text):
        self.count = count
        self.text = text
        # self.counts.append(self.count)
        # self.texts.append(self.text)

    def __str__(self):
        c = self.instance.counts if self.instance.counts else 'Empty'
        t = self.instance.texts if self.instance.texts else 'Empty'
        return (f'value: {self.instance.count}, text: {self.instance.text} '
                f'value archive: {c}, text archive: {t}')

    def __repr__(self):
        return f"Archive({self.instance.count}, '{self.instance.text}')"


if __name__ == '__main__':
    d1 = Archive(1, 'a')
    print(d1.text, d1.texts)
    print(f'{d1}')
    print(f'{d1 = }')
    d2 = Archive(2, 'b')
    print(d2.text, d2.texts)
    print(f'{d2}')
    print(f'{d2 = }')
"""
a []
value: 1, text: a value archive: Empty, text archive: Empty
d1 = self.instance.count = 1 self.instance.text = 'a' self.instance.counts = [] 
self.instance.texts = []
b ['a']
value: 2, text: b value archive: [1], text archive: ['a']
d2 = self.instance.count = 2 self.instance.text = 'b' self.instance.counts = [1]
self.instance.texts = ['a']
Process finished with exit code 0
"""
# 1:13:30, 1:17:50