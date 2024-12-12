import fileHandlers.layoutHandler as layoutHandler


def translate(inputText:str, inLayoutFilename:str, outLayoutFilename:str) -> str:
    # pick correct layouts
    inLayout = layoutHandler.getLayout(inLayoutFilename)
    outLayout = layoutHandler.getLayout(outLayoutFilename)

    # translate text
    outputText = ""
    for char in inputText:
        # check inLayout for keys
        for case in inLayout.keys():
            if char in inLayout[case]:
                outputText += outLayout[case][inLayout[case].index(char)]
                break
        # if not found - check implicit dict
        else:
            if char in outLayout["implicit"].keys():
                outputText += outLayout["implicit"][char]
            # if not stated anywhere - leave character as it is
            else:
                outputText += char
    
    return outputText


if __name__ == "__main__":
    inp = "Jq? f zr nfr dbikj&"
    out = translate(inp, "qwerty", "йцукен-ua")
    
    print(
        f"{inp = }\n"+
        f"{out = }"
    )