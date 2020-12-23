import platform
def where_am_i():
    '''Determines which device this script is running on'''
    current_machine = platform.machine()
    print('Platform processor:', platform.processor()) 
    print('Platform architecture:', platform.architecture())
    if current_machine == 'armv7l':
        print('probably pi3')
    elif current_machine == 'x86_64':
        print('probs workstation')
    elif current_machine == 'aarch64':
        if 'tegra' in platform.platform():
            print('definitely jetson')
        else:
            print('no idea')
    else:
        print('no idea')


def main():
    where_am_i()

if __name__ == "__main__":
    main()