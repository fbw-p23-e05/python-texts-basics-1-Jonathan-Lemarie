
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

word_in_text = 'capital'


if word_in_text in text:
    index = text.index(word_in_text)

print(f'{word_in_text}: {index}')