def find_digits_chars_symbols(sample_str):
    letter_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if "A"<= char <="z" :
            letter_count += 1
        elif "0"<= char <= "9":
            digit_count += 1
        else:
            symbol_count += 1

    print("letters =", letter_count)
    print("digits =", digit_count)
    print("symbols =", symbol_count)

str1=input()
find_digits_chars_symbols


