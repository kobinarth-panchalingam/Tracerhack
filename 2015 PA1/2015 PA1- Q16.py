try:
    n = input()
    if not(2<=len(n)<=100):
        print('length of no.of digits is not in the allowed range')
    else:
        if int(n)%8 == 0:
            print('Yes')
        else:
            box = []
            for i in range(1,len(n)): 
                  for j in range(0,len(n)): 
                      if j+i <= len(n):
                          x = list(n)
                          del x[j:j+i]
                          x = int(''.join(x))
                          print(x)
                          if x%8 == 0 and x > 0:
                              box.append(x)
                      else:
                          break
                  if box:
                      print('Yes m=',max(box))
                      break
            else:
                print('No')
except TypeError:
    print('Invalid Input')
