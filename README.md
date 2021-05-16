
Python script for finding and printing information about package which has been 
downloaded from Ubuntu repository. The script require one mandatory argument for 
specification of path to Ubuntu package (in deb format) as the input

"-p | --package" specify path to package (in deb format)
support following optional arguments:
"-l | --changelog" parse changelog and print description for this specific version

Example input:
python3 package_info.py -l -p /Downloads/curl_7.58.0.deb
