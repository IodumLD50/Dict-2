while True:
    key = input()
    if not key :
        print(f'Ответ: {data}')  
        break
    else:
      int(key)
      ch = int(key) ** int(key)
      data[key] = ch