from src.LLM import llm, speech_reco
import time
from src.utlis import parse_refined_text

audio = "/Users/muhammedamr/Desktop/AHBS/Refined_whisper/waves/wave2.m4a"
# start_speech = time.time()
text = speech_reco(audio)
# end_speech = time.time()
# speech_time_ms = (end_speech - start_speech) * 1000

# start_llm = time.time()
refined_text = llm(text)
# print(refined_text)
# end_llm = time.time()
# llm_time_ms = (end_llm - start_llm) * 1000

# Calculate total time
# total_time_ms = speech_time_ms + llm_time_ms
parsed_text, json_data, reasoning = parse_refined_text(refined_text)
print(parsed_text, json_data, reasoning)
# # Print results
# print("Speech recognition time: {:.2f} ms".format(speech_time_ms))
# print("LLM processing time: {:.2f} ms".format(llm_time_ms))
# print("Total processing time: {:.2f} ms".format(total_time_ms))


print("final output:  ",refined_text)