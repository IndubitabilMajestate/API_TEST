def queryGenerator(field_names, field_values):
    query = "?"
    if isinstance(field_names, list) and isinstance(field_values, list):
        if len(field_names) != len(field_values):
            raise ValueError(
                f"Lists dont match in size! Field name list size: {len(field_names)}, field values list size: {len(field_values)}")
        for index in range(len(field_names)):
            query += f"{field_names[index]}={field_values[index]}&"
        query = query[:-1]
    elif isinstance(field_names, str) and not isinstance(field_values, list):
        query += f"{field_names}={field_values}"
    else:
        raise ValueError("Both need to be lists of same size or single element objects/types.")
    return query