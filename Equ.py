from Codes import *
Underlying_Stock = fno_list()
a = 0
while a < len(Underlying_Stock):
    print(Underlying_Stock[a])
    value = Option_Chain_Scrapper(str(Underlying_Stock[a]))[1]
    Strike_Price = value['Unnamed: 11_level_0']['Strike Price']
    call_oi = value['CALLS']['OI'].replace('-','0')
    put_oi = value['PUTS']['OI'].replace('-','0')
    Strike_Price.to_list().pop()
    call_oi.to_list().pop()
    put_oi.to_list().pop()
    #MAX PAIN CALCULATION
    j = 0
    values = []
    while j < len(Strike_Price):
        i = 0
        l = 1
        instrinic_value = []
        while i < len(Strike_Price):
            if Strike_Price[i] <= Strike_Price[j]:
                instrinic_value.append(float(Strike_Price[j] - Strike_Price[i]) * float(call_oi[i]))
                i += 1
            else:
                instrinic_value.append(float(Strike_Price[i] - Strike_Price[j]) * float(put_oi[i]))
                i += 1
        values.append(sum(instrinic_value))
        j += 1
    print("Max Pain Point")
    #print(Strike_Price[values.index(min(values))])
    #Calculating PCR
    #print("PCR:")
    #print((sum(put_oi)/sum(call_oi)))
    print('\n')
    a += len(Underlying_Stock)
