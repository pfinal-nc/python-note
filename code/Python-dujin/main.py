from reader.reader import get_text
from reader.reader import get_radio


if __name__ == '__main__':
    text_list = get_text()
    text_str = ','.join(text_list)
    get_radio(text_str, 1)
