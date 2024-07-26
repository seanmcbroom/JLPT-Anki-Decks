import json
import os
import genanki

DECK_NAME = "JLPT N5 Vocab"
DECK_VERSION = "v1.0"

# Create a new deck
my_deck = genanki.Deck(
    493727845234,
    'Japanese N5 Vocab'
)

# Create a new model
my_model = genanki.Model(
    234560928,
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
                <p class="furigana">{{Kana}}</p>
                <p class="main-content">
                    {{WordJA}}
                </p>
                <p class="pos grey">{{PartOfSpeech}}</p>
                <br>
                {{#ExampleJA}}{{#ExampleEN}}
                <p id="examples" class="flex-column">
                    <p>Example:</p>
                    <p>{{ExampleJA}}</p>
                    <p class="hide">{{ExampleEN}}</p>
                </p>
                {{/ExampleEN}}{{/ExampleJA}}
            ''',
            'afmt': '''
                <p class="furigana">{{Kana}}</p>
                <p class="main-content">
                    {{WordJA}}
                </p>
                <p class="pos grey">{{PartOfSpeech}}</p>
                <br>
                <p>meaning: {{MeaningEN}}</p>
                <br>
                <p class="grey" style="font-size: 15px;">Deck Version: {{Version}} ~ <a href='https://jisho.org/search/{{Kana}}'>jisho</a>, <a href="https://www.google.com/search?q='{{WordJA}}'">google</a></p>
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

        .main-content {
            font-size: 35px;
        }
					
        .pos {
            font-size: 20px;
        }
        
        .furigana {
            font-size: 20px;
        }

        .hide {
            background-color: #111;
            color: #111;
            padding: 5px;
        }

        .hide:hover {
            color: white;
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

# Save the deck to a file
genanki.Package(my_deck).write_to_file(f'./output/{DECK_NAME}.apkg')
