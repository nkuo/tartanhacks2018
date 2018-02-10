top = 49.3457868 # north lat
left = -124.7844079 # west long
right = -66.9513812 # east long
bottom =  24.7433195 # south lat

#30 km, 1 degree is 111 km, assume 30km -> 20km
h = (top-bottom) * (111/20)
w = (right-left) * (111/20)

result = list()
lat = bottom
for i in range(int(h)):
    lon = left
    for j in range(int(w)):
        result.append((lat,lon))
        lon += 20/111
    lat += 20/111