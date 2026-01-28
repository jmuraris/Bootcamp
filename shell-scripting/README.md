This repo contains shell scripting examples and tutorials for various use cases.

#!/bin/bash - shebang line to specify the system which interpreter to be used for execution.

bash -n test_script.sh  # Syntax Check

bash -x test_script.sh  # Debugging (shows each command before execution)

bash -v test_script.sh  # Verbose mode

chmod +x test_script.sh # Make script executable

./test_script.sh      # Execute the script

echo $? # Check exit status of the last command (0 for success, non-zero for failure) 
# Variables
NAME="World"
echo "Hello, $NAME!"
# Environment Variables
export MY_VAR="Hello"   # script can access this any where.

echo $MY_VAR

# Variables with default values
LOG_DIR="${LOG_DIR:-/var/log}" # If LOG_DIR is not set, use /var/log

# Command Line Arguments
Command Line Arguments make scripts more dynamic.

./script.sh Bob 25 India # shell assign them to special variables 

#0 =script name (./script.sh) $1=first argument (Bob), $2=second argument (25), $3=third argument (India), #$=number of arguments (3), $@=all arguments (Bob 25 India)