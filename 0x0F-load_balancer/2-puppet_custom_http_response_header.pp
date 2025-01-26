# Puppet manifest to install, configure, and serve content with Nginx

node default {
  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure Nginx service is enabled and running
  service { 'nginx':
    ensure    => running,
    enable    => true,
    require   => Package['nginx'],
  }

  # Serve "Hello World!" on the root page
  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    mode    => '0644',
    owner   => 'www-data',
    group   => 'www-data',
    require => Package['nginx'],
  }

  # Set up redirection
  file_line { 'nginx_redirect_me':
    path  => '/etc/nginx/sites-available/default',
    line  => 'location ~^/redirect_me(/?)$ { return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4; }',
    match => 'server_name _;',
    after => 'server_name _;',
    require => Package['nginx'],
  }

  # Serve a custom 404 page
  file { '/var/www/html/custom_404.html':
    ensure  => file,
    content => "Ceci n'est pas une page",
    mode    => '0644',
    owner   => 'www-data',
    group   => 'www-data',
    require => Package['nginx'],
  }

  # Configure Nginx to use the custom 404 page
  file_line { 'nginx_custom_404':
    path  => '/etc/nginx/sites-available/default',
    line  => 'error_page 404 /custom_404.html; location = /custom_404.html { root /var/www/html; internal; }',
    match => 'server_name _;',
    after => 'server_name _;',
    require => Package['nginx'],
  }

  # Add a custom HTTP header
  file_line { 'nginx_custom_header':
    path  => '/etc/nginx/nginx.conf',
    line  => '    add_header X-Served-By $hostname;',
    match => 'http {',
    after => 'http {',
    require => Package['nginx'],
  }

  # Test Nginx configuration and restart service
  exec { 'nginx_config_test':
    command     => '/usr/sbin/nginx -t',
    refreshonly => true,
    subscribe   => File['/etc/nginx/sites-available/default', '/etc/nginx/nginx.conf'],
  }

  exec { 'restart_nginx':
    command     => '/bin/systemctl restart nginx',
    refreshonly => true,
    subscribe   => Exec['nginx_config_test'],
  }
}
