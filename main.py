base_struct = '''
#include <iostream>
using namespace std;

int main(){
'''

ending = '''
}
'''

def replace_spec_symb(line):
    #But if it is a text in string ""? PATCH IT
    line = line.replace("**", "*");#It will be compiled; but in real we have to replace it to pow function
    return line

tab = "    "
with open("code.py", "r") as file:
    code = file.readlines()

final_code = ""
print(code)
for line in code:
    line = line.replace("\n", "")
    line = replace_spec_symb(line)
    if line.startswith("print"):
        #if line.count("'") % 2 == 0 or line.count('"') % 2 == 0: #String
        args = line.replace("print(", "")[:-1]
        final_code += f"{tab}cout << {args} << endl;\n" 
    elif "=" in line:
        raw = line.split("=")
        variable = raw[0]
        value = raw[1][1::]
        #Predict value type
        #print(variable)
        #print(len(value))
        if value.isnumeric():
            final_code += f"{tab}int {variable} = {value};\n"
        else:
            final_code += f"{tab}string {variable} = {value};\n"
        
with open("out_cpp.cpp", "w") as file:
    print(base_struct + final_code + ending, file=file)        
