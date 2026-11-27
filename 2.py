def analyze_students_subjects(s1: set, s2: set) -> dict:
    common = s1 & s2
    only_1 = s1 - s2
    only_2 = s2 - s1
    total = len(s1 | s2)
    return {
        "umumiy": list(common),
        "faqat_1": list(only_1),
        "faqat_2": list(only_2),
        "umumiy_soni": total,
    }
if __name__ == "__main__":
    s1 = {"Math", "Physics", "IT", "English"}
    s2 = {"IT", "Biology", "Math"}
    print(analyze_students_subjects(s1, s2))
