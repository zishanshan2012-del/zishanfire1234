student_data ={
    "id1": {"name": "John Doe", "class":"v","subject_intergation":["english","math","science"]},
    "id2": {"name": "David Smith", "class":"v","subject_intergation":["english","math","science"]},
    "id3": {"name": "John Doe", "class":"v","subject_intergation":["english","math","science"]},
    "id4": {"name": "anna", "class":"v","subject_intergation":["english","math","science"]}
}
result = {}
seen_keys = []
for student_id,details in student_data.items():
    unique_key = (details["name"], details["class"], tuple(details["subject_intergation"]))
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
for K,v in result.items():
    print(f"{K}: {v}")