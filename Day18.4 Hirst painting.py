import colorgram

colors = colorgram.extract("hirst_painting.jpeg", 66)
rgb_list = []
for rgb_color in range(0, 31):
    fir = colors[rgb_color]
    rgb = fir.rgb
    rgb_list.append((rgb.r, rgb.g, rgb.b))

print(rgb_list)
