pip install googletrans==4.0.0-rc1


from googletrans import Translator, LANGUAGES



def display_languages():
    """
    Display all supported languages with their codes.
    """
    print("Available Languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")




def translate_text(text, src_language, dest_language):
    """
    Translate text using Google Translate API.
    
    Args:
        text (str): Text to translate.
        src_language (str): Source language code (e.g., 'en' for English).
        dest_language (str): Target language code (e.g., 'es' for Spanish).
    
    Returns:
        str: Translated text.
    """
    translator = Translator()
    try:
        translation = translator.translate(text, src=src_language, dest=dest_language)
        return translation.text
    except Exception as e:
        return f"Error: {e}"




def main():
    """
    Main function to run the translation tool.
    """
    print("Welcome to the Language Translation Tool!")
    
    while True:
        print("\nMenu:")
        print("1. View available languages")
        print("2. Translate text")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            display_languages()
        elif choice == '2':
            text = input("\nEnter the text to translate: ").strip()
            src_language = input("Enter the source language code (or type 'auto' to detect): ").strip()
            dest_language = input("Enter the target language code: ").strip()
            translated_text = translate_text(text, src_language, dest_language)
            print(f"\nTranslated Text: {translated_text}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()


INPUT:
    Enter the text to translate: Hello, how are you?
    Enter the source language code (or type 'auto' to detect): en
    Enter the target language code: es



OUTPUT:
    Translated Text: Hola, ¿cómo estás?




