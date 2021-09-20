student_1 = {"name" : "Susan",
             "stream" : "tech",
             "completed_lessons" : 4,
             "completed_lessons_name" : ["variables", "data_types", "dictionaries"]
             }

student_1["completed_lessons_name"].remove("data_types")
print(student_1["completed_lessons_name"])