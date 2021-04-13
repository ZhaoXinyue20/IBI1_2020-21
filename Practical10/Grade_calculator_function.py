def grade_calculator(name,portfolio_grade, poster_grade, exam_grade):
    """
    Input:(1) Student name;(str)
          (2) Student grade for the code portfolio;(int)
          (3) Student grade for the poster presentation;(int)
          (4) Student grade in the final exam.(int)
          
    return: name, grade
    """
    grade = portfolio_grade*0.4 + poster_grade*0.3 + exam_grade*0.3
    return name, grade
# test
test = grade_calculator("Anna Smith",95,90,88)
student_name = test[0]
final_grade = test[1]
print("The final grade of "+ str(student_name) +" is "+str(final_grade))
