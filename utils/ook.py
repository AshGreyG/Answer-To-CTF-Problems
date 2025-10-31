from brainfuck import brainfuck_eval

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
