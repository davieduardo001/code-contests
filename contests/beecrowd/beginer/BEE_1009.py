'''
JOAO
500.00
1230.30

print 684.54

---

MANGOJATA
1700.00
1230.50

TOTAL = R$ 1884.58
'''

seller_name = input()
salary = float(input())
total_sales = float(input())

TOTAL = salary + (total_sales * 15 / 100) # 15% of the total of sales

print(f'TOTAL = R$ {TOTAL:.2f}')