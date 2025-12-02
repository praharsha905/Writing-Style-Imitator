import random
import re

# --- Author Style Definitions ---

# Original Shakespearean Style
SHAKESPEAREAN_ANACHRONISMS = {
    "wi-fi": [
        "Hark! My Wi-Fi doth waver like Hamlet's sanity.",
        "Verily, my connection to the Globe's web is more fickle than a lover's heart.",
        "Doth my Wi-Fi scorn me? Its strength is less than Romeo's resolve.",
        "A plague on this weak signal! My Wi-Fi hath forsaken me.",
    ],
    "internet": [
        "Alas, the Globe's grand web hath failed me in mine hour of need!",
        "The carrier pigeons of the internet seem to have lost their way.",
        "Mine access to the digital Globe is as blocked as a plague-ridden town.",
        "What light through yonder window breaks? 'Tis not the internet, for it is down.",
    ],
    "battery": [
        "My device's life-force dwindles! Its battery is nigh on empty.",
        "Woe is me, for my phone's battery hath fled, like a coward from the fray.",
        "This low battery warning is a dagger to my heart!",
        "Hark, my phone's spirit wanes; its battery cries out for a charger's kiss.",
    ],
    "love": [
        "My love for thee is as boundless as the sea, and my data plan.",
        "Shall I compare thee to a summer's day? Thou art more lovely and more temperate, and hast better Wi-Fi.",
        "Love is a smoke made with the fume of sighs, and the blue light of a screen.",
        "If music be the food of love, then a full battery is its grand feast.",
    ],
    "sleep": [
        "To sleep, perchance to dream—ay, there's the rub, for my alarm is set for the morrow.",
        "My desire for slumber doth rival the ambition of Macbeth.",
        "O gentle sleep, nature's soft nurse, why dost thou flee from my weary eyes?",
        "I am so sleepy, I could be bounded in a nutshell and count myself a king of infinite space.",
    ],
    "work": [
        "To work, or not to work, that is the question.",
        "This toil doth vex me more than a midsummer's nightmare.",
        "I am weary of this labour; would that I were a player upon the stage!",
        "My workday is a tale told by an idiot, full of sound and fury, signifying overtime.",
    ],
    "food": [
        "What culinary delight awaits? My stomach doth rumble with anticipation.",
        "Is this a dagger which I see before me, or merely a fork pointing to pizza?",
        "A feast! A feast! My kingdom for a feast!",
        "To eat, or not to eat, that is a foolish question.",
    ],
    "coffee": [
        "This brew of beans is the very elixir of life! Pour me another, good sir.",
        "O, this blessed coffee! It doth mend my weary soul.",
        "My kingdom for a cup of this dark, magical potion!",
        "Without my morning's coffee, I am but a shadow of my former self.",
    ],
    "code": [
        "This code be a tangled web of sorrow! Would that I could debug with a flourish of a quill.",
        "To refactor, or not to refactor, that is the programmer's eternal query.",
        "Alas, a bug! A most pernicious bug! My script is undone!",
        "The quality of my code is not strained; it droppeth as the gentle rain from heaven.",
    ],
}
SHAKESPEAREAN_FALLBACKS = [
    "Thou speakest in riddles! Prithee, try thy words again.",
    "Hark! Thine utterance confounds me. Speak plainly, if thou canst.",
    "Thy words are as a foreign tongue to mine ears. What meanest thou?",
    "Verily, I understandeth not. Perchance a simpler phrase would suffice?",
    "A curious sentiment! But its meaning escapes my humble wit.",
]

# Edgar Allan Poe Style
POE_ANACHRONISMS = {
    "wi-fi": [
        "The signal, a faint and flickering phantom, fades into the encroaching darkness. Nevermore.",
        "This ghastly spectre of a connection haunts my device with its weakness.",
        "A creeping dread consumes me as the Wi-Fi bars descend into the abyss."
    ],
    "internet": [
        "I am lost within the digital abyss, a bleak and boundless expanse where connection is but a fleeting, tortured dream.",
        "The web is a catacomb of broken links and desolate pages, each a monument to my despair.",
        "This cursed internet whispers promises of knowledge, only to deliver the silence of the tomb."
    ],
    "battery": [
        "The crimson ember of life upon the screen wanes, its faint glow extinguished by the remorseless void. It is dead.",
        "A chilling pallor creeps across the screen; the battery, like a failing heart, has ceased its frantic beat.",
        "The device lies cold and lifeless, its spirit having fled with the final spark of its battery."
    ],
    "love": [
        "Love? A feverish dream, a torment of the soul that promises light but delivers only the deepest, most desolate shadow.",
        "My heart, a tell-tale thing, beats madly for one who can never be mine, a love lost to the chasms of sorrow.",
        "To love is to invite madness, to gaze into the beautiful eyes of ruin."
    ],
    "sleep": [
        "To sleep is to descend into the maelstrom of nightmare, a terrifying solace from the waking horror of existence.",
        "In sleep, I find no respite, only visions of terror that claw at the edges of my sanity.",
        "The descent into slumber is but a rehearsal for the final, unending darkness."
    ],
    "code": [
        "Each line of code, a maddening hieroglyph in a labyrinth of despair, where a single bug whispers of eternal failure.",
        "The script is a raven, tapping, tapping at the chamber door of my processor, refusing to compile.",
        "This algorithm is a pit and a pendulum, swinging ever closer to a fatal system crash."
    ],
}
POE_FALLBACKS = [
    "Thy words echo in the hollow chambers of my soul, yet their meaning is lost to the shadows.",
    "A chilling utterance, devoid of sense, a morbid whisper from the void.",
    "You speak, and a creeping horror, whose name I cannot guess, chills my very marrow."
]

# Jane Austen Style
AUSTEN_ANACHRONISMS = {
    "wi-fi": [
        "It is a truth universally acknowledged, that a household in possession of a good fortune must be in want of a reliable Wi-Fi signal.",
        "One's connection is most unstable. How is one to receive the latest society gossip with such an impediment?",
        "The quality of the Wi-Fi is most disagreeable and has put me in a temper."
    ],
    "internet": [
        "One simply cannot be expected to procure a suitable match on the internet without a reliable connection. It is most vexing.",
        "The internet is the talk of the town, though I find it a rather vulgar medium for correspondence.",
        "To be without the internet is to be entirely cut off from the world of eligible suitors and scandalous news."
    ],
    "battery": [
        "A phone's battery life, much like a young lady's reputation, is a delicate thing, easily and tragically depleted.",
        "My phone's battery has expired. I am now entirely at the mercy of my own thoughts, a most perilous situation.",
        "One finds one's spirits, much like one's battery, draining at an alarming rate."
    ],
    "love": [
        "Love is a matter of sense and sensibility, though a handsome fortune and a shared data plan do not go amiss.",
        "He is tolerable, I suppose, but not handsome enough to tempt me to share my charger.",
        "To be in love is to be in a state of perpetual anxiety over replied-to texts."
    ],
    "food": [
        "A well-laid table is the height of civility, though one must confess, this pizza is a rather scandalous, if delicious, affair.",
        "I am in need of sustenance. The lack of cake at this establishment is a great slight upon my character.",
        "The appetite, once awakened, must be satisfied, lest one become irritable."
    ],
    "work": [
        "One's daily work is a necessary burden, though one wishes it did not so thoroughly interfere with one's correspondence and social calls.",
        "It is a shame that one must work for a living, but a greater shame to do it without tea.",
        "I have no doubt that a long day of work improves the character, but I find it does little for my mood."
    ],
}
AUSTEN_FALLBACKS = [
    "I confess I am at a loss to comprehend your meaning. Perhaps you would be so good as to rephrase your sentiment?",
    "A most peculiar turn of phrase. I daresay it would not be uttered in polite society.",
    "Your statement lacks the propriety and clarity one expects from intelligent discourse."
]

# --- Master Dictionary of Authors ---
AUTHOR_STYLES = {
    "1": {
        "name": "William Shakespeare",
        "prompt": "Enter thy modern sentence: ",
        "responses": SHAKESPEAREAN_ANACHRONISMS,
        "fallbacks": SHAKESPEAREAN_FALLBACKS,
        "farewell": "\nFarewell, gentle friend!"
    },
    "2": {
        "name": "Edgar Allan Poe",
        "prompt": "Whisper thy dreadful sentence: ",
        "responses": POE_ANACHRONISMS,
        "fallbacks": POE_FALLBACKS,
        "farewell": "\nMay the shadows claim thee not."
    },
    "3": {
        "name": "Jane Austen",
        "prompt": "State your observation: ",
        "responses": AUSTEN_ANACHRONISMS,
        "fallbacks": AUSTEN_FALLBACKS,
        "farewell": "\nI bid you a good day."
    }
}


# --- Core Functions ---
def find_matching_keyword(sentence: str, response_dict: dict) -> str or None:
    """Finds the first matching keyword from the given dictionary in the user's sentence."""
    for keyword in response_dict:
        if re.search(r'\b' + re.escape(keyword) + r'\b', sentence, re.IGNORECASE):
            return keyword
    return None

def get_author_style_translation(sentence: str, author_style: dict) -> str:
    """Translates a modern sentence into the chosen author's style."""
    responses = author_style["responses"]
    fallbacks = author_style["fallbacks"]

    keyword = find_matching_keyword(sentence, responses)

    if keyword:
        return random.choice(responses[keyword])
    else:
        return random.choice(fallbacks)

def run_converter():
    """Main function to run the converter in a command-line interface."""

    # Author Selection
    while True:
        print("--- Literary Style Text Converter ---")
        print("Choose thy author:")
        for key, value in AUTHOR_STYLES.items():
            print(f"  {key}. {value['name']}")

        choice = input("\nEnter the number of your choice: ")
        if choice in AUTHOR_STYLES:
            selected_author = AUTHOR_STYLES[choice]
            break
        else:
            print("\nInvalid choice. Prithee, select a valid number.\n")

    # Main Interaction Loop
    print(f"\n--- You have chosen the style of {selected_author['name']} ---")
    print("Type 'quit' or 'exit' to bid farewell.\n")

    while True:
        try:
            user_input = input(selected_author['prompt'])

            if user_input.lower() in ['quit', 'exit']:
                print(selected_author['farewell'])
                break

            if not user_input.strip():
                print("\nPrithee, bestow upon me some words to transform!")
                continue

            translation = get_author_style_translation(user_input, selected_author)
            print(f"\n> {translation}\n")

        except (EOFError, KeyboardInterrupt):
            print(f"\n{selected_author['farewell']}")
            break

# Run the main converter function when the script is executed
if __name__ == "__main__":
    run_converter()
