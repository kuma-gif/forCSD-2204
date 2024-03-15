''' referend : https://www.youtube.com/watch?v=aJQWanFCukM '''
''' ตรวจสอบอัตราแลกเปลี่ยนเงินตราแบบ Real-time'''

# ดึงอัตรา Dollar USA
from forex_python.converter import CurrencyRates
c = CurrencyRates()
# ระบุอัตราสกุลเงินว่าจะดูของประเทศอะไร เช่น USD = Dollar
result = c.get_rates('USD')
print(result)