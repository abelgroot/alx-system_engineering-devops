# Puppet manifest to fix incorrect filename reference in wp-settings.php

exec { 'fix_wp_settings':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
    notify  => Exec['restart_apache'],
}
# Restart Apache after applying the fix
exec { 'restart_apache':
    command     => '/usr/sbin/apachectl restart',
    refreshonly => true,  # Only restart if notified
}
