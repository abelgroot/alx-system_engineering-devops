# Use $HOME to refer to the current user's home directory
$home = $::env['HOME']

# Configure Host block for 61947-web-01
augeas { 'Configure SSH Host':
  context => "/files${home}/.ssh/config",
  changes => [
    "set Host[last()+1] '61947-web-01'",
    "set Host[last()]/HostName '3.85.136.194'",
    "set Host[last()]/User 'ubuntu'",
    "set Host[last()]/PasswordAuthentication 'no'",
    "set Host[last()]/IdentityFile '${home}/.ssh/school'",
  ],
  onlyif  => "match Host[*]/HostName[. = '3.85.136.194'] size == 0", # Prevent duplicates
  require => File["${home}/.ssh/config"],
}
