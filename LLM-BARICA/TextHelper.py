class TextHelper: 
    @staticmethod
    def remove_croatian_chars(text: str) -> str:
        replacements = {
            "č": "ch",
            "ć": "ch",
            "š": "sh",
            "ž": "zh",
            "đ": "dj",
            "Č": "Ch",
            "Ć": "Ch",
            "Š": "Sh",
            "Ž": "Zh",
            "Đ": "Dj",
        }

        output = []
        for char in text:
            output.append(replacements.get(char, char))
        return "".join(output)
