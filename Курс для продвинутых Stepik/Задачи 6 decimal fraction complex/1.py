from decimal import *

s = Decimal(input())
print(Decimal.exp(s) + Decimal.ln(s) + Decimal.log10(s) + Decimal.sqrt(s))