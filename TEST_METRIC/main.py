import sacrebleu

def read_lines_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n')
    return lines

gold_filepath = 'TEST_METRIC/gold_translations.txt' 
model_output_filepath = 'TEST_METRIC/5-Miguel-Version-2.txt'  


gold_lines = read_lines_from_file(gold_filepath)
model_output_lines = read_lines_from_file(model_output_filepath)

refs = [gold_lines]
predictions = model_output_lines

chrf = sacrebleu.corpus_chrf(predictions, refs, word_order=2)
print(f"ChrF++ score: {chrf.score}")
