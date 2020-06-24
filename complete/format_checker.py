
import os
import shlex
import subprocess

filename = "p47_algos_submission.py"
# Set folder or we will use current directory.
folder = None
if folder is None:
    folder = os.getcwd()

# Create full path to fil.
filepath = rf"{folder}\{filename}"

# Dictionary of formatting checkers and tests.
procs = dict(
    black_cmd = shlex.split(f'python -m black --line-length 88 --target-version py38 "{filepath}"'),
    # flake8_cmd = shlex.split(f'python -m flake8 --ignore=E203,W503  --max-line-length=88 --show-source "{filepath}"'),
    flake8_plus = shlex.split(f'python -m flake8 --ignore=E203,W503 --max-complexity=25 --max-line-length=88 --statistics --count "{filepath}"'),
    doctest_cmd = shlex.split(f'python -m doctest -v "{filepath}"'),
)

def format_newline(iterable):
    out = iterable
    try:
        iterable = iterable.decode("utf-8")
        out = str(iterable).replace("\r\n", os.linesep)
    except TypeError:
        pass
    return out


def print_output(*args):
    args_len = len(args)
    if args_len > 0:
        k = args[0]
        print(f"{k}\n")
        if len(args) == 3:
            outs, errs = args[1], args[2]
        else:
            outs = args[1]

        if outs:
            outs = format_newline(outs)
            print(f"{outs}\n")
        if errs:
            print(f"{str(errs)}\n\n")    


def run(**kwargs):
    output_dict = []
    for k, cmd in kwargs.items():
        proc = subprocess.Popen(args=cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        try:
            outs, errs = proc.communicate()
            print_output(k, outs, errs)
        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
            print_output(k, outs, errs)
    return output_dict


if __name__ == "__main__":
    results_dict = run(**procs)

    # for i in results_dict:
    #     for (key, out, err) in i:
    #         print(f"{key}: {out}: {err}")
    # print("\n".join([f"{i}" for i in results_dict]))
    