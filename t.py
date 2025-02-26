from src.utlis import parse_refined_text
from src.LLM import llm, speech_reco

text = """1. Refine the Text: (MUST be written)
        The patient is a 32-year-old married male who has been a smoker for 10 years. He does not consume alcohol or caffeine. His mother has diabetes, and his father has no known diseases. His sister suffers from an anxiety disorder, and there are no known diseases for his grandparents or children. The patient suffers from chronic Factor VIII deficiency. He requires the following medications: codeine, morphine, and Factor VIII medication. The patient has a mild allergy to milk. He was brought to the hospital due to excessive knee pain, trouble sleeping, and difficulties with physical activities. He reports no sexual problems.

        2. Extract Patient Features: (MUST be written)
        ```json
        {
            "Diagnosis": "Chronic Factor VIII deficiency",
            "ICD-10 Code": "D66",
            "Gender": "Male",
            "Age": 32,
            "Smoker": true,
            "Medical History": {
                "Mother": "Diabetes",
                "Father": "No known diseases",
                "Sister": "Anxiety disorder",
                "Grandparents": "No known diseases",
                "Children": "No known diseases"
            },
            "Medication Orders": ["Codeine", "Morphine", "Factor VIII medication"],
            "Vital Signs": null,
            "Signs and Symptoms": ["Excessive knee pain", "Trouble sleeping", "Difficulties with physical activities"]
        }
        ```"""

re_text, json_data = parse_refined_text(text)
print(re_text, json_data)