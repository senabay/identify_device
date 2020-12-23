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
        subprocess_return = subprocess_out.stdout.read()
        print(subprocess_return)
    elif current_machine == 'x86_64':
        print('probs workstation')
    elif current_machine == 'aarch64':
        if 'tegra' in platform.platform():
            print('definitely jetson')
            #sudo apt-get install lshw
            subprocess_out = subprocess.Popen("cat /proc/cpuinfo", shell=True, stdout=subprocess.PIPE)
            subprocess_return = subprocess_out.stdout.read()
            print(subprocess_return)
        else:
            print('no idea')
    else:
        print('no idea')


def main():
    where_am_i()

if __name__ == "__main__":
    main()