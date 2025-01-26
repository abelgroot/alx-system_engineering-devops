# Puppet manifest to fully replicate the functionality of the provided Bash script

# Update the package list
exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
}

# Install Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get update'],
}

# Ensure Nginx is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx to serve "Hello World!" on the root page
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
  mode    => '0755',
  require => Package['nginx'],
}

# Set up redirection in the Nginx default configuration
exec { 'setup_redirection':
  command => "/bin/sed -i '/server_name _;/a \\
    location ~^/redirect_me(/?)$ {\\
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\\
    }' /etc/nginx/sites-available/default",
  unless  => "/bin/grep -q 'location ~^/redirect_me(/?)$' /etc/nginx/sites-available/default",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create a custom 404 page
file { '/var/www/html/custom_404.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n",
  require => Package['nginx'],
}

# Configure Nginx to use the custom 404 page
exec { 'configure_custom_404':
  command => "/bin/sed -i '/server_name _;/a \\
    error_page 404 /custom_404.html;\\n    location = /custom_404.html {\\n        root /var/www/html;\\n        internal;\\n    }' /etc/nginx/sites-available/default",
  unless  => "/bin/grep -q 'error_page 404 /custom_404.html;' /etc/nginx/sites-available/default",
  require => File['/var/www/html/custom_404.html'],
  notify  => Service['nginx'],
}

# Add the custom header to the Nginx configuration
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
