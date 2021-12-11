count_to_digit = {
    2: 1,
    3: 7,
    4: 4,
    # 5: [2, 3, 5],
    # 6: [0, 6, 9],
    7: 8
}

def contains(small, big):
    for letter in small:
        if letter not in big:
            return False
    return True

def matches(small, big):
    res = 0
    for letter in small:
        if letter in big:
            res += 1
    return res

if __name__ == "__main__":
    with open("./08.in") as f:
        lines = list(map(lambda line: line.strip().split(" | "), f.readlines()))

        count = 0
        outputs = []
        for signal, output in lines:
            signal = list(map(lambda x: "".join(sorted(x)), signal.split(" ")))
            output = list(map(lambda x: "".join(sorted(x)), output.split(" ")))

            for value in output:
                if len(value) in count_to_digit:
                    count += 1
            
            sig_to_digit = dict()
            for s in signal:
                if len(s) in count_to_digit:
                    sig_to_digit[s] = count_to_digit[len(s)]
            
            signal_seven, _ = next(filter(lambda x: x[1] == 7, sig_to_digit.items()))
            signal_four, _ = next(filter(lambda x: x[1] == 4, sig_to_digit.items()))
            for s in signal:
                if s not in sig_to_digit:
                    if len(s) == 5:
                        if contains(signal_seven, s):
                            sig_to_digit[s] = 3
                        elif matches(signal_four, s) == 3:
                            sig_to_digit[s] = 5
                        else:
                            sig_to_digit[s] = 2
                    elif len(s) == 6:
                        if contains(signal_four, s):
                            sig_to_digit[s] = 9
                        elif contains(signal_seven, s):
                            sig_to_digit[s] = 0
                        else:
                            sig_to_digit[s] = 6
            
            res = ""
            for o in output:
                res += str(sig_to_digit[o])
            outputs.append(int(res))

        print(f"Count: {count}")
        print(f"Sum of outputs: {sum(outputs)}")
