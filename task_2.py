'''Задание №2

С помощью цикла создайте словарь, в котором ключи будут, например от числа 10, до -5 (включительно). 
А значениями этих ключей будут сами эти числа возведённые в степени равных этим числам

Например:

my_dict = {
  10: 10000000000,
  9: 387420489,
  # и так далее ...
  -5: -0.00032
}'''

data = dict()
print('Если хотите посмотреть данные => Enter')

print('Введите ключи: ')

while True:
    key = input()
    if not key :
        print(f'Ответ: {data}')  
        
        while True:
          k = input('Введите клюк значение которого хотите увидеть: ')
          try:
              print(f'Значение {k}: {data[k]}')
          except:
              print(f'Kлюч {k} ещё не записан!')
              yn = input('Хотите записать? Y/N: ')
              if (yn == 'Y') or (yn == 'y'):
                int(k)
                ch = int(k) ** int(k)
                data[k] = ch 
              elif not k:
                 ex = input('Для выхода нажмите Y/N или Enter для просмотра базы данных: ')
                 if (ex == 'Y') or (ex == 'y'):
                    exit()
                 break
    else:
      int(key)
      ch = int(key) ** int(key)
      data[key] = ch
    
    
#print(data)
    