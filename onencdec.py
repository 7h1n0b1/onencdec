#/usr/bin/python

import base64, os, sys, urllib, codecs, binascii

###############################################################################

#############
# Tool Help #
#############

def tool_help():
	h = ''' 
	Summary
	=======

	One Encode Decode is a one stop tool for encoding and decoding solution.
	This tool can be used in two ways ie. Interactive and Non Interactive (command line).
	Example: -
	python onencdec -e my_string "Another string" -> Being the Non-Interactive mode
	or 
	python onencdec -> Being the Interactive Mode

	Non-Interactive
	===============

	-e -> For encoding the provided arguments.

		-b64 -> For Base64 Encoding
		-b32 -> For Base32 Encoding
		-b16 -> For Base16 Encoding
		-url -> For Url Encoding
		-rot13 -> For rot13 Encoding
		-uu -> For UU Encoding
		-hex -> For hex Encoding
			--file -> Provide the file to be encoded (Encodes the whole file).

	Example: - python onencdec.py -e -b64 string "Another String"
	Example: - python onencdec.py -e -b64 --file my_file.txt

	-d -> For decoding the provided arguments.

		-b64 -> For Base64 Decoding
		-b32 -> For Base32 Decoding
		-b16 -> For Base16 Decoding
		-url -> For Url Decoding
		-rot13 -> For rot13 Decoding
		-uu -> For UU Decoding
		-hex -> For hex Decoding
			-file -> Provide the file to be decoded.

	Example: - python onencdec.py -d -b64 c3RyaW5n QW5vdGhlciBTdHJpbmc=
	Example: - python onencdec.py -d -b64 --file b64_enc_file.txt

	Interactive
	===========

	-> Prepare a file and save it on a preffered location.
	-> Make sure the file is new line seperated, as the tool takes new line as the word seperater.
	-> Fire Up the tool.
	-> Select "1" to encode and "2" to decode.
	-> Go through the rest of the options.
	-> The output will be saved in "operations.txt" file.
	'''
	print h

#################
# Base64 Encode #
#################

def b64_enc(path):
	# path = raw_input('Enter file name: - ')
	# print(path)
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.readlines()
			for number in content:
				enc = base64.encodestring(number)
				wf.write(enc)
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

#################
# Base64 Decode #
#################

def b64_dec(path):
	# path = raw_input('Enter file name: - ')
	# print(path)
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.readlines()
			for number in content:
				try:
					dec = base64.decodestring(number)
				except:
					dec = "Not a valid operation.\n"
				wf.write(dec)
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file.")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

#################
# Base32 Encode #
#################

def b32_enc(path):
	# path = raw_input('Enter file name: - ')
	# print(path)
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.readlines()
			for number in content:
				enc = base64.b32encode(number)
				wf.write(enc+"\n")
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

#################
# Base32 Decode #
#################

def b32_dec(path):
	# path = raw_input('Enter file name: - ')
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.read().split('\n') 		# Have to split \n otherwise the decoder will produce an error.
			for number in content:
				try:
					dec = base64.b32decode(number)
				except:
					dec = "Not a valid operation.\n"
				wf.write(dec)
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

##############
# URL Encode #
##############

def url_enc(path):
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.readlines()
			for number in content:
				enc = urllib.quote(number)
				wf.write(enc+"\n")
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

##############
# URL Decode #
##############

def url_dec(path):
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.readlines()
			for number in content:
				try:
					dec = urllib.unquote(number)
				except:
					dec = "Not a valid operation.\n"
				wf.write(dec)
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

#################
# base16 Encode #
#################

def b16_enc(path):
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.readlines()
			for number in content:
				enc = base64.b16encode(number)
				wf.write(enc+"\n")
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

#################
# base16 Decode #
#################

def b16_dec(path):
	# path = raw_input('Enter file name: - ')
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.read().split('\n') 		# Have to split \n otherwise the decoder will give produce an error.
			for number in content:
				try:
					dec = base64.b16decode(number)
				except:
					dec = "Not a valid operation.\n"
				wf.write(dec)
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

################
# ROT13 Encode #
################

def rot13_enc(path):
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.readlines()
			for number in content:
				enc = codecs.encode(number, 'rot_13')
				wf.write(enc)
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

################
# ROT13 Decode #
################

def rot13_dec(path):
	# path = raw_input('Enter file name: - ')
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.read().split('\n') 		# Have to split \n otherwise the decoder will give produce an error.
			for number in content:
				try:
					dec = codecs.decode(number, 'rot_13')
				except:
					dec = "Not a valid operation.\n"
				wf.write(dec+"\n")
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

#############
# UU Encode #
#############

def uu_enc(path):
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.readlines()
			for number in content:
				enc = binascii.b2a_uu(number)
				wf.write(enc)
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

#############
# UU Decode #
#############

def uu_dec(path):
	# path = raw_input('Enter file name: - ')
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.read().split('\n') 		# Have to split \n otherwise the decoder will give produce an error.
			for number in content:
				try:
					dec = binascii.a2b_uu(number)
				except:
					dec = "Not a valid operation.\n"
				wf.write(dec+"\n")
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

##############
# Hex Encode #
##############

def hex_enc(path):
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.readlines()
			for number in content:
				enc = binascii.b2a_hex(number)
				wf.write(enc+"\n")
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")

##############
# Hex Decode #
##############

def hex_dec(path):
	# path = raw_input('Enter file name: - ')
	wf = open("operation.txt", 'w')
	if os.path.isfile(path):
		with open(path) as f:
			content = f.read().split('\n') 		# Have to split \n otherwise the decoder will give produce an error.
			for number in content:
				try:
					dec = binascii.a2b_hex(number)
				except:
					dec = "Not a valid operation.\n"
				wf.write(dec)
		f.close()
		wf.close()
		print("Done.... Data Stored in operation.txt file")
		sys.exit(0)
	else:
		print("There is something wrong with your file name!")


###############################################################################################################################
# Start of Main Program
###############################################################################################################################

########################################
# When arguments are provided run this #########################################
########################################

length=len(sys.argv) 	# Check the number of arguments.
# con=str(sys.argv)
# print sys.argv[0]
if length != 1: 		# If arguments are provided, run this.
########################################### Encoding ###########################################
	if sys.argv[1] == "-e":
########################################### Specific Encoding ###########################################
		if sys.argv[2] == '-b64':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read()
					print base64.encodestring(str(data))
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print base64.encodestring(str(sys.argv[i])) 	# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-b32':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read()
					print base64.b32encode(str(data))
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print base64.b32encode(str(sys.argv[i])) 	# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-b16':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read()
					print base64.b16encode(str(data))
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print base64.b16encode(str(sys.argv[i])) 	# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-url':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read()
					print urllib.quote(str(data))
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print urllib.quote(str(sys.argv[i])) 	# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-rot13':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read()
					print codecs.encode(str(data), 'rot_13')
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print codecs.encode(str(sys.argv[i]), 'rot_13') 	# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-uu':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read()
					#print binascii.b2a_uu(str(data))
					print(str(data)).encode('uu')
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print binascii.b2a_uu(str(sys.argv[i])) 	# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-hex':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read()
					print binascii.b2a_hex(str(data))
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print binascii.b2a_hex(str(sys.argv[i])) 	# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

########################################### All Encodings ###########################################
		print "=========================base64========================="
		i=2
		while i < length:
			try:
				print base64.encodestring(str(sys.argv[i])) 	# Try to Encode.
			except:
				i=i+1
				continue 										# Other wise continue.
			i=i+1
		print "\n=========================base32========================="
		i=2
		while i < length:
			try:
				print base64.b32encode(str(sys.argv[i])) 		# Try to Encode.
			except:
				i=i+1
				continue 										# Other wise continue.
			i=i+1
		print "\n=========================Base16========================="
		i=2
		while i < length:
			try:
				print base64.b16encode(str(sys.argv[i])) 		# Try to Encode.
			except:
				i=i+1
				continue 										# Other wise continue.
			i=i+1
		print "\n=========================URL========================="
		i=2
		while i < length:
			try:
				print urllib.quote(str(sys.argv[i])) 			# Try to Encode.
			except:
				i=i+1
				continue 										# Other wise continue.
			i=i+1

		print "\n=========================ROT13========================="
		i=2
		while i < length:
			try:
				string = str(sys.argv[i])
				print codecs.encode(string, 'rot_13') 			# Try to Encode.
			except:
				i=i+1
				continue 										# Other wise continue.
			i=i+1

		print "\n=========================UU========================="
		i=2
		while i < length:
			try:
				print binascii.b2a_uu(str(sys.argv[i])) 			# Try to Encode.
			except:
				i=i+1
				continue 										# Other wise continue.
			i=i+1

		print "\n=========================Hex========================="
		i=2
		while i < length:
			try:
				print binascii.b2a_hex(str(sys.argv[i])) 			# Try to Encode.
			except:
				i=i+1
				continue 											# Other wise continue.
			i=i+1

		sys.exit(0) 												# Exit after encoding.

####################################### Decoding #######################################
	elif sys.argv[1] == "-d":
####################################### Specific Decoding #######################################
		if sys.argv[2] == '-b64':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read()
					print base64.decodestring(str(data))
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print base64.decodestring(str(sys.argv[i])) 	# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-b32':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read().replace("\n", "")
					print base64.b32decode(str(data))
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print base64.b32decode(str(sys.argv[i])) 		# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-b16':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read().replace("\n", "")
					print data
					print base64.b16decode(str(data))
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print base64.b16decode(str(sys.argv[i])) 		# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-url':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read().replace("\n", "")
					print urllib.unquote(str(data))
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print urllib.unquote(str(sys.argv[i])) 	# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-rot13':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read().replace("\n", "")
					print codecs.decode(str(data), 'rot_13')
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print codecs.decode(str(sys.argv[i]), 'rot_13') 	# Try to Encode.
					except:
						i=i+1
						continue 											# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-uu':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read()
					#print binascii.b2a_uu(str(data))
					print(str(data)).decode('uu')
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print binascii.b2a_uu(str(sys.argv[i])) 		# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

		if sys.argv[2] == '-hex':
			if sys.argv[3] == '--file':
				file_name = sys.argv[4]
				with open(file_name, 'r') as myfile:
					data = myfile.read().replace("\n", "")
					print binascii.a2b_hex(str(data))
				sys.exit(0)
			else:
				i=3
				while i < length:
					try:
						print binascii.a2b_hex(str(sys.argv[i])) 		# Try to Encode.
					except:
						i=i+1
						continue 										# Other wise continue.
					i=i+1
				sys.exit(0)

####################################### All Decoding #######################################
		print "\n=========================base64========================="
		i=2
		while i < length:
			try:
				print base64.decodestring(str(sys.argv[i])) 	# Try to Decode.
			except:
				i=i+1
				continue 										# Other wise continue.
				#print "Not a base64 string"
			i=i+1
		print "\n=========================Base32========================="
		i=2
		while i < length:
			try:
				print base64.b32decode(str(sys.argv[i])) 		# Try to Decode.
			except:
				i=i+1
				continue 										# Other wise continue.
				#print "Not a base32 string"
			i=i+1
		print "\n=========================Base-16========================="
		i=2
		while i < length:
			try:
				print base64.b16decode(str(sys.argv[i])) 		# Try to Decode.
			except:
				i=i+1
				continue 										# Other wise continue.
				#print "Not a Base16 string"
			i=i+1

		print "\n=========================URL========================="
		i=2
		while i < length:
			try:
				print urllib.unquote(str(sys.argv[i])) 			# Try to Decode.
			except:
				i=i+1
				continue 										# Other wise continue.
				#print "Not a URL string"
			i=i+1

		print "\n=========================ROT13========================="
		i=2
		while i < length:
			try:
				string = str(sys.argv[i])
				print codecs.decode(string, 'rot_13') 			# Try to Decode.
			except:
				i=i+1
				continue 										# Other wise continue.
				#print "Not a URL string"
			i=i+1
		
		print "\n=========================UU========================="
		i=2
		while i < length:
			try:
				print binascii.a2b_uu(str(sys.argv[i])) 			# Try to Decode.
			except:
				i=i+1
				continue 										# Other wise continue.
				#print "Not a URL string"
			i=i+1

		print "\n=========================Hex========================="
		i=2
		while i < length:
			try:
				print binascii.a2b_hex(str(sys.argv[i])) 			# Try to Decode.
			except:
				i=i+1
				continue 										# Other wise continue.
				#print "Not a URL string"
			i=i+1

		sys.exit(0)

########################################### Help ###########################################
	elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
		tool_help()
		
		sys.exit(0)
########################################### Wrong Syntax ###########################################
	else:
		print("Check your syntax.")
		print("Do 'python onedecenc -e arg1 arg2' for encoding")
		print("Do 'python onedecenc -d arg1 arg2' for decoding")
		print("Type -h or --help for help")
		sys.exit(0)

####################
# End of Arguments ###############################################################
####################

print("oooooooooooo                       oooooooooo.                       ")
print("`888'     `8                       `888'   `Y8b                      ")
print(" 888         ooo. .oo.    .ooooo.   888      888  .ooooo.   .ooooo.  ")
print(" 888oooo8    `888P\"Y88b  d88' `\"Y8  888      888 d88' `88b d88' `\"Y8 ")
print(" 888    \"     888   888  888        888      888 888ooo888 888       ")
print(" 888       o  888   888  888   .o8  888     d88' 888    .o 888   .o8 ")
print("o888ooooood8 o888o o888o `Y8bod8P' o888bood8P'   `Y8bod8P' `Y8bod8P' ")
print("\n")

print "Make sure the characters in the file are seperated with new line\n" 

while True:
	print "================================= Main Menu =================================\n\n"
	print("Select your operation type.")
	print("1. Encode")
	print("2. Decode")
	print("\n")
	o_type=None
	e_type=None
	o_type=raw_input("> ")

	if o_type == "1": 		# When encoding is selected run this.

		while True:
			print "================================= Encoding =================================\n\n"
			print("Select the type of encoding")
			print("1. Base64")
			print("2. Base32")
			print("3. Base16")
			print("4. URL")
			print("5. ROT13")
			print("6. UU")
			print("7. Hex")
			print("99. For previous menu")
			e_type=raw_input("> ")

			if e_type == "1":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					b64_enc(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "2":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					b32_enc(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "3":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					b16_enc(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "4":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					url_enc(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "5":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					rot13_enc(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "6":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					uu_enc(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "7":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					hex_enc(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "99":
				break

			else:
				print("Please select a valid option")
				continue

	elif o_type == "2":

		while True:
			print "================================= Decoding =================================\n\n"
			print("Select the type of decoding")
			print("1. Base64")
			print("2. Base32")
			print("3. Base16")
			print("4. URL")
			print("5. ROT13")
			print("6. ROT13")
			print("7. Hex")
			print("99. Previous Menu")
			e_type=raw_input("> ")

			if e_type == "1":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					b64_dec(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "2":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					b32_dec(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "3":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					b16_dec(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "4":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					url_dec(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "5":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					rot13_dec(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "6":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					uu_dec(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "7":
				path=raw_input("Enter file's name > ")
				if os.path.isfile(path):
					hex_dec(path)
					break
				else:
					print("There is something wrong with the file name.")
					continue

			elif e_type == "99":
				break

			else:
				print("Please select a valid option")
				continue

	elif e_type == "99":
		continue

	else:
		print("\nPlease select a valid option\n")
		continue
