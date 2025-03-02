# Puppet manifest to fix incorrect filename reference in wp-settings.php
# This script replaces "class-wp-locale.phpp" with "class-wp-locale.php"
# ensuring WordPress can correctly locate the required file.
exec { 'fix_wp_settings':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  onlyif  => "grep -q 'class-wp-locale.phpp' /var/www/html/wp-settings.php",
}
