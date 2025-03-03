# Puppet manifest to increase the file descriptor limit for the holberton user using sed

# Update the soft limit for the holberton user in /etc/security/limits.conf
exec { 'update_holberton_soft_limit':
  command => "sed -i '/^holberton\\s\\+soft\\s\\+nofile/c\\holberton soft nofile 65536' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],  # Ensure sed is in the PATH
}

# Update the hard limit for the holberton user in /etc/security/limits.conf
exec { 'update_holberton_hard_limit':
  command => "sed -i '/^holberton\\s\\+hard\\s\\+nofile/c\\holberton hard nofile 65536' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],  # Ensure sed is in the PATH
}
