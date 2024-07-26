import json
import os
import genanki

DECK_NAME = "JLPT N5 Kanji"
DECK_VERSION = "v1.0.5"

# Create a new deck
my_deck = genanki.Deck(
    29647345129,
    'Japanese N5 Kanji'
)

# Create a new model
my_model = genanki.Model(
    88937610236,
    f'Japanese[{DECK_NAME}]',
    fields=[
        {'name': 'Kanji'},
        {'name': 'MeaningEN'},
        {'name': 'Version'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '''
                <p class="word">
                    {{Kanji}}
                </p>
            ''',
            'afmt': '''
                <p class="word">
                    {{Kanji}}
                </p>
                
                <br>
                
                <p>{{MeaningEN}}</p>
                <hr id=answer>
                
                <br>
                
                <p class="footer-links grey">deck version: {{Version}} ~ <a href='https://jisho.org/search/{{Kanji}} %23kanji'>jisho</a>, <a href="https://www.google.com/search?q='{{Kanji}}'">google</a></p>
            '''
        }
    ],
    css='''
        .card {
            font-family: sans-serif, arial, system-ui;
            font-size: 20px;
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: black;
            background-color: white;
        }

        p {
            margin: 2px;
        }

        .grey {	
            color: #888;
        }

        .flex-column {
            display: flex;
            flex-direction: row;
            gap: 5px;
        }

        .word {
            font-size: 35px;
        }
        
        .footer-links {
            font-size: 15px;
        }
    '''
)

def add_cards_from_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for card in data:
        note = genanki.Note(
            model=my_model,
            fields=[
                card,
                data[card]['meaning'],
                DECK_VERSION
            ]
        )
        my_deck.add_note(note)

add_cards_from_json_file('./lists/n5_kanji.json')

# Save the deck to a file
genanki.Package(my_deck).write_to_file(f'./output/{DECK_NAME}.apkg')
