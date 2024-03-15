import subprocess
import shlex

def execute_command(command):
    try:
        args = shlex.split(command)
        if '<' in args:
            input_file_index = args.index('<')
            input_file = args[input_file_index + 1]
            args = args[:input_file_index]
            with open(input_file, 'r') as f:
                return subprocess.run(args, stdin=f, text=True, capture_output=True)
        elif '>' in args:
            output_file_index = args.index('>')
            output_file = args[output_file_index + 1]
            args = args[:output_file_index]
            with open(output_file, 'w') as f:
                return subprocess.run(args, stdout=f, text=True, capture_output=True)
        else:
            return subprocess.run(args, text=True, capture_output=True)
    except Exception as e:
        return str(e)

def main():
    while True:
        user_input = input('$ ')
        if user_input.lower() == 'exit':
            break
        result = execute_command(user_input)
        print(result.stdout)
        if result.stderr:
            print("Error:", result.stderr)

if __name__ == "__main__":
    main()
