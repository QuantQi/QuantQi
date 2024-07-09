Test Case #,Description,Preconditions,Steps,Expected Results
1,Validate pickup of MT103 savings files,Encrypted MT103 savings files on Winshare,"1. Verify EFT picks up the files from Winshare. 2. Verify EFT uploads the files to S3 input folder.",Files are picked up and uploaded to S3 input folder.
2,Validate pickup of MT103 mortgage files,Encrypted MT103 mortgage files on Winshare,"1. Verify EFT picks up the files from Winshare. 2. Verify EFT uploads the files to S3 input folder.",Files are picked up and uploaded to S3 input folder.
3,Validate encryption of transformed PACS.008 files,PACS.008 files after transformation,"1. Verify microservices encrypt PACS.008 files. 2. Verify encrypted files are pushed to S3 output folder.",Transformed PACS.008 files are encrypted and pushed to S3 output folder.
4,Validate pickup of encrypted PACS.008 files by EFT,Encrypted PACS.008 files in S3 output folder,"1. Verify EFT picks up the encrypted PACS.008 files from S3 output folder.",Encrypted PACS.008 files are picked up by EFT.
5,Validate decryption and archiving of PACS.008 files,Encrypted PACS.008 files picked up by EFT,"1. Verify EFT decrypts the PACS.008 files. 2. Verify EFT saves a decrypted copy to Winshare archive.",PACS.008 files are decrypted and a copy is saved to Winshare archive.
6,Validate upload of encrypted PACS.008 files to HSBC SFTP connect,Encrypted PACS.008 files picked up by EFT,"1. Verify EFT uploads an encrypted copy to HSBC SFTP connect server.",An encrypted copy of PACS.008 files is uploaded to HSBC SFTP connect server.
7,Validate error logging for network failures during file upload,Simulated network failure,"1. Simulate network failure during EFT file upload to S3. 2. Verify error is logged in BAM or EFT logs.",Network failure is detected, and error is logged in BAM or EFT logs.
8,Validate error logging for decryption failures,Corrupted or incorrectly encrypted files,"1. Verify EFT attempts to decrypt corrupted/encrypted PACS.008 files. 2. Verify error is logged in BAM or EFT logs.",Decryption failure is detected, and error is logged in BAM or EFT logs.
9,Validate complete flow from pickup to upload,Valid MT103 file,"1. Verify EFT picks up the file from Winshare. 2. Verify microservices transform and encrypt the file. 3. Verify EFT decrypts and archives the file. 4. Verify EFT uploads the file to HSBC SFTP connect server.",Complete flow is validated from file pickup, transformation, encryption, decryption, archiving, and upload.