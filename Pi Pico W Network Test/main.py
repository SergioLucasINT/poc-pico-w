import network
import time
from machine import Pin, PWM
import usocket as socket

pinR = PWM(Pin(21))
pinG = PWM(Pin(20))
pinB = PWM(Pin(19))

def set_rgb_color(r, g, b):
    pinR.duty_u16(r)
    pinG.duty_u16(g)
    pinB.duty_u16(b)

print("Conectando ao WiFi", end="")
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Wokwi-GUEST", "")

while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.1)

print(" Sucesso!")
print(wlan.ifconfig())

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    
    # Enquanto o request está sendo executado, luz amarela acende
    set_rgb_color(65025, 65025, 0)
    
    print("Fazendo requisição para: " + url)

    response = s.recv(4096)
    s.close()
    
    status = response.split(b'\r\n')[0].decode('utf-8')
    
    if "HTTP/1.1 200 OK" in status or "HTTP/1.0 200 OK" in status:
        # Luz verde para sucesso
        set_rgb_color(0, 65025, 0)
    else:
        # Luz vermelha para falha
        set_rgb_color(65025, 0, 0)
    
    return status

response_status = http_get("http://www.google.com/")
print("HTTP Response Status:", response_status)

