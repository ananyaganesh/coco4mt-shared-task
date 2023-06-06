import sys
import jsonlines
from pathlib import Path

"""
Takes in indices, name of target lang, and selects corresponding sentences from source (English) and target. 
Generates JSON-lines files with English--tgt_lang sentence pairs as required by mBART.
"""

indices_path = sys.argv[1]
tgt_lang = sys.argv[2]

output_file_path = (Path('json_formatted_files') / ('eng_' + tgt_lang)).with_suffix('.jsonlines')

indices = [int(i) for i in open(indices_path).read().split('\n')]
src_lines = open('hr_dataset/eng/train.txt').read().strip().split('\n')
tgt_lines = open(Path('lr_dataset') / tgt_lang / 'train.txt').read().strip().split('\n') 

assert len(src_lines) == len(tgt_lines)

src_selections = [src_lines[i] for i in indices]
tgt_selections = [tgt_lines[i] for i in indices]

with jsonlines.open(output_file_path, mode='w') as outf:
  for src, tgt in zip(src_selections, tgt_selections):
    if len(src.strip()) > 0:
      line = {"translation": {'eng': src, tgt_lang: tgt}}
      outf.write(line)




