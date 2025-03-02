# Puppet manifest to fix incorrect filename reference in wp-settings.php

exec { 'fix_apache2':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/',
    notify  => Exec['restart_apache'],
}

exec { 'fix_mysql':
    command => 'sed -i s/myisam-recover/myisam-recover-options/g /etc/mysql/my.cnf',
    path    => '/usr/bin:/usr/sbin/',
    notify  => Exec['restart_mysql'],
}

# Restart Apache after applying the fix
exec { 'restart_apache':
    command => '/usr/sbin/apachectl restart',
}

# Restart mysql after applying the fix
exec { 'restart_mysql':
    command => 'service mysql restart',
    path    => '/usr/bin:/usr/sbin/',
}
