#macro parser
def _parse_macros(self):
    self._available_macros = ["MV", "SWP", "SUM", "WHILE"]

    lines = []

    for (line, p, o) in self._lines:
        lineNumber = len(lines) + 1

        if line[0] != "$":
            if len(line.strip()) > 0:
                lines.append((line, lineNumber, lineNumber))
            continue
        
        parseResult = _parse_macro(self, line, p, o)
        if len(parseResult) == 0:
            return
        
        for l in parseResult:
            lineNumber = len(lines) + 1
            if(len(l.strip()) > 0):
                lines.append((l.strip(), lineNumber, lineNumber))
    
    self._lines = lines.copy()

def _parse_macro(self, line, p, o):   
    l = line[1:]
    macro_split = l.strip().split("(")
    macro_name = macro_split[0]

    if macro_name not in self._available_macros:
        self._flag = False
        self._line = o
        self._errm = "Unknown macro appeared!"
        return []
        
    macro_arg_split = macro_split[1].split(")")

    if len(macro_arg_split) > 1 and len(macro_arg_split[1]) > 0 and macro_arg_split[1] != "\n":
        self._flag = False
        self._line = o
        self._errm = "Invalid arguments for macro!"
        return []

    macro_arguments = macro_arg_split[0].split(",")

    if any(map(lambda x: len(x) == 0, macro_arguments)):
            self._flag = False
            self._line = o
            self._errm = "Invalid arugements for macro(empty strings)!"
            return []

    if macro_name == "MV":
        if len(macro_arguments) != 2:
            self._flag = False
            self._flag = o
            self._errm = "Invalid arguments for macro(number of arguments)!"
            return []
        return _move_macro(self, macro_arguments[0], macro_arguments[1])
    
    elif macro_name == "SWP":
        if len(macro_arguments) != 2:
            self._flag = False
            self._flag = o
            self._errm = "Invalid arguments for macro(number of arguments)!"
            return []
        return _swap_macro(self, macro_arguments[0], macro_arguments[1])
        
    elif macro_name == "SUM":
        if len(macro_arguments) != 3:
            self._flag = False
            self._line = o
            self._errm = "Invalid arguments for macro(number of arguments)!"
            return []
        return _sum_macro(self, macro_arguments[0], macro_arguments[1], macro_arguments[2])

#macros templates
def _move_macro(self, a, b):
    return [f"@{a}",
            "D=M",
            f"@{b}",
            "M=D"]

def _swap_macro(self, a, b):
    self._macro_count += 1
    temp = "@swap." + str(self._macro_count)

    return [
        f"@{a}",
        "D=M",
        temp,
        "M=D",
        f"@{b}",
        "D=M",
        f"@{a}",
        "M=D",
        temp,
        "D=M",
        f"@{b}",
        "M=D"
    ]

def _sum_macro(self, a, b, d):
    return [
        f"@{a}",
        "D=M",
        f"@{b}",
        "D=D+M",
        f"@{d}",
        "M=D"
    ]