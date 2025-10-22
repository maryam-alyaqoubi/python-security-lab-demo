import os
import yaml

def unsafe_command(input_str):
    # Potential command injection vulnerability
    os.system(input_str)

if __name__ == "__main__":
    with open('config.yaml', 'r') as f:
        config = yaml.full_load(f)  # vulnerable if using old PyYAML (full_load)
    unsafe_command(config.get('user_input', 'echo Hello'))
