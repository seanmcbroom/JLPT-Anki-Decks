from bs4 import BeautifulSoup
import requests

def from_word(word):
    result = {
        'hiragana': '',
        'part_of_speech': '',
        'meaning': '',
        'examples': []
    }

    # Fetch the page content
    url = f'https://jisho.org/search/{word}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get the first result on the page
    main_result = soup.find("div", class_="concept_light clearfix")
    
    if not main_result:
        return {'error': 'Word not found'}
    
    # Get hiragana reading
    hiragana = main_result.find("span", class_="furigana").text.strip()
    result['hiragana'] = hiragana
    
    # Get part of speech and first meaning
    meanings_section = main_result.find("div", class_="concept_light-meanings")
    
    if meanings_section:
        first_meaning_wrapper = meanings_section.find("div", class_="meaning-wrapper")
        
        # Extract part of speech
        part_of_speech = first_meaning_wrapper.find_previous_sibling("div", class_="meaning-tags").text.strip()
        # Extract the first English meaning
        meaning = first_meaning_wrapper.find("span", class_="meaning-meaning").text.strip()

        result['part_of_speech'] = part_of_speech
        result['meaning'] = meaning
    else:
        return {'error': 'No meanings found'}
    
    # Find example sentences related to the first meaning
    example_sentences_div = first_meaning_wrapper.find("span", class_="sentences")
    
    if example_sentences_div:
        example_sentences = example_sentences_div.find_all("div", class_="sentence")

        for example in example_sentences:
            # Combine all Japanese text elements
            ja_example_elements = example.find("ul", class_="japanese_gothic").find_all("li", class_="clearfix")
            ja_example_sentence_string = ''.join([el.find("span", class_="unlinked").text.strip() for el in ja_example_elements if el.find("span", class_="unlinked")])

            # Find English example sentence
            en_example = example.find("span", class_="english").text.strip()

            result['examples'].append({
                'ja': ja_example_sentence_string,
                'en': en_example
            })
    else:
        result['examples'].append({
            'ja': "",
            'en': ""
        })
    
    return result