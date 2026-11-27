def analyze_students_subjects(s1: set, s2: set) -> dict:
    return {
        "umumiy": sorted(s1 & s2),
        "faqat_1": sorted(s1 - s2),
        "faqat_2": sorted(s2 - s1),
        "umumiy_soni": len(s1 | s2)
    }

if __name__ == "__main__":
	s1 = {"Math", "Physics", "IT", "English"}
	s2 = {"IT", "Biology", "Math"}
	print(analyze_students_subjects(s1, s2))
