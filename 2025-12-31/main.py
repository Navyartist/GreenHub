import datetime

# _2025_1_1_0_0_am = 1735657200
# result = _2025_1_1_0_0_am / 365.24 / 24 / 60 / 60
# year = 2025-1970
# print(result, year)
# # 결과값: 55.0373287671233 55

# r= 31556926 # 1 year
# res = r*55
# print(res)
# w = _2025_1_1_0_0_am - res
# print(w)

now = datetime.datetime.now()
timestamp = now.timestamp()
print(now)
print(timestamp)