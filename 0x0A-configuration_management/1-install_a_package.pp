# This Puppet manifest installs Flask version 2.1.0 using pip3.
package { 'python3-pip':
    ensure => installed,
}

# Install Flask 2.1.0 using an exec resource
package { 'flask':
    ensure => installed,
    name => 'flask~=2.1.0',
    provider => 'pip3',
}
