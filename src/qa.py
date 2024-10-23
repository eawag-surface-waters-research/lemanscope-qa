def quality_assurance(data):
    output = []
    for obs in data:
        obs["water"]["sd_depth"] = verify_secchi(obs["water"]["sd_depth"])
        obs["water"]["fu_processed"] = verify_fu(obs["water"]["fu_processed"])
        obs["water"]["fu_value"] = verify_fu(obs["water"]["fu_value"])
        if any(obs["water"][key] is not None for key in ["sd_depth", "fu_processed", "fu_value"]):
            output.append(obs)
    return output

def verify_secchi(value, min_value=0, max_value=15):
    value = verify_min_max(value, min_value, max_value)
    return value

def verify_fu(value, min_value=1, max_value=22):
    value = verify_min_max(value, min_value, max_value)
    return value

def verify_min_max(value, min_value, max_value):
    try:
        value = float(value)
        if value <= min_value or value >= max_value:
            raise ValueError("Value out of bounds")
        return value
    except:
        return None
