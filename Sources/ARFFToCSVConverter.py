import glob as gb # This builtin module would allow us to select only the file with .arff extension

files = [f for f in gb.glob("*.arff")] # We are using "files" because this selects all the files with that extension

# This function would convert the ARFF file to CSV file
def convert(lines):
    header = ""
    file_content = []
    data = not True
    
    for line in lines:
        if not data:
            if "@attribute" in line:
                attributes = line.split()
                columnName = attributes[attributes.index("@attribute")+1]
                header = header + columnName + ","
            elif "@data" in line:
                data = True
                header = header[:-1]
                header += "\n"
                file_content.append(header)
        else:
            file_content.append(line)
    return file_content
        

for file in files:
    with open(file, "r") as inp:
        lines = inp.readlines()
        output = convert(lines)
        with open("dataset" + ".csv", "w") as out:
            out.writelines(output)
