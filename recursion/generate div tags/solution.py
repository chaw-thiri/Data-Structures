# O((2n)!/(n!((n+1)!)))) time and space 
# n = input number 
def generateDivTags(numberOfTags):
    matchedDivTags = []
    generateDivTagsFromPrefix(numberOfTags,numberOfTags,"",matchedDivTags)
    return matchedDivTags
def generateDivTagsFromPrefix(openingTagNeeded,closingTagNeeded, prefix, result):
    if openingTagNeeded > 0:
        newPrefix = prefix + "<div>"
        generateDivTagsFromPrefix(openingTagNeeded-1, closingTagNeeded,newPrefix, result)

    if openingTagNeeded < closingTagNeeded:
        newPrefix = prefix + "</div>"
        generateDivTagsFromPrefix(openingTagNeeded, closingTagNeeded-1, newPrefix, result)

    if closingTagNeeded == 0:
        result.append(prefix)