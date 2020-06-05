from pathlib import Path
import json

american_to_british = {}
british_to_american = {}

for path in Path('classes/Language/Words/AmericanBritish').glob('*.php'):
    with open(path) as f:
        text = f.read().splitlines()
    for line in text:
        if '=>' not in line:
            continue
        line = line.replace("\\'", '^').replace("'", '').replace('^',"'")
        american, british = [e.strip() for e in line.split('=>')]
        if british.endswith(','):
            british = british[:-1]
        if british.startswith('['):
            british = british[1:-1]
            if british.endswith(','):
                british = british[:-1]
            british = [e.strip() for e in british.split(',')]
        else:
            british = [british]

        american_to_british[american] = british[0]

        for word in british:
            british_to_american[word] = american

with open('american-to-british.json', 'w') as f:
    json.dump(american_to_british, f, sort_keys=True, separators=',:')

with open('british-to-american.json', 'w') as f:
    json.dump(british_to_american, f, sort_keys=True, separators=',:')