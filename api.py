from flask import Flask, request
from multiprocessing import Process

from rainbow_wave import rainbow_wave_effect
from increase import increase_effect
from weird_shit import weird_shit_effect
from fill import fill_effect

app = Flask(__name__)

effect_process = None


def run_effect(effect, *args):
    global effect_process

    if effect_process:
        effect_process.terminate()

    effect_process = Process(target=effect, args=args, daemon=True)

@app.post("/rainbow-wave")
def rainbow_wave():
    run_effect(rainbow_wave_effect)

    return "Set successfully", 200


@app.post("/weird-shit")
def weird_shit():
    run_effect(weird_shit_effect)

    return "Set successfully", 200


@app.post("/increase")
def increase():
    run_effect(increase_effect)

    return "Set successfully", 200


@app.post("/fill/")
def fill():
    r = int(request.args.get("R"))
    g = int(request.args.get("G"))
    b = int(request.args.get("B"))

    run_effect(fill_effect, r, g, b)

    return "Set successfully", 200


if __name__ == "__main__":
    app.run("0.0.0.0", port=3002)
