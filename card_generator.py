import json
import time
import jisho_parser

with open('./word-lists/n4_words.json', 'r', encoding='utf-8') as n4_words_file:
    n4_words = json.load(n4_words_file)

for word in n4_words:
    try:
        parsed_data = jisho_parser.from_word(word)
        
        if 'error' in parsed_data:
            print(f"Error for word '{word}': {parsed_data['error']}")
        else:    
            json_data = {
                "WordJA": word,
                "Kana": n4_words[word]['kana'],
                "PartOfSpeech": parsed_data.get('part_of_speech', ''),
                "ExampleJA": parsed_data.get('examples', {})[0].get('ja', ''),
                "ExampleEN": parsed_data.get('examples', {})[0].get('en', ''),
                "MeaningEN": parsed_data.get('meaning', '')
            }
            
            # Save results to a new JSON file
            with open(f'./cards/n4-vocab/{word}.json', 'w', encoding='utf-8') as outfile:
                json.dump(json_data, outfile, ensure_ascii=False, indent=4)
    except Exception as e:
                print(f"Failed to process word '{word}': {e}")
    
    time.sleep(5) # sleep between so jisho doesn't get mad