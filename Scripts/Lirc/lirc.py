import lirc
"""
begin
    prog = irexec
    button = KEY_1
    config = echo "You pressed one"
    repeat = 0
end
"""
lirc.init('irexec')

while True:
    btn = lirc.nextcode()
    if btn != []:
        print btn
