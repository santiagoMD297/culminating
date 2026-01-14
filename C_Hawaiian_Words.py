class Translator:
    def __init__(self):
        # Hawaiian vowels and consonants
        self.vowels = set("aeiou")
        self.consonants = set("pkhlmnw")

        # Valid characters in input (plus space and apostrophe)
        self.valid_chars = self.vowels | self.consonants | set([" ", "'"])

        # Vowel group pronunciations
        self.vowel_groups = {
            "ai": "eye",
            "ae": "eye",
            "ao": "ow",
            "au": "ow",
            "ei": "ay",
            "eu": "eh-oo",
            "iu": "ew",
            "oi": "oy",
            "ou": "ow",
            "ui": "ooey",
        }

        # Single vowel pronunciations
        self.single_vowels = {
            "a": "ah",
            "e": "eh",
            "i": "ee",
            "o": "oh",
            "u": "oo",
        }

    def _is_valid_phrase(self, phrase: str) -> bool:
        """
        Check that the phrase only uses valid Hawaiian characters,
        spaces, or apostrophes.
        """
        for ch in phrase:
            if ch.lower() not in self.valid_chars:
                return False
        return True

    def translate(self, phrase: str) -> str:
        """
        Translate a Hawaiian phrase into its phonetic pronunciation.

        - Returns "invalid" if any invalid character appears.
        - Words stay separated by spaces.
        - Syllables inside a word are separated with hyphens.
        """
        phrase = phrase.lower()

        # Validate
        if not self._is_valid_phrase(phrase):
            return "invalid"

        words = phrase.split(" ")
        translated_words = []

        for word in words:
            if word == "":
                translated_words.append("")
            else:
                translated_words.append(self._translate_word(word))

        return " ".join(translated_words)

    def _translate_word(self, word: str) -> str:
        """
        Translate a single Hawaiian word (no spaces) into syllables.
        """
        syllables = []
        current_consonants = ""
        last_vowel = None  # used to decide w -> w or v

        i = 0
        n = len(word)

        while i < n:
            ch = word[i]

            # Apostrophe = hard break; keep it simple (ignore for tests)
            if ch == "'":
                i += 1
                continue

            # Consonant (including w)
            if ch in self.consonants:
                if ch == "w":
                    # w rules:
                    # - start or after a/o/u/None: "w"
                    # - after i/e: "v"
                    if last_vowel in ["i", "e"]:
                        current_consonants += "v"
                    else:
                        current_consonants += "w"
                else:
                    current_consonants += ch
                i += 1
                continue

            # Vowel
            if ch in self.vowels:
                # Check for vowel group
                pair = None
                if i + 1 < n and word[i + 1] in self.vowels:
                    pair = ch + word[i + 1]

                if pair and pair in self.vowel_groups:
                    pron = self.vowel_groups[pair]
                    i += 2
                    last_vowel = pair[1]  # second vowel in the pair
                else:
                    pron = self.single_vowels[ch]
                    i += 1
                    last_vowel = ch

                syllable = current_consonants + pron
                syllables.append(syllable)
                current_consonants = ""
                continue

            # Should never hit this because of validation
            i += 1

        # If somehow we have trailing consonants, attach them to last syllable
        if current_consonants and syllables:
            syllables[-1] += current_consonants

        # Join syllables with hyphens inside the word
        return "-".join(syllables)


# Sample usage (optional – you can keep or delete this block)
if __name__ == "__main__":
    translator = Translator()
    print(translator.translate("maui keiki"))