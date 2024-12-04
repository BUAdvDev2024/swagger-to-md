
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
    lines.append(f"## <a name=\"{group_title}\"></a> {group_title.title()} Endpoints")
    # for each endpoint in group print detailed docs
    endpoints_data = get_all_endpoint_data_in_group(all_endpoints, group_title)

    for endpoint_data in endpoints_data:
        title_line = f"## <a name=\"{endpoint_data["endpoint"]}\"></a>{endpoint_data["endpoint"]}"
        for method in endpoint_data["data"].keys():
            title_line += f" `{method.upper()}` "
        lines.append(title_line)
        

        # for each method right doc
        for method, method_data in endpoint_data["data"].items():
            # doc summary if it exists
            if method_data.get("summary"):
                summary = method_data.get("summary")
                lines.append("#### Summary")
                lines.append(summary)

            if method_data.get("requestBody"):
                requestBody = method_data.get("requestBody")
                content = requestBody["content"]
                # build table of expected content types and schemas
                lines.append("#### Request Body Content")
                lines.append("| Content Type | Schema |")
                lines.append("|--------------|--------|")
                schemas = []
                for schema_data in content.values():
                    schema_ref = schema_data["schema"]["$ref"].split("/")[-1]
                    schema_tag = f"[{schema_ref}](#{schema_ref})"
                    if not schema_tag in schemas:
                        schemas.append(schema_tag)
                lines.append(f"| `{"` `".join(content.keys())}` | {" ".join(schemas)}")                    

            if method_data.get("parameters"):
                params = method_data.get("parameters")
                lines.append("#### Parameters")
                # create table of parameters
                lines.append("| Name | Data Type |")
                lines.append("|------|--------|")
                for param in params:
                    lines.append(f"| {param["name"]} | `{"` `".join(param["schema"].values())}` |")
            elif method == "get":
                lines.append("#### Parameters")
                lines.append("No parameters")
            if method_data.get("responses"):
                responses = method_data.get("responses")
                lines.append("#### Responses")
                lines.append("| Response | Description |")
                lines.append("|----------|-------------|")
                for response, response_data in responses.items():
                    lines.append(f"| {response} | {response_data["description"]}")
            lines.append("")
    return lines
        

def get_detailed_schema_docs(schema_name, schema_data):
    lines = []
    lines.append(f"## <a name=\"{schema_name}\"></a>{schema_name} `{schema_data["type"]}`")
    lines.append("### Properties")
    lines.append("| Property Name | Type | Format | Nullable? |")
    lines.append("|---------------|------|--------|----------|")
    for property_name, property_data in schema_data["properties"].items():
        lines.append(f"| {property_name} | {property_data["type"]} | {property_data.get("format") or "--"} | { "nullable" if property_data.get("nullable") else "--"} |")
    return lines

def main():
    if len(sys.argv) < 4:
        print("Incorrect number of parameters provided, try again")
        return
    
    print("Converting swagger to md file")

    api_name = sys.argv[1]
    source_json_file = sys.argv[2]
    output_file_path = sys.argv[3]

    # read source swagger.json file
    data = {}
    with open(source_json_file) as file:
        data = json.loads(file.read())

    lines = []
    # print header
    lines.append(f"# {api_name}")
    lines.append(f"###### API Version: {data["info"]["version"]} - Open API Version: {data["openapi"]} - Paths: ({len(data["paths"])}) - Schema ({len(data["components"]["schemas"].keys())})")
    
    # print glossary for endpoints grouped by route
    lines.append("## API Endpoints")
    groups = get_endpoint_groups(data["paths"])
    for group in groups:
        lines.append(f"* [{group.title()}](#{group})")
        endpoints_in_group = get_all_endpoint_data_in_group(data["paths"], group)
        for endpoint_data in endpoints_in_group:
            relative_endpoint = endpoint_data["endpoint"].split("/")[-1]
            lines.append(f"\t* [{relative_endpoint}](#{endpoint_data["endpoint"]})")
    # print glossary for schemas
    lines.append("## Schemas")
    for schema_name in data["components"]["schemas"].keys():
        lines.append(f"* [{schema_name.title()}](#{schema_name})")
        

    
    # print detailed docs for each group of endpoints
    for group in groups:
        for line in get_detailed_group_docs(group, data["paths"]):
            lines.append(line)

    # print detailed docs for each schema
    if data.get("components"):
        components = data.get("components")
        lines.append("## Schemas")
        if components.get("schemas"):
            schemas = components.get("schemas")
            # get lines for schema documentation
            for schema_name, schema_data in schemas.items():
                for line in get_detailed_schema_docs(schema_name, schema_data):
                    lines.append(line)
        else:
            lines.append("No schemas")

    # add watermark
    lines.append("")
    lines.append("###### API doc created by swagger-to-md.py")        

    # create file and write lines to it
    with open(output_file_path, "w") as file:
        for line in lines:
            file.write(f"{line}\n")
        
    



if __name__ == "__main__":
    main()