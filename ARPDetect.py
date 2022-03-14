import subprocess
import time
import winsound

while True:

    choice = input("Would you like to test[T/t] or initialize[I/i] ARPDetect? ")

    if choice == "T" or choice == "t":
        print("ALERT! ARP POISONING DETECTED!")
        winsound.PlaySound("jamil", winsound.SND_FILENAME)

    elif choice == "I" or choice == "i":

        while True:
            subprocess.call("arp -a 192.168.43.1")
            get_output = subprocess.getoutput("arp -a 192.168.43.1")
            output_log = open("Logs.txt", "w")
            output_log.write(get_output)
            output_log.close()
            log = open("Logs.txt", "r")
            if log.mode == "r":
                contents = log.read()
                if "F0-D5-BF-DE-37-07" in contents:
                    print("ARP POISONING: FALSE")
                elif "F0-D5-BF-DE-37-07" != contents:
                    print("ARP POISONING DETECTED!")
                    winsound.PlaySound("jamil", winsound.SND_FILENAME)
                    break
            time.sleep(10)
