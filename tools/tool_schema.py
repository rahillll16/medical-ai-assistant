best_hospital_finder = {
    "name" : "find_best_hospital",
    "description" : "Find best hospital by city, department and budget",
    "parameters" : {
        "type" :"object",
        "properties": {
            "city":{"type":"string"},
            "department" : {"type":"string"},
            "excluded_prices":{
                "type":"array",
                "items" : {"type":"string"}
            }
        },
        "required": ["city", "department", "excluded_prices"]
    }
}