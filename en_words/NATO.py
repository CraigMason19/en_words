"""
NATO.py
-------

Provides useful helper functions for working with the NATO alphabet
 
https://www.nato.int/en/about-us/nato-history/history-by-theme/symbols-of-nato/nato-phonetic-alphabet
"""

NATO_LOOKUP: dict[str, str] = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',

    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu',
}

NATO_PHONETIC_LOOKUP: dict[str, str] = {
    '0': 'Zee-ro',
    '1': 'Wun',
    '2': 'Too',
    '3': 'Tree',
    '4': 'Fow-er',
    '5': 'Fife',
    '6': 'Six',
    '7': 'Sev-en',
    '8': 'Ait',
    '9': 'Nin-er',

    'A': 'Al-fah',
    'B': 'Brah-voh',
    'C': 'Char-lee',
    'D': 'Dell-tah',
    'E': 'Eck-oh',
    'F': 'Foks-trot',
    'G': 'Golf',
    'H': 'Hoh-tel',
    'I': 'In-dee-ah',
    'J': 'Jew-lee-ett',
    'K': 'Key-loh',
    'L': 'Lee-mah',
    'M': 'Mike',
    'N': 'No-vem-ber',
    'O': 'Oss-cah',
    'P': 'Pah-pah',
    'Q': 'Keh-beck',
    'R': 'Row-me-oh',
    'S': 'See-air-rah',
    'T': 'Tang-go',
    'U': 'You-nee-form',
    'V': 'Vic-tah',
    'W': 'Wiss-key',
    'X': 'Ecks-ray',
    'Y': 'Yang-key',
    'Z': 'Zoo-loo'
}