# Puppet manifest to fix incorrect filename reference in wp-settings.php
# This script replaces "class-wp-locale.phpp" with "class-wp-locale.php"
# and restarts Apache to apply changes.

exec { 'fix_wp_settings':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
}
