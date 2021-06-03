# %%
import flair
import bpemb
from numpy.core.numeric import full
import textract
import os
# %%
bpe = bpemb.BPEmb(lang="sv", dim=50)
# %%

# %%
for root, dirs, files in os.walk('~/Downloads/'):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    for file in files:
        print(file)
# %%

# %%
full_files = []
for subdir, dirs, files in os.walk('/home/londogard/Downloads/Resume&Job_Description/Original_Resumes'):
    for file in files:
        full_files.append(f"{subdir}/{file}")
# %%
full_files[:3]
# %%

# %%
new_files = []
counter = 0
for file in full_files:
    if 'doc' in file or '.exe' in file or 'xlsx' in file:
        continue
    counter += 1
    if counter % 10 == 0:
        print(f"...10 more done (total: {counter}")
    #print(file[-20:])
    text = textract.process(file)
    with open(f"{counter}.txt", 'w') as f:
        f.write(text.decode("utf-8"))
# %%
new_files[:3]
# %%
