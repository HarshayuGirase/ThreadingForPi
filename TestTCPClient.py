import socket
import numpy as np
from cStringIO import StringIO
import cv2
import time

def startClient(server_address,image):
    start_time = time.clock()
    if not isinstance(image,np.ndarray):
        print 'not a valid numpy image' 
        return
    client_socket=socket.socket()
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #so it can be recreated
    port=7562
    try:
        client_socket.connect((server_address, port))
        print 'Connected to %s on port %s' % (server_address, port)
    except socket.error,e:
        print 'Connection to %s on port %s failed: %s' % (server_address, port, e)
        return

    f = StringIO()
    np.savez_compressed(f,frame=image)
    f.seek(0)
    out = f.read()
    print len(out)
    client_socket.sendall(out)
    client_socket.shutdown(1)
    client_socket.close()
    print 'image sent'

    print(time.clock() - start_time)
    

depthMat = cv2.imread('./Boiler3.png', cv2.IMREAD_UNCHANGED)
startClient('192.168.1.6', depthMat)