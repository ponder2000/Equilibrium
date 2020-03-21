from tqdm import trange
from Codes import *
import json

# list of queries
Underlying_Stock = fno_list()

# to store the searched result
Underlying_Stock_with_value = dict()

# scarping the data
for a in trange(len(Underlying_Stock), desc = 'Number of Stock'):
    print(Underlying_Stock[a])

    # getting the values
    value = Option_Chain_Scrapper(str(Underlying_Stock[a]))
    Strike_Price = value['Unnamed: 11_level_0']['Strike Price']
    call_oi = value['CALLS']['OI'].replace('-','0')
    put_oi = value['PUTS']['OI'].replace('-','0')

    # converting the pandas series into list for easy operation
    Strike_Price = list(Strike_Price)
    call_oi = list(call_oi)
    put_oi = list(put_oi)

    # removing the last total row
    Strike_Price = Strike_Price[:len(Strike_Price)-1]
    call_oi = call_oi[:len(call_oi)-1]
    put_oi = put_oi[:len(put_oi)-1]

    # converting into float for numerical calculation
    Strike_Price = list(map(float, Strike_Price))
    call_oi = list(map(float, call_oi))
    put_oi = list(map(float, put_oi))

    values = []
    for j in range(len(Strike_Price)):
        instrinic_value = []
        for i in range(len(Strike_Price)):
            if Strike_Price[i] <= Strike_Price[j]:
                instrinic_value.append(float(Strike_Price[j] - Strike_Price[i]) * float(call_oi[i]))
            else:
                instrinic_value.append(float(Strike_Price[i] - Strike_Price[j]) * float(put_oi[i]))
        values.append(sum(instrinic_value))


    #MAX PAIN CALCULATION
    try:
        max_pain_point = Strike_Price[values.index(min(values))]
    except:
        print(f"No data available on required stock! length of value = {len(values)}\nHence making max_pain_point = 0")
        max_pain_point = 0

    #Calculating PCR
    try:
        pcr = sum(put_oi)/sum(call_oi)
    except:
        print(f"Either of put_oi or call_oi must be zero. len_put_oi, len_call_oi = {len(put_oi)}, {len(call_oi)}")
        pcr = 0

    # storing the values for further use
    Underlying_Stock_with_value[Underlying_Stock[a]] = {'Max_Pain_Point':None, 'PCR': None, 'Values': None}
    Underlying_Stock_with_value[Underlying_Stock[a]]['Max_Pain_Point'] = max_pain_point
    Underlying_Stock_with_value[Underlying_Stock[a]]['PCR'] = pcr
    Underlying_Stock_with_value[Underlying_Stock[a]]['Values'] = values


# storing into a json object
with open('Underlying_Stock_With_value.json', 'w') as f:
    json.dump(Underlying_Stock_with_value, f)

print("Scraping done!!!")
