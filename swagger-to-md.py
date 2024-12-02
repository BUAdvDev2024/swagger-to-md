
import json
import sys

def get_endpoint_groups(endpoints: list):
    groups = []
    for endpoint in endpoints:
        split = endpoint.split("/")
        if not split[1] in groups:
            groups.append(split[1])
    return groups

def get_endpoint_titles_in_group(all_endpoints: list, group: str):
    endpoints = []
    for endpoint in all_endpoints:
        split = endpoint.split("/")
        if split[1].lower() == group.lower():
            relative_path = "/".join(split[2:])
            if not relative_path in endpoints:
                endpoints.append(relative_path)
    return endpoints

def get_all_endpoint_data_in_group(all_endpoints: list, group: str):
    endpoints_data = []
    for endpoint, data in all_endpoints.items():
        split = endpoint.split("/")
        if split[1].lower() == group.lower():
            relative_path = "/".join(split[2:])
            if data not in endpoints_data:
                endpoints_data.append({"endpoint": endpoint, "data": data})
    return endpoints_data

def get_detailed_group_docs(group_title: str, all_endpoints: list):
    lines = []
    lines.append(f"### <a name=\"{group_title}\"></a> {group_title.title()}")
    # for each endpoint in group print detailed docs
    endpoints_data = get_all_endpoint_data_in_group(all_endpoints, group_title)

    for endpoint_data in endpoints_data:
        title_line = f"#### <a name=\"{endpoint_data["endpoint"]}\"></a>{endpoint_data["endpoint"]}"
        for method in endpoint_data["data"].keys():
            title_line += f" `{method.upper()}` "
        lines.append(title_line)
        # for each method right doc
        

    return lines
        

def main():
    if len(sys.argv) < 3:
        print("Incorrect number of parameters provided, try again")
        return
    
    print("Converting swagger to md file")

    source_json_file = sys.argv[1]
    output_file_path = sys.argv[2]

    data = {}
    with open(source_json_file) as file:
        data = json.loads(file.read())

    lines = []
    lines.append(f"# {data["info"]["title"]} API Document - Version: {data["info"]["version"]}")
    lines.append("###### OpenAPI Documentation Markdown Document")
    lines.append(f"Open API Version: {data["openapi"]}")
    lines.append(f"Number of Paths: {len(data["paths"])}")
    lines.append("## API Endpoints:")
    # print end points groups, print endpoints nested
    groups = get_endpoint_groups(data["paths"])
    for group in groups:
        lines.append(f"* [{group.title()}](#{group})")
        endpoints_in_group = get_endpoint_titles_in_group(data["paths"], group)
        for endpoint in endpoints_in_group:
            lines.append(f"\t* {endpoint}")

    
    # print detailed docs for each group of endpoints
    for group in groups:
        for line in get_detailed_group_docs(group, data["paths"]):
            lines.append(line)

    with open(output_file_path, "w") as file:
        for line in lines:
            file.write(f"{line}\n")
        
    



if __name__ == "__main__":
    main()