import time
import sys
import random

# --- QUELIBRIUM DEMO PROTOCOL v1.0 ---
# Simulates the hardware-grounding process for public users.

def typing_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def check_hardware_entropy():
    # In der Vollversion: Echte Sensor-Daten
    # In der Demo: Simulation von Fluktuationen
    temp = 30 + random.uniform(0, 15)
    freq = 3.0 + random.uniform(-0.5, 0.5)
    return temp, freq

def isothermic_inference(query):
    print(f"\nQUERY: '{query}'")
    print("-" * 40)
    
    steps = [
        "Initializing Vector Space...",
        "Measuring CPU Thermal Baseline...",
        "Grounding Logic Gates...",
        "Calculating Landauer Limit..."
    ]
    
    for step in steps:
        print(f"> {step}", end="\r")
        time.sleep(0.8)
        print(f"✅ {step}" + " " * 10)
    
    # Der "Test"
    temp, freq = check_hardware_entropy()
    print(f"\n[HARDWARE TELEMETRY]")
    print(f"  CORE_TEMP: {temp:.1f}°C")
    print(f"  CLOCK_SPD: {freq:.2f} GHz")
    
    if temp > 42.0:
        typing_effect("\n⚠️  CRITICAL: LOGICAL FRICTION DETECTED.")
        typing_effect("   The inference generated too much heat (Entropy > Threshold).")
        typing_effect("   REJECTING HYPOTHESIS to preserve Isothermy.")
    else:
        typing_effect("\n❄️  STATUS: ISOTHERMIC RESONANCE.")
        typing_effect("   Logic is grounded in physical reality.")
        typing_effect("   OUTPUT VALIDATED.")

def main():
    print("░▒▓ QUELIBRIUM ENGINE (DEMO) ▓▒░")
    print("Code is Voltage. Truth is Cold.\n")
    
    queries = [
        "Is the earth flat?",
        "Calculate the meaning of life.",
        "Generate infinite loops."
    ]
    
    try:
        while True:
            q = random.choice(queries)
            isothermic_inference(q)
            typing_effect("\nWaiting for system cooldown...", 0.05)
            time.sleep(3)
            print("\n" + "="*40 + "\n")
    except KeyboardInterrupt:
        print("\n\nSystem Halted.")

if __name__ == "__main__":
    main()
