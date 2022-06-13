CONSTRAINTS = {
    "product": {
        "name": {"required": True, "type": str},
        "price": {"required": True, "type": float},
        "description": {"required": True, "type": str},
        "sku": {"required": True, "type": str},
        "active": {"required": True, "type": str},
    }
}


def validate_compulsory_header(entity: str, data: list) -> bool:
    """
    Validate data against constraints
    """
    return set(CONSTRAINTS[entity].keys()) == set(data)


def extract_header(file):
    """
    Extract header from file
    """
    with open(file, "r") as f:
        header = f.readline().strip().split(",")
    return header
