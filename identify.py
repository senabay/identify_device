import platform
import re
import subprocess
def where_am_i():
    '''Determines which device this script is running on'''
    current_machine = platform.machine()
    try:
        os_system_info_out = subprocess.Popen("cat /etc/os-release", shell=True, stdout=subprocess.PIPE)
        os_system_info_return = str(os_system_info_out.stdout.read())
        #print(os_system_info_return)
        x1= re.search('PRETTY_NAME=', os_system_info_return)
        start_index_os = x1.start()
        x2= re.search('VERSION_ID=', os_system_info_return)
        end_index_os = x2.start()
        os_system = os_system_info_return[start_index_os:end_index_os-2]
        print(os_system.rstrip("\n"))
    except:
        print("there is no file such as: /etc/os-release")    

    if current_machine == 'armv7l':
        print('probably pi3')       
        subprocess_out = subprocess.Popen("cat /proc/cpuinfo", shell=True, stdout=subprocess.PIPE)
        subprocess_return = str(subprocess_out.stdout.read())
        if 'Raspberry Pi 4' in subprocess_return:
            print("this is raspberry pi 4 ")
        if 'Raspberry Pi 3' in subprocess_return:  
            print("this is raspberry pi 3 ")  
    elif current_machine == 'x86_64':
        print('probs workstation')
    elif current_machine == 'aarch64':
        if 'tegra' in platform.platform():
            print('definitely jetson')            
            list_of_machine_ids =[2180,3310,3489,2888,3448,3668] 
            list_of_machine_names = ["Jetson TX1", "NVIDIA Jetson TX2","NVIDIA Jetson TX2i and Jetson TX2 4GB","NVIDIA Jetson AGX Xavier"," NVIDIA Jetson Nano","Jetson Xavier NX"]
            
            def check_in_it(subprocess_that_made):
                machine_is = None
                for i in range(len(list_of_machine_ids)):
                    if str(list_of_machine_ids[i]) in subprocess_that_made:                    
                        machine_is = list_of_machine_names[i]
                        #print(machine_is)
                return machine_is
            
            machine_is = None            
            
            if machine_is == None:
                
                subprocess_out = subprocess.Popen("cat /proc/device-tree/nvidia,boardids", shell=True, stdout=subprocess.PIPE,stderr = subprocess.PIPE)
                subprocess_return1 = str(subprocess_out.stdout)
                machine_is = check_in_it(subprocess_return1)
            
            if machine_is == None:
               
                subprocess_out = subprocess.Popen("cat /proc/device-tree/compatible", shell=True, stdout=subprocess.PIPE,stderr = subprocess.PIPE)
                subprocess_return1 = str(subprocess_out.stdout)
                machine_is = check_in_it(subprocess_return1)
                        
            if machine_is == None:
            
                subprocess_out = subprocess.Popen("cat /proc/device-tree/nvidia,dtsfilename", shell=True, stdout=subprocess.PIPE,stderr = subprocess.PIPE)
                subprocess_return1 = str(subprocess_out.stdout)
                machine_is = check_in_it(subprocess_return1)            
            
            if machine_is == None:
                print("unknown jetson")     
            else:
                print(machine_is)

        else:
            print('no idea')
    else:
        print('no idea')



def main():
    where_am_i()

if __name__ == "__main__":
    main()
