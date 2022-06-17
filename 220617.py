#지구에 달과 수성이 같이 공전한다면 어떻게 될지에 대해
#각각의 값을 변경하며 실험가능

#보통의 달과 지구사이의 거리 385000000
earth = sphere(pos=vec(0, 0, 0), radius=6400000, texture=textures.earth)
#pos=vec의 값을 조종하여 초기 위치설정 변경가능
#radius의 값을 변경하여 달과 수성의 지름 변경가능
moon = sphere(pos=vec(300000000, 0, 0), radius=1737100,
              texture=textures.rock, make_trail=True)
mercury = sphere(pos=vec(-400000000, 0, 0), radius=2439700,
              color = color.red, make_trail=True)

#크기확대
earth.radius = 6 * earth.radius
moon.radius = 6 * moon.radius
mercury.radius = 6 * mercury.radius

#질량의 크기를 조정하여 다른 결과를 도출가능
G = 6.673e-11
earth.m = 5.972e24
moon.m = 7.347e22
mercury.m = 3.285e23

#초기속도를 변경해 다른 결과 도출가능
earth.v = vec(200, 0, 0)
moon.v = vec(200, 1001, 0)
mercury.v = vec(200, -1200, 0)

#시간 배속비율 dt의 값을 늘리거나 줄여 속도변경
t = 0
dt = 1000

#대충 밑에있는건 물리
while True:
    rate(1000)

    r = moon.pos - earth.pos
    r2 = mercury.pos - earth.pos
    r3 = moon.pos - mercury.pos
    r4 = mercury.pos - moon.pos

    moon.f = -G * earth.m * moon.m/mag(r)**2*norm(r) +(-G * mercury.m * moon.m/mag(r3)**2*norm(r3))
    mercury.f = -G * earth.m * mercury.m/mag(r2)**2*norm(r2) +(-G * moon.m * mercury.m/mag(r4)**2*norm(r4))
    earth.f = -moon.f -mercury.f

    moon.v = moon.v + moon.f/moon.m * dt
    mercury.v = mercury.v + mercury.f/mercury.m * dt
    earth.v = earth.v + earth.f/earth.m * dt

    moon.pos = moon.pos + moon.v * dt
    mercury.pos = mercury.pos + mercury.v * dt
    earth.pos = earth.pos + earth.v * dt

    t = t + dt
