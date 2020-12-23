import platform
import re
import subprocess
def where_am_i():
    '''Determines which device this script is running on'''
    current_machine = platform.machine()
    #try:
    os_system_info_out = subprocess.Popen("cat /etc/os-release", shell=True, stdout=subprocess.PIPE)
    os_system_info_return = str(os_system_info_out.stdout.read())
    x1= re.search('NAME=', os_system_info_return)
    start_index_os = x1.end()
    x2= re.search('VERSION=', os_system_info_return)
    end_index_os = x2.start()
    os_system = os_system_info_return[start_index_os:end_index_os]
    print(re.sub(r'\n', '', os_system))
    #except:
        #print("there is no file such as: /etc/os-release")    

    if current_machine == 'armv7l':
        print('probably pi3')
       
        subprocess_out = subprocess.Popen("cat /proc/cpuinfo", shell=True, stdout=subprocess.PIPE)
        subprocess_return = str(subprocess_out.stdout.read())
        #print(str(subprocess_return))
        if 'Raspberry Pi 4' in subprocess_return:
            print("this is raspberry pi 4 ")
        if 'Raspberry Pi 3' in subprocess_return:  
            print("this is raspberry pi 3 ")  
    elif current_machine == 'x86_64':
        print('probs workstation')
    elif current_machine == 'aarch64':
        if 'tegra' in platform.platform():
            print('definitely jetson')
            #sudo apt-get install lshw
            subprocess_out = subprocess.Popen("cat /proc/device-tree/nvidia,dtsfilename", shell=True, stdout=subprocess.PIPE)
            subprocess_return = str(subprocess_out.stdout.read())
            list_of_machine_ids =[3668 ,3448,2888,3310,3489,2180] 
            list_of_machine_names = ["NVIDIA Jetson Xavier NX", "NVIDIA Jetson Nano","NVIDIA Jetson AGX Xavier series","original NVIDIA Jetson TX2","NVIDIA Jetson™ TX2i and Jetson TX2 4GB","Jetson TX1"]
            found = False
            for i in range(len(list_of_machine_ids)):
                if str(list_of_machine_ids[i]) in subprocess_return:
                    print(list_of_machine_names[i])
                    found = True
            if found == False:
                print("unknown jetson")     

        else:
            print('no idea')
    else:
        print('no idea')


def main():
    where_am_i()

if __name__ == "__main__":
    main()
