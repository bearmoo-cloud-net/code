import subprocess
import sys
import syslog
import smtplib
from time           import time
from optparse     import OptionParser

# Function that does basic standard output
def message(message):
    sys.stdout.write(message)
    sys.stdout.flush()

#This debug function is used to print more information and return a time.
def printDebugMessage(debugEnable, message):
    if debugEnable.lower() == 'yes':
        print message
        return time()

#Get command line options then return the variables.
def cliOptions():
    """
    Setup command-line parsing options
    """
    parser = OptionParser()
    parser.add_option('-o', '--output',             default = '',				dest = 'directory',      help = 'Where to save the files to.')
    parser.add_option('-p', '--passw',              default = '',				dest = 'passwd',        help = 'Provide a Password.')
    parser.add_option('-u', '--user',               default = 'admin',				dest = 'user',      help = 'Provide a user name.')
    return parser.parse_args()

#Take the contents of the array SiteGearReport and writing in a file in a directory. For example /tmp/SVL.out
def outToAFile(directory, messageToWriteOut):
    fileHandler = open(directory + "sample.out", "w")
    fileHandler.write(messageToWriteOut)
    fileHandler.close()

#will send an email to a mailing list.
def sendEmail(sendMailTo, message, theSender, emailServer):
    #Construct the message
    debugMessage (debug, "\n\n Starting the function sendEmail....")
    emailMessage="From: " + theSender + "\nTo: " + sendMailTo + "\nSubject: Test email."
    emailMessage+= "\n\n" + siteGearReport

    #Start the process to sending the email out
    try:
        message("\n\tConnecting the Email server: " + emailServer + "..... ")
        emailConn=smtplib.SMTP(emailServer)
        emailConn.sendmail(theSender, sendMailTo, emailMessage)
        emailConn.quit()
        message("\n\tSuccessfully sent email.")
    except:
        message("\n\tError: unable to send email")

# This function calls shell commands. Clean the output but removing the any newline and return charaters.
def externalCommands(command):
    processResults = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    results = processResults.stdout.readlines()

    results = map(lambda s: s.rstrip('\r\n'), results)
    return results