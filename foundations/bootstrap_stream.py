import json
import yaml
import os

CONFIG_FILE = 'scripts/interview_config.json'
OUTPUT_FILE = 'stream.yml'

def get_multiline_input(prompt_text):
    print(f"\n{prompt_text}")
    print("(Press Enter twice to finish your input)")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def run_interview():
    print("==================================================")
    print("   ATOMIC STREAM: GOVERNANCE BOOTSTRAP")
    print("==================================================")
    
    if not os.path.exists(CONFIG_FILE):
        print(f"Error: Could not find {CONFIG_FILE}.")
        return

    with open(CONFIG_FILE, 'r') as file:
        config = json.load(file)

    stream_data = {}

    for role, details in config.get('roles', {}).items():
        print(f"\n\n--- {role.upper()} ---")
        print(f"Role Context: {details.get('description', '')}")
        input("Press Enter when this person is ready...")

        for q in details.get('questions', []):
            print(f"\n> {q['prompt']}")
            print(f"  Help: {q['help_text']}")
            
            answer = None
            if q['type'] == 'text_block':
                answer = get_multiline_input("Enter your response:")
            elif q['type'] == 'list':
                raw_input = input("Enter your response: ")
                # Clean up the list by splitting on commas and stripping whitespace
                answer = [item.strip() for item in raw_input.split(',') if item.strip()]
            else:
                answer = input("Enter your response: ").strip()

            stream_data[q['key']] = answer

    print("\n==================================================")
    print("   INTERVIEW COMPLETE. GENERATING CONFIGURATION...")
    print("==================================================")

    # Write the collected data to stream.yml
    with open(OUTPUT_FILE, 'w') as yaml_file:
        yaml.dump(stream_data, yaml_file, default_flow_style=False, sort_keys=False)
    
    print(f"Success! The foundational variables have been written to {OUTPUT_FILE}.")

if __name__ == "__main__":
    run_interview()
