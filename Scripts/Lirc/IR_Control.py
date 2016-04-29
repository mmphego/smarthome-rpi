import lirc as IR
"""
create file ~/.lircrc

begin
    prog = irexec
    button = KEY_1
    config = echo "You pressed one"
    repeat = 0
end
"""
IR.init('irexec')

while True:
    btn = IR.nextcode()
    if btn != []:
        print btn
