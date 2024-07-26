import json
import os
import genanki

DECK_NAME = "JLPT N4 Vocab"
DECK_VERSION = "v1.0.5"

# Create a new deck
my_deck = genanki.Deck(
    2059400110,
    'Japanese N4 Vocab'
)

# Create a new model
my_model = genanki.Model(
    12121212,
    f'Japanese[{DECK_NAME}]',
    fields=[
        {'name': 'WordJA'},
        {'name': 'Kana'},
        {'name': 'PartOfSpeech'},
        {'name': 'ExampleJA'},
        {'name': 'ExampleEN'},
        {'name': 'MeaningEN'},
        {'name': 'Version'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '''
                <p class="word">
                    {{WordJA}}
                </p>
                <p class="pos grey">{{PartOfSpeech}}</p>
            ''',
            'afmt': '''
                <p class="furigana">{{Kana}}</p>
                <p class="word">
                    {{WordJA}}
                </p>
                <p class="pos grey">{{PartOfSpeech}}</p>
                
                <br>
                
                <p>{{MeaningEN}}</p>
                <hr id=answer>
                
                <br>
                
                {{#ExampleJA}}{{#ExampleEN}}
                <p>example:</p>
                <p>{{ExampleJA}}</p>
                <p class="hide">{{ExampleEN}}</p>
                <br>
                {{/ExampleEN}}{{/ExampleJA}}
                
                <p class="footer-links grey">deck version: {{Version}} ~ <a href='https://jisho.org/search/{{Kana}}'>jisho</a>, <a href="https://www.google.com/search?q='{{WordJA}}'">google</a></p>
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
					
        .pos {
            font-size: 20px;
        }
        
        .furigana {
            font-size: 20px;
        }
        
        .footer-links {
            font-size: 15px;
        }
    '''
)

def add_cards_from_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                note = genanki.Note(
                    model=my_model,
                    fields=[
                        data.get('WordJA', ''),
                        data.get('Kana', ''),
                        data.get('PartOfSpeech', ''),
                        data.get('ExampleJA', ''),
                        data.get('ExampleEN', ''),
                        data.get('MeaningEN', ''),
                        DECK_VERSION
                    ]
                )
                my_deck.add_note(note)

add_cards_from_directory('./cards/n4-vocab')

genanki.Package(my_deck).write_to_file(f'./output/{DECK_NAME}.apkg')