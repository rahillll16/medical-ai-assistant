import json

DATA_PATH = "data/MOCK_DATA.json"


def find_best_hospital(city,department,excluded_prices=None):
    print (f"Finding best hospital in {city} for {department}")
    with open("MOCK_DATA.json", "r", encoding="utf-8") as f:
        hospitals = json.load(f)
    
    #Filter by city & department
    filtered = []
    for h in hospitals:
        if h["city"].lower() == city.lower() and h["departments"].lower() == department.lower():
            if h["price_level"] not in excluded_prices:
                filtered.append(h)
                
    if not filtered:
        return {"found":False}
    
    # Sort by rating (descending)
    filtered.sort(key=lambda x: x["rating"], reverse=True)
    
    h = filtered[0]
    
    return {
        "found": True,
        "hospital_name": h["hospital_name"],
        "city": h["city"],
        "rating": h["rating"],
        "price_level": h["price_level"],
        "phone": h["contact_phone"],
        "email": h["contact_email"]
    }