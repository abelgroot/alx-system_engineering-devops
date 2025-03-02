# Puppet manifest to fix incorrect filename reference in wp-settings.php
# This script replaces "class-wp-locale.phpp" with "class-wp-locale.php"
# and restarts Apache to apply changes.

exec { 'fix_wp_settings':
  command     => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin/'
  # Ensure the Apache service is restarted after fixing the issue
  notify      => Exec['restart_apache'],
}

# Restart Apache after applying the fix
exec { 'restart_apache':
  command     => '/usr/sbin/apachectl restart',
  refreshonly => true,  # Only restart if notified
}
