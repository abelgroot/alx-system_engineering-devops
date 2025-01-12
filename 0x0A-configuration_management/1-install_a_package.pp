# Ensure pip3 is installed
package { 'python3-pip':
  ensure => 'installed',
}

package { 'werkzeug':
  ensure => '2.2.2',
  provider => 'pip3',
}

# Install Flask 2.1.0 using pip3
exec { 'Install Flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/bin'],
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}
