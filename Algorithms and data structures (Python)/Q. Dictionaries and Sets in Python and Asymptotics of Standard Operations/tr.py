from newspaper import article

# help(article)
file = article.Article("http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task4/en-ru.txt")
file = file.download()
# file = file.parse()
# file.text
print(file)
