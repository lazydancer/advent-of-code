def part1():
    with open('input', 'r') as f:
        initial_str, logic_str = f.read().split('\n\n') 
        values = {x.split(": ")[0]: int(x.split(": ")[1]) for x in initial_str.split('\n')}
        logic = [{
            "action": x.split()[1],
            "a": x.split()[0],
            "b": x.split()[2],
            "c": x.split()[4],
        } for x in logic_str.split('\n')]

    
    done = False
    while not done:
        print('hi')
        done = True

        for l in logic:
            if l["a"] in values.keys() and l["b"] in values.keys() and l["c"] not in values.keys():
                match l["action"]:
                    case "OR":
                        values[l["c"]] = values[l["a"]] | values[l["b"]]
                    case "AND":
                        values[l["c"]] = values[l["a"]] & values[l["b"]]
                    case "XOR":
                        values[l["c"]] = values[l["a"]] ^ values[l["b"]]
                
                done = False


    result = 0
    for i in range(100):
        z_index = ("z" + str(i).zfill(2))
        if z_index not in values.keys():
            break

        result += values[z_index] * 2**i

    print(result)


part1()