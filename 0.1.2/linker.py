import subprocess
import sys

def run_script(script_name):
    try:
        subprocess.run(["python3.10", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py [link_corpus (y/n)] [generate_local_minimum (y/n)]")
        sys.exit(1)

    link_corpus_arg = sys.argv[1].strip().lower()
    generate_local_minimum_arg = sys.argv[2].strip().lower()

    if link_corpus_arg == 'y':
        run_script("unifiedCorpus.py")
        run_script("unifiedIterator.py")

    if generate_local_minimum_arg == 'y':
        run_script("refinement.py")
