def replace_words(s, words):
    for k, v in words.items():
        s = s.replace(k, v)
    return s

s = 'hello world'
dictionary = {"hello": "foo", "world": "bar"}

print(replace_words(s, dictionary))