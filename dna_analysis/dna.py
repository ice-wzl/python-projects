sample = ['GTA','GGG','CAC']
def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, 'r') as f:
    for line in f:
      dna_data += line
      return dna_data
def dna_condons(dna):
  condons = []
  for i in range(0, len(dna), 3):
    if (i + 3) < len(dna): 
      condons.append(dna[i:i + 3])
  return condons

def match_dna(dna):
  matches = 0
  for condon in dna:
    if condon in sample:
      matches += 1 
  return matches 

def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)  
  condons = dna_condons(dna_data)
  num_matches = match_dna(condons)
  if num_matches >= 3:
    print "Investigation Continuing. Matches: %d" % (num_matches)
  else:
    print "Suspect Free. Matches: %d" % (num_matches)

is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')

