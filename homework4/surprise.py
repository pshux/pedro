# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def print_star_names(data):

    for star in data:

        print(f"Target: {star}")

def print_spectral_types(data):

    for star, info in data.items():

        # 'info' is the inner dictionary

        print(f"{star}: Spectral Type {info['Spectral Type']}")

print_star_names(targets)

print_spectral_types(targets)


def find_dimmer_stars(data):

    print("Stars dimmer than 0.1 mag:")

    for star, info in data.items():

        if info["Magnitude"] > 0.1:

            print(f"- {star} ({info['Magnitude']})")

find_dimmer_stars(targets)

targets["Aldebaran"] = {
    "RA": "04h 35m 55.2s",
    "Dec": "+16° 30′ 33″",
    "Magnitude": 0.85,
    "Spectral Type": "K5III"
}

def find_brightest_near_20(data):
    
    closest_star = None
    
    min_diff = float('inf')
    
    for star, info in data.items():
    
        dec_str = info["Dec"]
 
    
        dec_deg = float(dec_str.split('°')[0].replace('−', '-'))

        diff = abs(dec_deg - 20)
        
       
    
        if diff < min_diff:
    
            min_diff = diff
    
            closest_star = star
            
    return closest_star

brightest = find_brightest_near_20(targets)

print(f"The star closest to 20° Dec is: {brightest}")

print("Favorite Constellation: Sagittarius")