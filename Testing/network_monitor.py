import time

cmd ='/proc/net/dev'
while True:

    with open(cmd) as f:
        network_data = f.readlines()
    eth0_data = network_data[2].split()
    wlan0_data = network_data[3].split()
    import IPython;IPython.embed()
    eth0_rx = int(eth0_data[1])
    eth0_tx = int(eth0_data[-8])
    wlan0_rx = int(wlan0_data[1])
    wlan0_tx = int(wlan0_data[-8])

    if wlan0_rx:
        print 'wlan0_rx: ', wlan0_rx
        print 'wlan0_tx: ', wlan0_tx
    else:
        print 'eth0_rx: ', eth0_rx
        print 'eth0_tx: ', eth0_tx

    time.sleep(2)
