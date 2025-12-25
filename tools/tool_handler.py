import json
from tools.hospital_finder import find_best_hospital

def handling_tool_calls(message):
    
    tool_messages=[]
    
    for tool_call in message.tool_calls:
        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        
        if tool_name == "find_best_hospital":
            result = find_best_hospital(
                city = args["city"],
                department = args["department"],
                excluded_prices = args["excluded_prices"]
            )
            
            tool_messages.append({
                "role":"tool",
                "content":json.dumps(result),
                "tool_call_id":tool_call.id
            })
            
    return tool_messages
