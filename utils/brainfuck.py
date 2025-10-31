from typing import List, Dict

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
