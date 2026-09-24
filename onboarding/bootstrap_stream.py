"""
Atomic Stream — Governance Bootstrap

Interviews the accountable humans and writes the Stream's stream.yml.

Run from anywhere:
    python onboarding/bootstrap_stream.py

Reads:  onboarding/interview_config.json
Writes: stream.yml  (repository root)
"""

import json
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit(
        "Error: PyYAML is not installed.\n"
        "Install it with:  pip install -r onboarding/requirements.txt"
    )

# Paths resolve against this file, not the working directory, so the script
# runs correctly from the repository root or from inside onboarding/.
HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)

CONFIG_FILE = os.path.join(HERE, 'interview_config.json')
OUTPUT_FILE = os.path.join(REPO_ROOT, 'stream.yml')


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


def confirm_overwrite(path):
    """stream.yml is committed and read by agents at runtime. Never replace it silently."""
    if not os.path.exists(path):
        return True
    print(f"\n{os.path.relpath(path, REPO_ROOT)} already exists.")
    print("Continuing will replace this Stream's live configuration.")
    return input("Type 'replace' to continue, anything else to abort: ").strip() == 'replace'


def run_interview():
    print("==================================================")
    print("   ATOMIC STREAM: GOVERNANCE BOOTSTRAP")
    print("==================================================")

    if not os.path.exists(CONFIG_FILE):
        sys.exit(f"Error: Could not find {CONFIG_FILE}.")

    try:
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
    except json.JSONDecodeError as e:
        sys.exit(f"Error: {os.path.basename(CONFIG_FILE)} is not valid JSON — {e}")

    if not confirm_overwrite(OUTPUT_FILE):
        sys.exit("Aborted. Nothing was written.")

    stream_data = {}

    for role, details in config.get('roles', {}).items():
        print(f"\n\n--- {role.upper()} ---")
        print(f"Role Context: {details.get('description', '')}")
        input("Press Enter when this person is ready...")

        for q in details.get('questions', []):
            print(f"\n> {q['prompt']}")
            print(f"  Help: {q['help_text']}")

            if q['type'] == 'text_block':
                answer = get_multiline_input("Enter your response:")
            elif q['type'] == 'list':
                entered = input("Enter your response: ")
                # Split on commas and strip whitespace.
                answer = [item.strip() for item in entered.split(',') if item.strip()]
            else:
                answer = input("Enter your response: ").strip()

            stream_data[q['key']] = answer

    print("\n==================================================")
    print("   INTERVIEW COMPLETE. GENERATING CONFIGURATION...")
    print("==================================================")

    with open(OUTPUT_FILE, 'w') as yaml_file:
        yaml.dump(stream_data, yaml_file, default_flow_style=False, sort_keys=False)

    print(f"Success! The foundational variables have been written to {OUTPUT_FILE}.")
    print("\nReview it, then commit it to main. Agents read it from there.")
    print("Credentials do not belong in this file — see foundations/access/.")


if __name__ == "__main__":
    run_interview()
