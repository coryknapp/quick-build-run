import sys
import os
import subprocess as sub

class color:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

def launch_command( command ):
    """executes arg as it would in the commandline, prints output and returns

    :command: string to execute

    """
    print color.OKBLUE + command + color.ENDC
    comp = sub.Popen( command.split(), stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = comp.communicate()
    print output[:-1] #cut the \n at the end

commands = []

if len( sys.argv ) == 2:
    fh = open( sys.argv[1] )
elif os.path.isfile( 'test.cpp' ):
    fh = open( 'test.cpp' )
elif os.path.isfile( 'main.cpp' ):
    fh = open( 'main.cpp' )
else:
    print 'no file found to qbr.'
    sys.exit();

for line in fh.readlines():
    if line[0:2] == '//':
        if line[2:6] == 'qbr ':
            commands.append( line[6:-1] )
    else:
        # we're done collecting commands so execute them and then quit
        for line in commands:
            launch_command( line )
        sys.exit()
