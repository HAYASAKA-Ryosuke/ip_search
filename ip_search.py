#!coding:utf-8

from multiprocessing import Pool
import subprocess


class Ping(object):
    def __init__(self, hosts, pool_num=5):
        self.hosts = hosts
        self.pool_num = pool_num

    def _shell(self, host):
        popen = subprocess.Popen(["ping", "-c", "1", "-W", "0", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = popen.communicate()
        if not ("1 packets transmitted, 0 packets received, 100.0% packet loss" in str(out[0])):
            print(host)
            return host

    def send(self):
        p = Pool(self.pool_num)
        return p.map(self._shell, self.hosts)

if __name__ == '__main__':
    hosts = ['192.168.' + str(num1) + '.' + str(num2) for num1 in range(255) for num2 in range(255)]
    ping = Ping(hosts)
    ping.send()
