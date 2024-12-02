
import json
import sys

def get_endpoint_groups(endpoints: list):
    groups = []
    for endpoint in endpoints:
        split = endpoint.split("/")
        if not split[1] in groups:
            groups.append(split[1])
    return groups

def get_endpoints_in_group(all_endpoints: list, group):
    endpoints = []
    for endpoint in all_endpoints:
        split = endpoint.split("/")[2:]
        relative_path = "/".join(split)
        if not relative_path in endpoints:
            endpoints.append(relative_path)
    return endpoints
        

def main():
    if len(sys.argv) < 3:
        print("Incorrect number of parameters provided, try again")
        return
    
    print("Converting swagger to md file")

    source_json_file = sys.argv[1]
    output_file_path = sys.argv[2]

    data = {}
    with open(source_json_file) as file:
        lines = file.read()
        data = json.loads(lines)

    with open(output_file_path, "w") as file:
        file.write(f"# {data["info"]["title"]} API Document - Version: {data["info"]["version"]}\n")
        file.write("###### OpenAPI Documentation Markdown Document\n")
        file.write(f"Open API Version: {data["openapi"]}\n")
        file.write(f"Number of Paths: {len(data["paths"])}\n")
        file.write(f"## API Endpoints:\n")
        # print end points groups, print endpoints nested
        groups = get_endpoint_groups(data["paths"])
        for group in groups:
            file.write(f"* [{group.title()}](#{group})\n")
            endpoints_in_group = get_endpoints_in_group(data["paths"], group)
            for endpoint in endpoints_in_group:
                file.write(f"\t* {endpoint}\n")

        
        # print detailed docs for each group of endpoints
        for group in groups:
            file.write(f"## <a name=\"{group}\"></a> {group.title()}\n")
            file.write(f"Some detailed documentation for this group will go here.\n")

        
    



if __name__ == "__main__":
    main()