from optparse import OptionParser

def cliOptions():
  """
  Setup command-line parsing options
  """
  parser = OptionParser()
  parser.add_option('-a', '--access-key',   default = '',      dest = 'accessKey',   help = 'Rancher api account access key.')
  parser.add_option('-s', '--secret-key',   default = '',      dest = 'secretKey',   help = 'Rancher api account secret key' )
  parser.add_option('-u', '--user',         default = 'admin', dest = 'user',        help = 'User account for rancher.'      )
  parser.add_option('-p', '--port',         default = '8080',  dest = 'port',        help = 'default port to use.'           )
  #parser.add_option('-i', '--ipaddress',    default = '',      dest = 'ipaddress',   help = 'Host ipaddress ou wish to add.' )
  parser.add_option('-r', '--rancherhost', default = '',      dest = 'rancherHost', help = 'Rancher host server.'           )
  #parser.add_option('-h', '--hostname',     default = '',      dest = 'hostname',    help = 'Host server name.'              )
  #parser.add_option('-sa', '--sshaccount',  default = 'root',  dest = 'sshcount',    help = 'ssh account to use.'            )
  #parser.add_option('-d', '--description',  default = '',      dest = 'description', help = 'Add a destription.'             )
  return parser.parse_args()
