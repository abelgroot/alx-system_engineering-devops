# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => Package['nginx'],
}

# Create the index.html file with Hello World! message
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure the Nginx site to handle the redirect
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80;
    root /var/www/html;
    index index.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 http://\$host/;
    }
}
",
  notify  => Service['nginx'],
}

# Reload Nginx to apply the new configuration
exec { 'reload_nginx':
  command => '/usr/sbin/service nginx reload',
  unless  => '/usr/bin/pgrep -f "nginx: master process" | grep -q "^1\$"',
  require => File['/etc/nginx/sites-available/default'],
}
