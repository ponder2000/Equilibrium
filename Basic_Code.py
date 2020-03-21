from Codes import *
value = Option_Chain_Scrapper('BANKNIFTY')
Strike_Price = value[1]['Unnamed: 11_level_0']['Strike Price']
call_oi = value[1]['CALLS']['OI']
put_oi = value[1]['PUTS']['OI']
