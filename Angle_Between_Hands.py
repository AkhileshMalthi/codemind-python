time = input()
h,m = map(int,time.split(":"))
h_angle = (h*60 + m)*0.5
m_angle = m*6
angle = abs(h_angle - m_angle)
print(min(360 - angle,angle))
