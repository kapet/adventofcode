import collections

data = [line.strip() for line in open('2021/03/input.txt')]

oxy_data = data[:]
for idx in range(len(data[0])):
    freq = collections.Counter((val[idx] for val in oxy_data))
    keep = (freq['1'] >= freq['0']) and '1' or '0'
    oxy_data = [val for val in oxy_data if val[idx] == keep]
    if len(oxy_data) <= 1:
        break
print(oxy_data)

co2_data = data[:]
for idx in range(len(data[0])):
    freq = collections.Counter((val[idx] for val in co2_data))
    keep = (freq['1'] < freq['0']) and '1' or '0'
    co2_data = [val for val in co2_data if val[idx] == keep]
    if len(co2_data) <= 1:
        break
print(co2_data)

oxy = int(oxy_data[0], 2)
co2 = int(co2_data[0], 2)
print(oxy, co2, oxy*co2)