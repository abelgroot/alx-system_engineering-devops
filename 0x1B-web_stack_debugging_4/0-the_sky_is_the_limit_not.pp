# Define a custom resource to update the ULIMIT value in /etc/default/nginx
exec { 'update_ulimit':
  command => "sed -i 's/15/65536/' /etc/default/nginx",
  path    => ['/bin', '/usr/bin'],  # Ensure sed is in the PATH
  notify  => Service['nginx'],  # Notify the Nginx service to restart
}

# Ensure the Nginx service is running and restart it if notified
service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  restart   => 'service nginx restart',  # Use "service nginx restart" instead of "systemctl"
}
