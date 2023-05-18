def main():
    with open('assembler.txt') as file:
        lines = [line.rstrip() for line in file]
    registers={}
    for line in lines:
        if line.startswith("MV"):
            cmd, rest = line.split()
            reg,raw_value=rest.split(',')
            value=int(raw_value[1:])
            registers[reg]=value
            print("MV",reg, value)
        elif line.startswith("ADD"):
            cmd, rest = line.split()
            reg1,reg2=rest.split(',')
            if reg2.startswith('#'):
                reg2=int(reg2[1:])
                value=registers.get(reg1)
                if value:
                    sum=value+reg2
                    registers[reg1]=sum
                else:
                    print(f"{reg1} doesn't exist in memory.")
            else:
                value_reg1=registers.get(reg1)
                value_reg2=registers.get(reg2)
                if value_reg1 and value_reg2:
                    sum=value_reg1+value_reg2
                    registers[reg1]=sum
                else:
                    if not value_reg1:
                        print(f"{reg1} doesn't exist in memory.")
                    if not value_reg2:
                        print(f"{reg2} doesn't exist in memory.")
            print("ADD",reg1, reg2)
        elif line.startswith("SHOW"):
            reg = line.split()[1]
            value=registers.get(reg,f"{reg} doesn't exist in memory.")
            print("SHOW",reg,value)
                
            

if __name__ == "__main__":
    main()