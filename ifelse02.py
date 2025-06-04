parol = input("Parolni kiriting: ")


kamida_8_belgi = len(parol) >= 8


kamida_bir_harf = (
    'a' in parol or 'b' in parol or 'c' in parol or 'd' in parol or 'e' in parol or
    'f' in parol or 'g' in parol or 'h' in parol or 'i' in parol or 'j' in parol or
    'k' in parol or 'l' in parol or 'm' in parol or 'n' in parol or 'o' in parol or
    'p' in parol or 'q' in parol or 'r' in parol or 's' in parol or 't' in parol or
    'u' in parol or 'v' in parol or 'w' in parol or 'x' in parol or 'y' in parol or 'z' in parol or
    'A' in parol or 'B' in parol or 'C' in parol or 'D' in parol or 'E' in parol or
    'F' in parol or 'G' in parol or 'H' in parol or 'I' in parol or 'J' in parol or
    'K' in parol or 'L' in parol or 'M' in parol or 'N' in parol or 'O' in parol or
    'P' in parol or 'Q' in parol or 'R' in parol or 'S' in parol or 'T' in parol or
    'U' in parol or 'V' in parol or 'W' in parol or 'X' in parol or 'Y' in parol or 'Z' in parol
)


kamida_bir_raqam = (
    '0' in parol or '1' in parol or '2' in parol or '3' in parol or '4' in parol or
    '5' in parol or '6' in parol or '7' in parol or '8' in parol or '9' in parol
)


kamida_bir_maxsus = (
    '!' in parol or '@' in parol or '#' in parol or '$' in parol or '%' in parol or
    '^' in parol or '&' in parol or '*' in parol or '(' in parol or ')' in parol or
    '-' in parol or '_' in parol or '+' in parol or '=' in parol or ':' in parol or
    ';' in parol or '"' in parol or "'" in parol or '<' in parol or '>' in parol or
    ',' in parol or '.' in parol or '/' in parol or '?' in parol or '|' in parol or '\\' in parol
)


if kamida_8_belgi and kamida_bir_harf and kamida_bir_raqam and kamida_bir_maxsus:
    print("Parol qabul qilindi.")
else:
    print("Parol noto'g'ri. Kamida 8 belgi, 1 harf, 1 raqam va 1 maxsus belgi bo'lishi kerak.")

