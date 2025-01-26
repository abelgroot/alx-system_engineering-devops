# Puppet manifest to configure Nginx with a custom HTTP header (X-Served-By)

# Ensure Nginx is installed and running
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Add the custom header to the Nginx configuration using sed
exec { 'add_custom_header':
  command => "/bin/sed -i '/http {/a \\    add_header X-Served-By \$hostname;' /etc/nginx/nginx.conf",
  unless  => "/bin/grep -q 'add_header X-Served-By \$hostname;' /etc/nginx/nginx.conf",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Test the Nginx configuration before restarting
exec { 'nginx_test_config':
  command     => '/usr/sbin/nginx -t',
  refreshonly => true,
  notify      => Service['nginx'],
}
