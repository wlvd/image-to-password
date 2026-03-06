from PIL import Image
import numpy as np

def medie_coloana(px, x):
    return px[:, x, :].mean(axis=0)

def medie_rand(px, y):
    return px[y, :, :].mean(axis=0)

def scale(v):
    m = float(np.max(v))
    if m == 0:
        return np.array([0.0, 0.0, 0.0])
    return v / m

path=input("Drag&Drop your image:\n").strip()
path = path.strip('"').strip("'")
img = Image.open(path).convert("RGB")
w,h = img.size
px=np.array(img)

offset = medie_rand(px, h-1)
print(offset)
weight=scale(medie_rand(px, h-2))
print(weight)


pixel_array = []
for x in range(w):
    pixel = medie_coloana(px, x) + offset
    pixel_array.append((pixel*weight).sum())

print(pixel_array)
pixel_array=np.array(pixel_array)

print("\n\n\nA-Z: ")
for x in pixel_array:
    print(chr(int(x%26+97)), end="")

print("\n\nA-Z + a-z + !-/ + 0-9: ")
for x in pixel_array:
    print(chr(int(x%94+33)), end="")

print("\n")