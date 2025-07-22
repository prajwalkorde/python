a=int(input('enter a number.'))
b=int(input('enter a number.'))
try: 
    print(a/b)
except Exception as e:
    print("infinite")
else:
    print('thank you.')