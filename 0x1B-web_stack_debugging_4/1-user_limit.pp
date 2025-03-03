# Puppet manifest to increase the file descriptor limit for the holberton user

# Update the /etc/security/limits.conf file to increase the file descriptor limit for the holberton user
file_line { 'increase_holberton_soft_limit':
  ensure => present,
  path   => '/etc/security/limits.conf',
  line   => 'holberton soft nofile 65536',
  match  => '^holberton soft nofile',
}

file_line { 'increase_holberton_hard_limit':
  ensure => present,
  path   => '/etc/security/limits.conf',
  line   => 'holberton hard nofile 65536',
  match  => '^holberton hard nofile',
}

# Ensure the PAM limits module is configured to use /etc/security/limits.conf
file_line { 'enable_pam_limits':
  ensure => present,
  path   => '/etc/pam.d/common-session',
  line   => 'session required pam_limits.so',
  match  => '^session\s+required\s+pam_limits\.so',
}

# Apply the changes immediately for the current session
exec { 'apply_limits':
  command     => 'sysctl -p /etc/security/limits.conf',
  path        => ['/sbin', '/usr/sbin', '/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => [File_line['increase_holberton_soft_limit'], File_line['increase_holberton_hard_limit']],
}
