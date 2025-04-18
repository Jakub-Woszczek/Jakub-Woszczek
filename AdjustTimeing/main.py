from random import shuffle


def replace_lines_in_html(file_path, lines_to_change, output_path=None):
    """
    Zamienia wybrane linie w pliku HTML.

    :param file_path: ścieżka do oryginalnego pliku HTML
    :param replacements: słownik {numer_linii: "nowa zawartość"}
                         (numeracja od 1, jak w edytorze tekstu)
    :param output_path: opcjonalnie ścieżka do nowego pliku
                        (jeśli None, nadpisze oryginał)
    """
    shuffle(lines_to_change)
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i,line_no in enumerate(lines_to_change):
        if 1 <= line_no <= len(lines):
            delay = round(0.5+i*0.1,1)
            lines[line_no - 1] = f'      animation-delay: {delay}s;' + '\n'
            # print(lines[line_no - 1])
        else:
            print(f"⚠️ Linia {line_no} poza zakresem.")

    with open(output_path or file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print("✅ Zamieniono wskazane linie.")

lines_to_replace = [35,66,89,147,171,207,240,316,376,420,470]
replace_lines_in_html("index.html", lines_to_replace)