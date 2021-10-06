a = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", 
"HeightCm": 167, "WeightKg": 82}]

def BMI_Alteration(x):
    for i in x:
        BMI = i["HeightCm"]/i["WeightKg"]
        i["BMI VALUE"]= f" {BMI}KG/M2"
        if BMI<18.4:
            i["BMI Category"] = "Underweight"
            i["Health risk"] = "Malnutrition risk"
        elif 18.5 <BMI> 24.9:
            i["BMI Category"] = "Normal weight"
            i["Health risk"] = "Low risk"
        elif 25<BMI>29.9:
            i["BMI Category"] = "Overweight"
            i["Health risk"] = "Enhanced risk"
        elif 30<BMI>34.9:
            i["BMI Category"] = "Moderately obese"
            i["Health risk"] = "Medium risk"
        elif 35<BMI>39.9:
            i["BMI Category"] = "Moderately obese"
            i["Health risk"] = "Medium risk"
        elif BMI>40:
            i["BMI Category"] = "Very severely obese"
            i["Health risk"] = "Very high risk"
    print(x)
    return x

BMI_Alteration(a)