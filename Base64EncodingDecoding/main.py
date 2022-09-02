# This Python script to make Base64 Encoding and Base64 Decoding.

import base64

input_file = open('row_data_in.text', 'a+')
output_Encode_file = open('encoded_data_out.text', 'a+')
output_decode_file = open('decoded_data_out.text', 'a+')
list_data_in = ["Name: Moahmed Sayed ", "Age: 32 ", "job: Engineer \n"]
input_file.writelines(list_data_in)

with open('row_data_in.text', 'rb') as binary_in_data_reading:
    binary_file_data = binary_in_data_reading.read()
    base64_encoding = base64.b64encode(binary_file_data)
    base64_message = base64_encoding.decode('utf-8')
    output_Encode_file.writelines(base64_message)

with open('encoded_data_out.text', 'rb') as binary_in_base64_reading:
    binary_file_data = binary_in_base64_reading.read()
    base64_decoding = base64.b64decode(binary_file_data)
    base64_message = base64_decoding.decode('utf-8')
    output_decode_file.writelines(base64_message)
