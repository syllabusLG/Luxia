#!/bin/bash

folder="/labdata/Hierarchy/METADATA_ROUTINE/_LUXIA_DATA_TRANSFER"
extension="fastq.gZ"
suffixR1="_R1_001.$extension"
suffixR2="_R2_001.$extension"

#Send FTP
sendFTP(){
	#FTP variables
	host="52.47.123.17"
	user="ibbl"
	ssh_key="/home/robot/bin/LUXIA/key/Luxia-sftp"
	
	# Arguments subject=$1; exp=$2; from=$3; dest=$4; cas=$5; files=$6
	sftp -i $ssh_key $user@$host 
	#put $1_
	echo "$1"
	put $folder/*.extension
	quit
	

}

#Check folder function
checkFolder(){
	path=$1

	echo "---- Checking folder $path"

	# Check if exists
	if ! [ -e $path ]; then
		# Failure
		echo -e "\e[31m\e[1m$path not exists\e[0m"
		#sendEmail "$subjectKO" "$exp" "$from" $path 1 $list_files
		python send_mail.py $path 1 ${list_files[@]}
        return 1
	fi

	# Check if its a folder
	if ! [ -d $path ]; then
		# Failure
		echo -e "\e[31m\e[1m$path not a folder\e[0m"
		#sendEmail "$subjectKO" "$exp" "$from" $path 2 $list_files
        python send_mail.py $path 2 ${list_files[@]}
        return 1
	fi

    # Count number of files
    nbFiles=`ls -1 $path | wc -l`
	
	# Retrieve list of files
	list_files=`ls -1 $path | grep -v /`

    if (( $nbFiles % 2 )); then
    	echo -e "\e[39m\e[1m$nbFiles files (odd)\e[0m"
    else
    	echo -e "\e[39m\e[1m$nbFiles files (even)\e[0m"
    fi

    # egrep '*_R[1-2]_001{1}.fastq.gz'`
    for prefix in `ls -1 $path | sed -e 's/_R[1-2]_001\+.fastq.gz//g' | uniq`
    do
        if ! [ -e $path/$prefix$suffixR1 -a -e $path/$prefix$suffixR2 ]; then
            # Failure
            echo -e "\e[31m\e[1mFailed\e[0m"
			#sendEmail "$subjectKO" "$exp" "$from" $dest_ibbl 3 $list_files
            python send_mail.py $path 3 ${list_files[@]}
            return 1
        fi
    done

    # Success
    echo -e "\e[32m\e[1mSuccess\e[0m"
    echo "$subjectOK" "$exp" "$from" "$to"
	echo "$listFiles"
	#sendFTP "$list_files" 
    #sendEmail "$subjectOK" "$exp" "$from" $dest_client 4 "$list_files"
    python send_mail.py $path 4 ${list_files[@]}
    return 0
}

checkFolder $folder

