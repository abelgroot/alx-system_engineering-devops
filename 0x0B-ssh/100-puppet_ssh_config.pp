# Add IdentityFile to ssh_config if not present
exec { 'Set IdentityFile':
  command => 'echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  unless  => 'grep -q "IdentityFile ~/.ssh/school" /etc/ssh/ssh_config',
  path    => ['/usr/bin', '/bin'],
}

# Add PasswordAuthentication to ssh_config if not present
exec { 'Disable PasswordAuthentication':
  command => 'echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  unless  => 'grep -q "PasswordAuthentication no" /etc/ssh/ssh_config',
  path    => ['/usr/bin', '/bin'],
}
