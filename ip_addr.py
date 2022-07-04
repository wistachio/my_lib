import urllib.request

ip_checklist = ['https://api.ipify.org','https://ipinfo.io/ip','https://ifconfig.me/ip']

def get_ip():
    for ip_check in ip_checklist:
        try:
            return urllib.request.urlopen(ip_check).read().decode('utf8')
        except Exception as e:
            print(e)
