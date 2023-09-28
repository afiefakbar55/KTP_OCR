#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def extract_data(items):

    new_data = []
    new_items = []
    
    for i in items:
        if i == 'status' or i == 'perkawinan':
            i = 'status perkawinan'
            new_items.append(i)

        elif i == 'gol' or i == 'darah':
            i = 'gol. darah'
            new_items.append(i)

        elif i == 'tempat' or i == 'tanggal' or i == 'lahir':
            i = 'tempat tanggal lahir'
            new_items.append(i)

        elif i == 'jenis' or i == 'kelamin':
            i = 'jenis kelamin'
            new_items.append(i)

        else:
            new_items.append(i)

    for i in new_items:
        if i not in new_data:
            new_data.append(i)
        
    return new_data
    
def mapping_data(extracted):
    
    import re
    
    pat = r'(nik|nama|tempat tanggal lahir|jenis kelamin|gol. darah|alamat|agama|status perkawinan|pekerjaan)'
    index = []

    dik = {}
    nilai = ''
    
    for i in extracted:
        if re.search(pat, i.strip()):
            index.append(extracted.index(i))
    
    for i in range(len(index)):
        start_idx = index[i]
        
        if i != (len(index)-1):
            
            end_idx = index[i+1]
        
        
            section = extracted[start_idx + 1:end_idx]

            if (end_idx-(start_idx+1)) != 1:
                nilai += ' '.join(section) + ' '
                nilai = nilai.strip()
                dik[extracted[start_idx]] = nilai

            else:
                dik[extracted[start_idx]] = section[0].strip()
        else:
            dik[extracted[start_idx]] = extracted[start_idx + 1]
    
    return dik


# In[3]:




