# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Werkzeug version 2.2.2 using pip3
exec { 'Install Werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.2.2',
  path    => ['/usr/bin', '/bin'],
  unless  => '/usr/bin/pip3 show Werkzeug | grep -q "Version: 2.2.2"',
  require => Package['python3-pip'],
}

# Install Flask version 2.1.0 using pip3
exec { 'Install Flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/bin'],
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}
