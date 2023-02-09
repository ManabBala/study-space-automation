from pyvda import AppView, VirtualDesktop, get_virtual_desktops


def all_virtual_desktop():
    for vd in get_virtual_desktops():
        print(vd.name)


def get_vd_by_name(name):
    for vd in get_virtual_desktops():
        if vd.name == name:
            return vd


def get_vd_by_number(number):
    return VirtualDesktop(number)