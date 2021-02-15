import sys
import module_cmd
if len(sys.argv) < 2:
    print("Missing Args")
else:
    if len(sys.argv) == 2 and sys.argv[1] == 'api':
        print("run api")
        module_cmd.run_api()
    else:
        print("Hello World")
