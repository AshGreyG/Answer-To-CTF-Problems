from typing import Dict, List

# This problem is based on ook! language: https://www.dcode.fr/ook-language.
# It's derived from brainfuck language.
#
# Ook. Ook. -> +
# Ook! Ook! -> -
# Ook. Ook? -> >
# Ook? Ook. -> <
# Ook! Ook? -> [
# Ook? Ook! -> ]
# Ook! Ook. -> .
# Ook. Ook! -> ,

def brainfuck_eval(raw_code : str, input_str : str = "") -> str :
    output : List[str] = []
    valid = "+-><.,[]"
    code = [c for c in raw_code if c in valid]
    code_len = len(code)
    code_ptr = 0

    memory = [0] * 3000
    ptr = 0

    input_ptr = 0

    loop_map : Dict[int, int] = {}
    stack : List[int] = []

    for i, op in enumerate(code) :
        if op == "[" :
            stack.append(i)
        elif op == "]" :
            if not stack :
                raise SyntaxError("Mismatched loop end symbol ]")
            left_index = stack.pop()
            loop_map[left_index] = i
            loop_map[i] = left_index

    while code_ptr < code_len :
        match code[code_ptr] :
            case "+" :
                temp = memory[ptr] + 1
                if temp > 255 :
                    memory[ptr] = temp % 256
                else :
                    memory[ptr] = temp
            case "-" :
                temp = memory[ptr] - 1
                if temp < 0 :
                    memory[ptr] = (temp + 256) % 256
                else :
                    memory[ptr] = temp
            case ">" :
                ptr += 1
            case "<" :
                ptr -= 1
            case "." :
                output.append(chr(memory[ptr]))
            case "," :
                if input_ptr < len(input_str) :
                    memory[ptr] = ord(input_str[input_ptr])
                else :
                    memory[ptr] = 0
            case "[" :
                if memory[ptr] == 0 :
                    code_ptr = loop_map[code_ptr]
            case "]" :
                if memory[ptr] != 0 :
                    code_ptr = loop_map[code_ptr]
        code_ptr += 1

    return "".join(output)

def ook_only_symbol_eval(raw_code : str, input_str : str = "") -> str :
    valid = ".!?"
    code = "".join([c for c in raw_code if c in valid])

    brainfuck_ops = ""

    for i in range(0, len(code), 2) :
        match code[i:i + 2] :
            case ".." :
                brainfuck_ops += "+"
            case "!!" :
                brainfuck_ops += "-"
            case ".?" :
                brainfuck_ops += ">"
            case "?." :
                brainfuck_ops += "<"
            case "!?" :
                brainfuck_ops += "["
            case "?!" :
                brainfuck_ops += "]"
            case "!." :
                brainfuck_ops += "."
            case ".!" :
                brainfuck_ops += ","

    return brainfuck_eval(brainfuck_ops, input_str)

ook_ops = ""

with open("file.txt", "r", encoding = "utf-8") as file :
    for line in file :
        tokens = map(lambda s : s[-1], line.strip().split(" "))
        for ch in tokens :
            ook_ops += ch

print(f"Ook! ops are: \n{ook_ops}")
print(f"Evaluate Ook! result: \n{ook_only_symbol_eval(ook_ops)}")

# Result is flag{0a394df55312c51a}, and this problem is abstracted to the utils
