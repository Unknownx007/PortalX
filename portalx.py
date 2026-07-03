import os
import sys
import time
import random
from core.database import FsocietyDatabase
from core.servers import FsocietyNetworkDaemons

# MULTI-CHANNEL ANSI HIGH-REP COLOR MATRIX
C_RED     = "\033[31m"
C_GREEN   = "\033[32m"
C_YEL     = "\033[33m"
C_BLUE    = "\033[34m"
C_MAG     = "\033[35m"
C_CYAN    = "\033[36m"
C_WHITE   = "\033[37m"
C_BOLD    = "\033[1m"
C_RESET   = "\033[0m"

# Cyberpunk Neon Accents
NEON_GN   = "\033[92m"
NEON_YW   = "\033[93m"
NEON_BL   = "\033[94m"
NEON_MG   = "\033[95m"
NEON_CN   = "\033[96m"

# Cached Operational Configuration State Registry
g_interface = "wlan0"
g_ssid = "Free_Public_WiFi"
g_local_ip = "192.168.12.1"
g_mode = 1

def print_dedsec_cyber_banner():
    """Generates a high-density, multi-colored FSOCIETY system terminal layout."""
    os.system("clear")
    
    # 1. Output the Color-Mapped High-Fidelity Portal Transmitter Glyph
    print(f"{NEON_CN}{C_BOLD}        .---.                                                      .---.")
    print(f"       /  .  \\       {NEON_MG}[!] ALERT: BROADCAST listener ACTIVE {NEON_CN}        /  .  \\")
    print(f"      |\\_/|\\_/|                                                  |\\_/|\\_/|")
    print(f"      |   |   |         {C_WHITE}______     ______   _______  _______{NEON_CN}     |   |   |")
    print(f"   _  |   |   |  _     {C_RED}/  __  \\   /  ___/  /  _   / /  ____/{NEON_CN}  _  |   |   |  _")
    print(f"  | |_|   |   | | |   {C_RED}/  /_/  /  /  /__   /  /_/ / /  /___{NEON_CN}   | |_|   |   | | |")
    print(f"  |   |   |   | | |  {C_RED}/  ____ /  /  ___/  /  _   / /  ____/{NEON_CN}   |   |   |   | | |")
    print(f"  |   |___|___| | | {C_RED}/  /       /  /___  /  / | / /  /_____{NEON_CN}   |   |___|___| | |")
    print(f"  |             |  {C_RED}/__/       /______/ /__/  |/ /________/{NEON_CN}   |             |")
    print(f"   \\___________/                                              \\___________/")
    print(f"       |   |                 {NEON_YW}    UnknownX007     {NEON_CN}                |   |")
    print(f"       |   |               {C_WHITE}Ingestion & Gateway Core{NEON_CN}               |   |")
    
    # 2. Minimalist Authoritative System Brand Credits
    print(f"{C_RED}================================================================================")
    print(f"{C_WHITE}{C_BOLD}   [ ⚡ DEDSEC CENTRAL CONTROL ]    ::    [ OPERATOR IDENTITY: Unknownx007 ]")
    print(f"{C_RED}================================================================================" + C_RESET)

def print_dedsec_provocative_cow():
    """Generates an automated ASCII cowsay terminal block serving dynamic, cynical feedback alerts."""
    frustrated_lines = [
        "Wake up user... Your pathetic little network data belongs to DEDSEC now.",
        "You actually thought typing 'test1' would bypass our socket routing? Pathetic sh*t.",
        "Input real credentials next time or stop wasting my local thread cycles.",
        "Your wireless adapter is crying. Give it valid parameters, you absolute script monkey.",
        "Bypassing mobile security layers while you sit there clicking blank buttons..."
    ]
    selected_insult = random.choice(frustrated_lines)
    
    # Render the structured ASCII Cow communication box card
    print(f"\n{NEON_MG}  " + "_" * (len(selected_insult) + 2))
    print(f"  < {C_WHITE}{selected_insult}{NEON_MG} >")
    print(f"  " + "-" * (len(selected_insult) + 2))
    print(f"         \\   ^__^")
    print(f"          \\  {C_RED}()(){NEON_MG}_______")
    print(f"             (__)\\       )\\/\\")
    print(f"              U  ||----w |")
    print(f"                 ||     ||\n" + C_RESET)

def configure_rogue_network_parameters():
    global g_interface, g_ssid, g_local_ip, g_mode
    print_dedsec_cyber_banner()
    print(f"{NEON_CN}{C_BOLD}[⚙️ VECTOR SELECTION CONFIGURATIONS]{C_RESET}\n")
    
    # Colorized Input Prompt Strings
    val_int = input(f" {NEON_YW}[?] Target Wireless NIC Interface {C_WHITE}(wlan0/wlan1) {NEON_CN}[Current: {g_interface}]: {C_RESET}").strip()
    if val_int: g_interface = val_int

    if g_interface.lower() in ["virtual", "lo", "localhost"]:
        g_local_ip = "127.0.0.1"
    else:
        g_local_ip = "192.168.12.1"

    val_ssid = input(f" {NEON_YW}[?] Deceptive Broadcast SSID Identity {NEON_CN}[Current: {g_ssid}]: {C_RESET}").strip()
    if val_ssid: g_ssid = val_ssid

    print_dedsec_cyber_banner()
    print(f"{NEON_MG}{C_BOLD}[⚙️ PERSISTENCE SECURITY EVASION MODES]{C_RESET}\n")
    print(f"    {NEON_GN}[1]{C_WHITE} Standard Profile : Single Data Capture & Release Target to Internet Gateway")
    print(f"    {NEON_GN}[2]{C_WHITE} Aggressive Loop : Infinite Token Error Reprompt (Continuous Force-Feed)")
    print(f"\n{C_RED}================================================================================{C_RESET}")
    val_mode = input(f" {NEON_YW}[+] Choose Evasion Mode Index {NEON_CN}[Current: {g_mode}]: {C_RESET}").strip()
    g_mode = 2 if val_mode == "2" else 1

    print_dedsec_cyber_banner()
    print(f"{NEON_GN}[✅] System operational memory caches updated successfully.{C_RESET}")
    print(f"    {C_WHITE}├── NIC Interface Target : {NEON_CN}{g_interface}")
    print(f"    {C_WHITE}├── Air Broadcast SSID   : {NEON_CN}{g_ssid}")
    print(f"    {C_WHITE}├── Internal Gateway IP  : {NEON_CN}{g_local_ip}")
    print(f"    {C_WHITE}└── Client Loop Strategy : {NEON_CN}{'INFINITE AGGRESSIVE REPROMPT' if g_mode == 2 else 'SINGLE CAPTIVE RELEASE'}{C_RESET}\n")
    time.sleep(2.0)

def execute_master_portal_listener_post():
    print_dedsec_cyber_banner()
    print(f"{NEON_CN}{C_BOLD}[📁 WEAPONIZED TEMPLATE INGESTION MANAGER]{C_RESET}\n")
    print(f"    {NEON_GN}[1]{C_WHITE} Mount Core Profile : DedSec Standard Technical Validation Template")
    print(f"    {NEON_GN}[2]{C_WHITE} Mount Custom Clones : Inject Local Custom HTML File Path Architecture")
    print(f"\n{C_RED}================================================================================{C_RESET}")
    choice_idx = input(f" {NEON_YW}[+] Select Deployment Vector Index: {C_RESET}").strip()
    
    html_mode_setting = "dedsec"
    if choice_idx == "2":
        custom_path = input(f"\n {NEON_YW}[?] Enter Absolute Local Path to Custom HTML File: {C_RESET}").strip()
        if os.path.exists(custom_path):
            html_mode_setting = custom_path
            print(f" {NEON_GN}[✅] HTML target template structure verified. Ready to bind.{C_RESET}")
            time.sleep(1.0)
        else:
            print(f" {C_RED}[!] Error: File path target unresolvable. Falling back to DedSec standard layout.{C_RESET}")
            time.sleep(1.5)

    print_dedsec_cyber_banner()
    print(f"{NEON_YW}[*] Spawning Asynchronous Multi-Threaded Network Socket Core Listener...{C_RESET}")
    
    # Initialize background UDP / TCP socket daemons
    FsocietyNetworkDaemons.boot_asynchronous_listeners(g_interface, g_mode, html_mode_setting)
    
    # Initialize low-level system access point routing if not running virtual mode loopbacks
    if g_interface.lower() not in ["virtual", "lo", "localhost"]:
        FsocietyNetworkDaemons.activate_wireless_hotspot(g_interface, g_ssid, g_local_ip)
    
    print(f"\n{NEON_GN}[✅] UDP Socket DNS Poisoner Daemon running actively on Port 53.")
    print(f"{NEON_GN}[✅] TCP Socket HTTP Captive Portal Server running actively on Port 80.{C_RESET}")
    
    if g_interface.lower() in ["virtual", "lo", "localhost"]:
        print(f"\n{NEON_CN}[💡 VIRTUAL INTERNAL VALIDATION ACTIVE] Open local browser: http://127.0.0.1{C_RESET}")
    else:
        print(f"\n{NEON_YW}[📡 LIVE AP CELL TRANSMITTING] Connect target device to Wi-Fi SSID: {g_ssid}{C_RESET}")
        
    print(f"{C_WHITE}[*] Listening post deployed. Standing by... (Press Enter to drop execution loops and release card){C_RESET}")
    print(f"{NEON_CN}[💡 LIVE TELEMETRY LOG FLOW] Real-time harvested packets data will stream below natively:{C_RESET}")
    print(f"{C_RED}--------------------------------------------------------------------------------{C_RESET}")
    
    input() 
    FsocietyNetworkDaemons.deactivate_wireless_hotspot(g_interface)
    time.sleep(1.0)

def master_event_loop():
    os.makedirs("db", exist_ok=True)
    FsocietyDatabase.initialize_vault()
    while True:
        print_dedsec_cyber_banner()
        
        # 3. Inject the dynamic provocative ascii cowsay box into the heart of the selection interface
        print_dedsec_provocative_cow()
        
        print(f"{NEON_CN}{C_BOLD}[⚙️ CHOOSE FIELD OPERATION VECTOR INDEX]{C_RESET}\n")
        print(f"    {NEON_GN}[1]{C_WHITE} Configure Rogue Gateway Wireless AP Interface Parameters")
        print(f"    {NEON_GN}[2]{C_WHITE} Instantiate Active Captive Portal Web Listeners Post")
        print(f"    {NEON_GN}[3]{C_WHITE} Gracefully Terminate Framework Operations Loop")
        print(f"\n{C_RED}================================================================================{C_RESET}")
        choice = input(f"{NEON_YW}[+] Select Tactical Index: {C_RESET}").strip()
        
        if choice == "1":
            configure_rogue_network_parameters()
        elif choice == "2":
            execute_master_portal_listener_post()
        elif choice == "3":
            print(f"\n{C_RED}[!] Terminating tactical operational control loops safely.{C_RESET}\n")
            break

if __name__ == "__main__":
    try:
        master_event_loop()
    except KeyboardInterrupt:
        print(f"\n{C_RED}[!] Operation aborted by user command interception.{C_RESET}\n")

