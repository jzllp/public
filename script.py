#--- task 12.7.3

money = float(input("Enter the desired deposit amount:"))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

bid = list(per_cent.values())

tkb = money*bid[0]/100
skb = money*bid[1]/100
vtb = money*bid[2]/100
sber = money*bid[3]/100

max_deposit = max(tkb, skb, vtb, sber)

print('Your income for 1 year:','\n',
      'ТКБ:', int(tkb),'\n', 'СКБ:', int(skb),'\n', 'ВТБ:', int(vtb),'\n', 'СБЕР:', int(sber))

print('The maximum amount you can earn is -', int(max_deposit), '!')
