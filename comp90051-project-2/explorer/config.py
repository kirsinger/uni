PROJ2_MAPPINGS = {

    ("Community", "community"):
        {
            "Community Name":("name", "string"),
            "Region":("region", "string")
        },

    ("Geography", "geography"):
        {
            "Map reference":("map_ref", "int"),
            "Grid reference":("grid_ref", "string"),
            "Location":("location", "string"),
            "Population Density":("population_density", "float"),
            "Travel time to GPO (minutes)":("time_to_gpo_min", "int"),
            "Distance to GPO (km)":("dist_to_gpo_km", "int"),
            "LGA":("local_govt_area", "string"),
            "Primary Care Partnership":("primary_care_partnership", "string"),
            "Medicare Local":("medicare_local", "string"),
            "Area (km^2)":("area_square_km", "float"),
            "ARIA+ (min)":("aria_score_min", "float"),
            "ARIA+ (max)":("aria_score_max", "float"),
            "ARIA+ (avg)":("aria_score_avg", "float"),
            "ABS remoteness category":("abs_remoteness_category", "string"),
            "DHS Area":("dhs_area", "string")
        },

    ("Land Use", "land_use"):
        {
            "Commercial (km^2)":("commercial_square_km", "float"),
            "Commercial (%)":("commercial_pct", "float"),
            "Industrial (km^2)":("industrial_square_km", "float"),
            "Industrial (%)":("industrial_pct", "float"),
            "Residential (km^2)":("residential_square_km", "float"),
            "Residential (%)":("residential_pct", "float"),
            "Rural (km^2)":("rural_sqaure_km", "float"),
            "Rural (%)":("rural_pct", "float"),
            "Other (km^2)":("other_square_km", "float"),
            "Other (%)":("other_pct", "float")
        },

    ("2012 population", "2012_population"):
        {
            "2012 ERP age 0-4, persons":("age_0_4_persons", "int"),
            "2012 ERP age 0-4, %":("age_0_4_pct", "float"),
            "2012 ERP age 5-9, persons":("age_5_9_persons", "int"),
            "2012 ERP age 5-9, %":("age_5_9_pct", "float"),
            "2012 ERP age 10-14, persons":("age_10_14_persons", "int"),
            "2012 ERP age 10-14, %":("age_10_14_pct", "float"),
            "2012 ERP age 15-19, persons":("age_15_19_persons", "int"),
            "2012 ERP age 15-19, %":("age_15_19_pct", "float"),
            "2012 ERP age 20-24, persons":("age_20_24_persons", "int"),
            "2012 ERP age 20-24, %":("age_20_24_pct", "float"),
            "2012 ERP age 25-44, persons":("age_25_44_persons", "int"),
            "2012 ERP age 25-44, %":("age_25_44_pct", "float"),
            "2012 ERP age 45-64, persons":("age_45_64_persons", "int"),
            "2012 ERP age 45-64, %":("age_45_64_pct", "float"),
            "2012 ERP age 65-69, persons":("age_65_69_persons", "int"),
            "2012 ERP age 65-69, %":("age_65_69_pct", "float"),
            "2012 ERP age 70-74, persons":("age_70_74_persons", "int"),
            "2012 ERP age 70-74, %":("age_70_74_pct", "float"),
            "2012 ERP age 75-79, persons":("age_75_79_persons", "int"),
            "2012 ERP age 75-79, %":("age_75_79_pct", "float"),
            "2012 ERP age 80-84, persons":("age_80_84_persons", "int"),
            "2012 ERP age 80-84, %":("age_80_84_pct", "float"),
            "2012 ERP age 85+, persons":("age_85_plus_persons", "int"),
            "2012 ERP age 85+, %":("age_85_plus_pct", "float"),
            "2012 ERP, total":("total_persons", "int")
        },

    #2007 Population
    ("2007 population", "2007_population"):
        {
            "2007 ERP age 0-4, persons":("age_0_4_persons", "int"),
            "2007 ERP age 0-4, %":("age_0_4_pct", "float"),
            "2007 ERP age 5-9, persons":("age_5_9_persons", "int"),
            "2007 ERP age 5-9, %":("age_5_9_pct", "float"),
            "2007 ERP age 10-14, persons":("age_10_14_persons", "int"),
            "2007 ERP age 10-14, %":("age_10_14_pct", "float"),
            "2007 ERP age 15-19, persons":("age_15_19_persons", "int"),
            "2007 ERP age 15-19, %":("age_15_19_pct", "float"),
            "2007 ERP age 20-24, persons":("age_20_24_persons", "int"),
            "2007 ERP age 20-24, %":("age_20_24_pct", "float"),
            "2007 ERP age 25-44, persons":("age_25_44_persons", "int"),
            "2007 ERP age 25-44, %":("age_25_44_pct", "float"),
            "2007 ERP age 45-64, persons":("age_45_64_persons", "int"),
            "2007 ERP age 45-64, %":("age_45_64_pct", "float"),
            "2007 ERP age 65-69, persons":("age_65_69_persons", "int"),
            "2007 ERP age 65-69, %":("age_65_69_pct", "float"),
            "2007 ERP age 70-74, persons":("age_70_74_persons", "int"),
            "2007 ERP age 70-74, %":("age_70_74_pct", "float"),
            "2007 ERP age 75-79, persons":("age_75_79_persons", "int"),
            "2007 ERP age 75-79, %":("age_75_79_pct", "float"),
            "2007 ERP age 80-84, persons":("age_80_84_persons", "int"),
            "2007 ERP age 80-84, %":("age_80_84_pct", "float"),
            "2007 ERP age 85+, persons":("age_85_plus_persons", "int"),
            "2007 ERP age 85+, %":("age_85_plus_pct", "float"),
            "2007 ERP, total":("total_persons", "int")
        },

    ("2007-2012 population change", "2007_2012_population_change"):
        {
            "% change, 2007-2012, age 0-4":("pct_age_0_4", "float"),
            "% change, 2007-2012, age 5-9":("pct_age_5_9", "float"),
            "% change, 2007-2012, age 10-14":("pct_age_10_14", "float"),
            "% change, 2007-2012, age 15-19":("pct_age_15_19", "float"),
            "% change, 2007-2012, age 20-24":("pct_age_20_24", "float"),
            "% change, 2007-2012, age 25-44":("pct_age_25_44", "float"),
            "% change, 2007-2012, age 45-64":("pct_45_64", "float"),
            "% change, 2007-2012, age 65-69":("pct_65_69", "float"),
            "% change, 2007-2012, age 70-74":("pct_age_70_74", "float"),
            "% change, 2007-2012, age 75-79":("pct_age_75_79", "float"),
            "% change, 2007-2012, age 80-84":("pct_age_80_84", "float"),
            "% change, 2007-2012, age 85+":("pct_age_85_plus", "float"),
            "% change, 2007-2012, total":("pct_total", "float")
        },

    ("Services", "services"):
        {
            "Public Hospitals":("public_hospitals", "int"),
            "Private Hospitals":("private_hospitals", "int"),
            "Community Health Centres":("community_health_centres", "int"),
            "Bush Nursing Centres":("bush_nursing_cetres", "int"),
            "Allied Health":("allied_health_services", "int"),
            "Alternative Health":("alternative_health_services", "int"),
            "Child Protection and Family":("child_protection_and_family_services", "int"),
            "Dental":("dental_services", "int"),
            "Disability":("disability_services", "int"),
            "General Practice":("general_practices", "int"),
            "Homelessness":("homelessness_services", "int"),
            "Mental Health":("mental_health_services", "int"),
            "Pharmacies":("pharmacies", "int"),
            "Aged Care (High Care)":("aged_care_services_high", "int"),
            "Aged Care (Low Care)":("aged_care_services_low", "int"),
            "Aged Care (SRS)":("aged_care_srs", "int"),
            "Kinder and/or Childcare":("childcare_services", "int"),
            "Primary Schools":("primary_schools", "int"),
            "Secondary Schools":("secondary_schools", "int"),
            "P12 Schools":("p12_schools", "int"),
            "Other Schools":("other_schools", "int"),
            "Centrelink Offices":("centrelink_offices", "int"),
            "Medicare Offices":("medicare_offices", "int"),
            "Medicare Access Points":("medicare_access_points", "int")
        },

    ("Socio-demographic", "socio_demographic"):
        {
            "Number of Households":("households", "int"),
            "Average persons per household":("avg_persons_per_household", "float"),
            "Occupied private dwellings":("occupied_private_dwellings", "int"),
            "Occupied private dwellings, %":("pct_occupied_private_dwellings", "float"),
            "Population in non-private dwellings":("persons_in_non_private_dwellings", "int"),
            "Public Housing Dwellings":("public_housing_dwellings", "int"),
            "% dwellings which are public housing":("pct_public_housing_dwellings", "float"),
            "Dwellings with no motor vehicle":("dwellings_no_car", "int"),
            "Dwellings with no motor vehicle, %":("pct_dwellings_no_car", "float"),
            "Dwellings with no internet":("dwellings_no_internet", "int"),
            "Dwellings with no internet, %":("pct_dwellings_no_internet", "float"),
            "Equivalent household income <$600/week":("household_income_less_600_week", "int"),
            "Equivalent household income <$600/week, %":("pct_household_income_less_600_week", "float"),
            "Personal income <$400/week, persons":("personal_income_less_400_week", "int"),
            "Personal income <$400/week, %":("pct_personal_income_less_400_week", "float"),
            "Number of families":("num_families", "int"),
            "Female-headed lone parent families":("female_headed_lone_parent_families", "int"),
            "Female-headed lone parent families, %":("pct_female_headed_lone_parent_families", "float"),
            "Male-headed lone parent families":("male_headed_lone_parent_families", "int"),
            "Male-headed lone parent families, %":("pct_male_headed_lone_parent_families", "float"),
            "% residing near PT":("pct_population_near_pt", "float"),
            "IRSD (min)":("isrd_score_min", "int"),
            "IRSD (max)":("isrd_score_max", "int"),
            "IRSD (avg)":("isrd_score_avg", "int"),
            "Primary school students":("primary_school_students", "int"),
            "Secondary school students":("secondary_school_students", "int"),
            "TAFE students":("tafe_students", "int"),
            "University students":("uni_students", "int"),
            "Holds degree or higher, persons":("persons_with_higher_degree", "int"),
            "Holds degree or higher, %":("pct_persons_with_higher_degree", "float"),
            "Did not complete year 12, persons":("persons_dnc_year_12", "int"),
            "Did not complete year 12, %":("pct_persons_dnc_year_12", "float"),
            "Unemployed, persons":("unemployed", "int"),
            "Unemployed, %":("pct_unemployed", "float"),
            "Volunteers, persons":("volunteers", "int"),
            "Volunteers, %":("pct_volunteers", "float"),
            "Requires assistance with core activities, persons":("persons_req_assist_with_core_activities", "int"),
            "Requires assistance with core activities, %":("pct_persons_req_assist_with_core_activities", "float"),
            "Aged 75+ and lives alone, persons":("persons_aged_75_plus_living_alone", "int"),
            "Aged 75+ and lives alone, %":("pct_persons_aged_75_plus_living_alone", "float"),
            "Unpaid carer to person with disability, persons":("unpaid_carers_disability", "int"),
            "Unpaid carer to person with disability, %":("pct_unpaid_carers_disability", "float"),
            "Unpaid carer of children, persons":("unpaid_carers_children", "int"),
            "Unpaid carer of children, %":("pct_unpaid_carers_children", "float"),
            "Top industry":("top_industry", "string"),
            "Top industry, %":("pct_top_industry", "float"),
            "2nd top industry - persons":("second_top_industry", "string"),
            "2nd top industry, %":("pct_second_top_industry", "float"),
            "3rd top industry - persons":("third_top_industry", "string"),
            "3rd top industry, %":("pct_third_top_industry", "float"),
            "Top occupation":("top_occupation", "string"),
            "Top occupation, %":("pct_top_occupation", "float"),
            "2nd top occupation - persons":("second_top_occupation", "string"),
            "2nd top occupation, %":("pct_second_top_occupation", "float"),
            "3rd top occupation - persons":("third_top_occupation", "string"),
            "3rd top occupation, %":("pct_third_top_occupation", "float")
        },

    ("Diversity", "diversity"):
        {
            "Aboriginal or Torres Strait Islander, persons":("aboriginal_tsi_persons", "int"),
            "Aboriginal or Torres Strait Islander, %":("pct_aboriginal_tsi_persons", "float"),
            "Born overseas, persons":("born_overseas", "int"),
            "Born overseas, %":("pct_born_overseas", "float"),
            "Born in non-English speaking country, persons":("born_non_english_speaking_country", "int"),
            "Born in non-English speaking country, %":("pct_born_non_english_speaking_country", "float"),
            "Speaks LOTE at home, persons":("speak_lote_at_home", "int"),
            "Speaks LOTE at home, %":("pct_speak_lote_at_home", "float"),
            "Poor English proficiency, persons":("persons_poor_english", "int"),
            "Poor English proficiency, %":("pct_persons_poor_english", "float"),
            "Top country of birth":("top_country_of_birth_name", "string"),
            "Top country of birth, persons":("top_country_of_birth", "int"),
            "Top country of birth, %":("pct_top_country_of_birth", "float"),
            "2nd top country of birth":("second_top_country_of_birth_name", "string"),
            "2nd top country of birth, persons":("second_top_country_of_birth", "int"),
            "2nd top country of birth, %":("pct_second_top_country_of_birth", "float"),
            "3rd top country of birth":("third_top_country_of_birth_name", "string"),
            "3rd top country of birth, persons":("third_top_country_of_birth", "int"),
            "3rd top country of birth, %":("pct_third_top_country_of_birth", "float"),
            "4th top country of birth":("fourth_top_country_of_birth_name", "string"),
            "4th top country of birth, persons":("fourth_top_country_of_birth", "int"),
            "4th top country of birth, %":("pct_fourth_top_country_of_birth", "float"),
            "5th top country of birth":("fifth_top_country_of_birth_name", "string"),
            "5th top country of birth, persons":("fifth_top_country_of_birth", "int"),
            "5th top country of birth, %":("pct_fifth_top_country_of_birth", "float"),
            "Top language spoken":("top_language_spoken_name", "string"),
            "Top language spoken, persons":("top_language_spoken", "int"),
            "Top language spoken, %":("pct_top_language_spoken", "float"),
            "2nd top language spoken":("second_top_language_spoken_name", "string"),
            "2nd top language spoken, persons":("second_top_language_spoken", "int"),
            "2nd top language spoken, %":("pct_second_top_language_spoken", "float"),
            "3rd top language spoken":("third_top_language_spoken_name", "string"),
            "3rd top language spoken, persons":("third_top_language_spoken", "int"),
            "3rd top language spoken, %":("pct_third_top_language_spoken", "float"),
            "4th top language spoken":("fourth_top_language_spoken_name", "string"),
            "4th top language spoken, persons":("fourth_top_language_spoken", "int"),
            "4th top language spoken, %":("pct_fourth_top_language_spoken", "float"),
            "5th top language spoken":("fifth_top_language_spoken_name", "string"),
            "5th top language spoken, persons":("fifth_top_language_spoken", "int"),
            "5th top language spoken, %":("pct_fifth_top_language_spoken", "float")
        },

    ("Hospital", "hospital"):
        {
            "Public hospital separations, 2012-13":("num_public_hospital_separations_2012_2013", "int"),
            "Nearest Public Hospital":("nearest_public_hospital", "string"),
            "Travel time to nearest public hospital":("time_to_nearest_public_hospital", "int"),
            "Distance to nearest public hospital":("distance_to_nearest_public_hospital", "int"),
            "Obstetric type separations, 2012-13":("obstetric_separations_2012_2013", "int"),
            "Nearest public hospital with maternity services":("nearest_public_hospital_with_maternity_services", "string"),
            "Time to nearest public hospital with maternity services":("time_to_nearest_public_hospital_with_maternity_services", "int"),
            "Distance to nearest public hospital with maternity services":("distance_to_nearest_public_hospital_with_maternity_services", "int"),
            "Presentations to emergency departments, 2012-13":("emergency_dept_presentations_2012_2013", "int"),
            "Nearest public hospital with emergency department":("nearest_public_hospital_with_emergency_dept", "string"),
            "Travel time to nearest public hospital with emergency department":("time_to_nearest_public_hospital_with_emergency_dept", "int"),
            "Distance to nearest public hospital with emergency department":("distance_to_nearest_public_hospital_with_emergency_dept", "int"),
            "Presentations to emergency departments due to injury":("num_emergency_dept_presentations_injury", "int"),
            "Presentations to emergency departments due to injury, %":("pct_emergency_dept_presentations_injury", "float"),
            "Category 4 & 5 emergency department presentations":("num_emergency_dept_presentations_cat_4_5", "int"),
            "Category 4 & 5 emergency department presentations, %":("pct_emergency_dept_presentations_cat_4_5", "float")
        }
}
