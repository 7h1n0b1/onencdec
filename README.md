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
		-html ->  For html Encoding
		-bin -> For Binary Encoding
			--file -> Provide the file to be encoded (Encodes the whole file as one).

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
		-html -> For HTML Decoding
		-bin -> For binary decoding
			--file -> Provide the file to be decoded.

	Example: - python onencdec.py -d -b64 c3RyaW5n QW5vdGhlciBTdHJpbmc=
	Example: - python onencdec.py -d -b64 --file b64_enc_file.txt

	Interactive
	===========

	-> Prepare a file and save it on a preffered location.
	-> Make sure the file is new line seperated, as the tool takes new line as the word seperater.
	-> Fire Up the tool.
	-> Select "1" to encode and "2" to decode.
	-> Go through the rest of the options.
	-> The output will be saved in "operation.txt" file.
