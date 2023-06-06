# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

with open(r'C:\autotests_course\Homework9\test_file\task1_data.txt', mode='r', encoding='utf-8') as f1, \
     open(r'C:\autotests_course\Homework9\test_file\task1_answer.txt', mode='w', encoding='utf-8') as f2:
    f2.write(''.join(i for i in f1.read() if i not in '1234567890'))

f1.close()
f2.close()
