nu = [111.118,106.357,108.08,53.94,113.42,164.71,139.543,111.682,]

w = [37.789,62.218,41.579,20.207,79.216,94.507,80.447,112.020,]

v = [112.46,141.880,132.370,69.560,163.72,192.510,171.150,170.430,]


def P0_1_teor():
    for i in range(len(nu)):
        print(1-nu[i]*(v[i]-w[i]),nu[i],w[i],v[i])


print(P0_1_teor())