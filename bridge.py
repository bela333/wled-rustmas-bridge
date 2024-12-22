import socket
import struct

SERVE_PORT = 7283
WLED_ADDRESS = "wled.local"
WLED_PORT = 21324



MODE_WARLS = 1
MODE_DRGB  = 2
MODE_DRGBW = 3
MODE_DNRGB = 4

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", SERVE_PORT))

while True:
    packet = server.recv(2000)
    length = int.from_bytes(packet[:2], 'little')
    rest = packet[2:]
    assert len(rest) == length
    resp = struct.pack("BB", MODE_DRGB, 240) # 240: wait 4 minutes before returning to normal mode
    resp += rest
    server.sendto(resp, (WLED_ADDRESS, WLED_PORT))