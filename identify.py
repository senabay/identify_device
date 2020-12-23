import platform
import subprocess
def where_am_i():
    '''Determines which device this script is running on'''
    current_machine = platform.machine()
    print('Platform processor:', platform.processor()) 
    print('Platform architecture:', platform.architecture())
    print('Python SCM:', platform.python_compiler()) 
    

    #list_files = subprocess.run(["ls", "-l"])
    #print("The exit code was: " ,list_files)


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
            subprocess_out = subprocess.Popen("cat /proc/cpuinfo", shell=True, stdout=subprocess.PIPE)
            subprocess_return = str(subprocess_out.stdout.read())
            #print(subprocess_return)
            if 'ARMv8 Processor rev 0' in subprocess_return: 
                print("this is jetson nx")
            if 'ARMv8 Processor rev 3' in subprocess_return: 
                print("this is jetson tx")  
        else:
            print('no idea')
    else:
        print('no idea')


def main():
    where_am_i()

if __name__ == "__main__":
    main()