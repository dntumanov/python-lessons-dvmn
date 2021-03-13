from transliterate import translit
from num2words import num2words

import text

TRANSLIT_RU = 'ru'
numbers_from_text = [78, 15, 3, 40, 8]

print(translit(text.data, TRANSLIT_RU))

for number in numbers_from_text:
    print(number, '-', translit(num2words(number), TRANSLIT_RU))
