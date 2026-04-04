# Given a string s representing time in 24-hour format "HH:MM", compute the smallest angle in degrees between the hour and minute hands of an analog clock.

s = "06:00"
H, M = (int(i) for i in s.split(":"))
H = H % 12 if H > 12 else H
angle = abs(H * 30 - M * 5.5)
print(min(angle, abs(360 - angle)))

