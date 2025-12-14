# Šifrovací nástroj (Playfair varianta)
Grafická aplikace v Pythonu/Tkinteru pro kódování a dekódování textu pomocí matic 5×5 nebo 6×6 a klíčového slova. Podporuje vlastní matici, kontrolu chybějících písmen a českou/anglickou abecedu.

## Požadavky
- Python 3.9+ s knihovnami `tkinter` a `numpy` (Tkinter je součástí standardní instalace na Windows/macOS; na Linuxu jej případně doinstalujte)

## Spuštění
```bash
python kod.py
```
Po spuštění se otevře okno aplikace.

## Použití
- **Text** – vstupní text k zakódování nebo dekódování.
- **Kódovací slovo** – klíč pro permutaci sloupců (při dekódování musí být stejné jako při kódování).
- **Český jazyk** – přepíná variantu abecedy (slučování W/V nebo J/I).
- **6x6 matice** – volí větší matici (26 písmen + číslice).
- **Zakódovat** – vygeneruje náhodnou matici (pokud není zadaná vlastní), zobrazí ji a vrátí šifrovaný text.
- **Odkódovat** – použije matici zadanou ve vstupním poli a vrátí dešifrovaný text.

## Vlastní matice
- Matice se zadává do víceradého pole jako řádky s hodnotami oddělenými mezerou, např. pro 5×5:
  ```
  A B C D E
  F G H I J
  K L M N O
  P Q R S T
  U V W X Y
  ```
- Tlačítko **Zkontrolovat chybějící písmena** vypíše, která písmena/znaky v matici chybí (užitečné při ručním zadání).

## Tipy a omezení
- Při dekódování je nutné použít stejnou matici i kódovací slovo jako při kódování.
- Mezery a číslice se při kódování převádějí na zástupné sekvence (např. `XMEZERAX`, `XTWOX`) a při dekódování se nahrazují zpět.
- Pro reprodukovatelné výsledky je možné v kódu před spuštěním aplikace nastavit seed pro `random`.
