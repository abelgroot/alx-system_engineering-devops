exec { 'fix_wp_settings':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  onlyif  => "grep -q 'class-wp-locale.phpp' /var/www/html/wp-settings.php",
}
