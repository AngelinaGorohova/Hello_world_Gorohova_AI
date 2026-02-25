donor_phenotype = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
patient_phenotype = input("Введите фенотип группы крови пациента (I, II, III, IV): ").strip().upper()

if donor_phenotype == patient_phenotype or donor_phenotype == "I":
    print("Переливание крови возможно!")
else:
    print("Переливание крови невозможно.")