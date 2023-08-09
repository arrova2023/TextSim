import subprocess

def run_script(script_name):
    subprocess.run(["python3.10", script_name])

def main():
    run_script("openInput.py")
    run_script("lematize.py")
    run_script("stopWords.py")
    run_script("matrix.py")
    run_script("id3.py")
    run_script("temperature.py")
    run_script("energyMin.py")

if __name__ == "__main__":
    main()
